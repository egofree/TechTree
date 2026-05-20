"""Wikimedia API client with retry, backoff, and rate-limit handling.

Stdlib-only HTTP client for interacting with Wikimedia APIs
(Commons, Wikipedia, Wikidata). Provides configurable base URL,
custom User-Agent, retry with exponential backoff, and proper
error handling for HTTP errors, timeouts, and rate limiting.
"""

import json
import time
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_USER_AGENT = "BootCivImageBot/1.0 (https://github.com/bootciv; educational CC0 project)"

DEFAULT_TIMEOUT = 30

DEFAULT_BASE_URL = "https://commons.wikimedia.org/w/api.php"


class WikiClient:
    """HTTP client for Wikimedia APIs with retry and backoff.

    Args:
        base_url: API endpoint URL (default: Wikimedia Commons).
        user_agent: User-Agent header value.
        timeout: Request timeout in seconds.
        max_retries: Number of retry attempts on transient errors.
        retry_delay: Initial delay in seconds between retries (doubles each attempt).
    """

    def __init__(self, base_url=None, user_agent=None, timeout=None,
                 max_retries=1, retry_delay=5):
        self.base_url = base_url or DEFAULT_BASE_URL
        self.user_agent = user_agent or DEFAULT_USER_AGENT
        self.timeout = timeout or DEFAULT_TIMEOUT
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    @property
    def headers(self):
        """Default HTTP headers for all requests."""
        return {"User-Agent": self.user_agent}

    def get(self, url=None, params=None):
        """Make a GET request with retry and exponential backoff.

        Args:
            url: Full URL to request. If None, constructed from base_url + params.
            params: Dict of query parameters (used when url is None).

        Returns:
            Response body as bytes, or None on failure after retries exhausted.
        """
        if url is None:
            qs = urllib.parse.urlencode(params or {})
            url = "{}?{}".format(self.base_url, qs)
        req = urllib.request.Request(url, headers=self.headers)
        delay = self.retry_delay
        for attempt in range(self.max_retries + 1):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    return resp.read()
            except urllib.error.HTTPError as exc:
                if exc.code == 429:
                    # Rate limited — honor Retry-After if present
                    retry_after = exc.headers.get("Retry-After")
                    wait = float(retry_after) if retry_after else delay
                    print("    Rate limited (429), waiting {:.0f}s...".format(wait))
                    time.sleep(wait)
                    delay *= 2
                    continue
                if attempt < self.max_retries:
                    print("    Retry after HTTP error: {}".format(exc))
                    time.sleep(delay)
                    delay *= 2
                    continue
                print("    Skipping due to HTTP error: {}".format(exc))
                return None
            except (urllib.error.URLError, OSError) as exc:
                if attempt < self.max_retries:
                    print("    Retry after error: {}".format(exc))
                    time.sleep(delay)
                    delay *= 2
                    continue
                print("    Skipping due to error: {}".format(exc))
                return None
        return None

    def get_json(self, url=None, params=None):
        """Make a GET request and parse the JSON response.

        Args:
            url: Full URL to request. If None, constructed from base_url + params.
            params: Dict of query parameters (used when url is None).

        Returns:
            Parsed JSON as dict/list, or None on failure.
        """
        data = self.get(url=url, params=params)
        if data is None:
            return None
        try:
            return json.loads(data.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            print("    Skipping due to JSON parse error: {}".format(exc))
            return None
