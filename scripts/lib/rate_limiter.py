"""Rate limiting and retry logic for Wikimedia API calls.

Stdlib-only. Designed to be shared across Wikipedia, Wikidata, and Commons APIs.

Usage:
    from lib.rate_limiter import RateLimiter, RetryHandler

    limiter = RateLimiter(requests_per_second=1, burst=3)
    retry = RetryHandler(base_delay=5, max_retries=3)

    limiter.wait()
    data = retry.call(api_request_func, params)
"""

import time
import threading


class RateLimiter:
    """Token-bucket rate limiter for API call throttling.

    Args:
        requests_per_second: Target sustained request rate.
        burst: Maximum number of requests that can fire in rapid succession
               before the bucket empties and throttling kicks in.
    """

    def __init__(self, requests_per_second=1.0, burst=3):
        self._rps = requests_per_second
        self._burst = max(1, burst)
        self._tokens = float(self._burst)
        self._last = time.monotonic()
        self._lock = threading.Lock()

    def wait(self):
        """Block until a request token is available, then consume one."""
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last
            self._last = now
            self._tokens = min(self._burst, self._tokens + elapsed * self._rps)

            if self._tokens < 1.0:
                sleep_time = (1.0 - self._tokens) / self._rps
                time.sleep(sleep_time)
                self._tokens = 0.0
            else:
                self._tokens -= 1.0


class RetryHandler:
    """Exponential-backoff retry wrapper for flaky API calls.

    Args:
        base_delay: Seconds to wait before the first retry.
        max_retries: Maximum number of retry attempts (0 = no retry).
        backoff_factor: Multiplier applied to delay after each attempt.
    """

    def __init__(self, base_delay=5, max_retries=1, backoff_factor=2.0):
        self._base_delay = base_delay
        self._max_retries = max_retries
        self._backoff_factor = backoff_factor

    def call(self, func, *args, **kwargs):
        """Call *func* with retries on exception.

        Returns the function result on success, or None after all retries
        are exhausted.  Exceptions are printed, not re-raised.

        (Mirrors the original api_request behaviour of returning None on failure.)
        """
        last_exc = None
        for attempt in range(self._max_retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    delay = self._base_delay * (self._backoff_factor ** attempt)
                    print("    Retry {}/{} after error: {}".format(
                        attempt + 1, self._max_retries, exc))
                    time.sleep(delay)
                else:
                    print("    Skipping due to error: {}".format(exc))
        return None

    @property
    def base_delay(self):
        return self._base_delay

    @property
    def max_retries(self):
        return self._max_retries
