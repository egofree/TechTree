# Operating System Construction

> **Node ID**: software-bootstrapping.operating-systems
> **Domain**: [Software Bootstrapping](./index.md)
> **Dependencies**: [`software-bootstrapping.assemblers`](assemblers.md), [`computing.data-storage`](../computing/data-storage.md)
> **Enables**: [`software-bootstrapping.dev-tools`](dev-tools.md)
> **Timeline**: Years 55-70
> **Outputs**: operating_system, process_management, file_systems
> **Critical**: Yes — the OS manages hardware resources and provides the execution environment for all application software


An operating system (OS) manages the computer's hardware resources — processor time, memory, storage, and I/O devices — and provides services that application programs use: file storage, process execution, input/output, and memory allocation. Without an OS, each program must contain its own device drivers, memory management, and I/O routines, making programs large, complex, and machine-specific.

The OS evolves through stages, mirroring the bootstrap chain:
1. **Monitor program**: A simple program that reads commands from the console and loads/executes other programs. No multitasking, no memory protection.
2. **Batch monitor**: Reads jobs from paper tape or cards, executes each in sequence, prints output. Automatic job sequencing.
3. **Single-user OS**: Interactive command interpreter (shell), file system on disk, basic device drivers. One program at a time.
4. **Multi-tasking OS**: Multiple programs in memory simultaneously, time-sliced execution, memory protection, privileged instructions.

Each stage is built using the tools from previous stages — initially in assembly language, then in a high-level language once a compiler is available.


## Software
- **Working assembler** ([assemblers](assemblers.md)): OS kernels are initially written in assembly language for the interrupt handlers, context switching, and device driver low-level routines.
- **Compiler** ([compilers](compilers.md)): Once available, most OS code (file systems, shell, utilities) is written in a high-level language. Only hardware-specific routines remain in assembly.

## Hardware
- **Computer with ≥16 KB memory**: A minimal monitor needs 1-4 KB; a useful single-user OS needs 16-64 KB; a multitasking OS needs 64-256 KB or more.
- **Disk or reliable storage** ([computing.data-storage](../computing/data-storage.md)): The OS needs persistent storage for the file system. Paper tape is too slow for interactive use.
- **Timer/clock interrupt**: For multitasking, the hardware must generate periodic interrupts that the OS uses to switch between processes.
- **Memory protection** (optional, for multitasking): Hardware mechanism to prevent one process from overwriting another's memory (base/limit registers, or later, an MMU).

## Knowledge
- **Interrupt handling**: How the processor responds to hardware interrupts (save context, vector to handler, restore context, return from interrupt).
- **Device I/O**: How to program the specific I/O controllers for disk, terminal, printer, etc.
- **Data structures**: Linked lists (process queues), trees (file directories), bitmaps (memory allocation), stacks (interrupt context saving).

## Bill of Materials

| Item | Quantity | Source | Alternatives |
|------|----------|--------|-------------|
| Computer with ≥16 KB memory | 1 unit | [computing.electronic](../computing/electronic.md) | Minimal monitor works with 4 KB |
| Disk storage | ≥100 KB capacity | [computing.data-storage](../computing/data-storage.md) | Magnetic drum, tape (slow but functional) |
| Terminal (teletype or CRT) | 1 unit | [computing.electronic](../computing/electronic.md) | Hardwired control panel |
| Timer/clock hardware | 1 unit | Part of computer architecture | Software timing loops (single-tasking only) |


## Stage 1: Monitor Program

The monitor is the simplest OS — a single program that provides:
- **Command reading**: Read a command line from the terminal (e.g., `RUN PROG1`, `LOAD TAPE`, `DUMP 1000-1FFF`).
- **Program loading**: Read a program from paper tape or disk into memory at a fixed address.
- **Program execution**: Jump to the loaded program's entry point.
- **Return to monitor**: The loaded program returns control to the monitor when finished (via a jump to the monitor's reentry point).

**Implementation** (~500-2,000 bytes of code):
```
MONITOR:
    PRINT ">"
    READ_LINE command_buffer
    PARSE command
    
    IF command = "RUN":
        LOAD program from default device
        CALL entry_point
        GOTO MONITOR
    
    IF command = "LOAD":
        READ filename from argument
        LOAD program from named file
        GOTO MONITOR
    
    IF command = "DUMP":
        READ address range
        DISPLAY memory contents in hex
        GOTO MONITOR
```

## Stage 2: Boot Loader

The boot loader is the first code that runs when the computer powers on. Its job is to load the OS from disk into memory and transfer control to it.

**Boot sequence**:
1. Hardware loads the boot sector (first 128-512 bytes on disk) into memory at a fixed address (e.g., address 0x0000 or 0x7C00) and jumps to it.
2. Boot loader initializes the stack pointer and segment registers.
3. Boot loader reads the OS kernel from disk sectors into memory (using BIOS-like disk I/O routines, or direct disk controller programming).
4. Boot loader jumps to the kernel's entry point.

**Boot loader size**: 128-512 bytes (fits in one disk sector). Written in assembly language, hand-positioned to fit.

## Stage 3: Interrupt Handlers

Interrupts are the mechanism by which hardware signals the processor:

**Interrupt processing**:
1. Hardware device raises an interrupt signal.
2. Processor completes the current instruction.
3. Processor saves the current program counter and status register to the stack.
4. Processor loads the interrupt handler address from the interrupt vector table.
5. Interrupt handler executes (service the device, acknowledge the interrupt).
6. Handler executes "return from interrupt" — restores PC and status from stack.
7. Interrupted program resumes where it left off.

**Critical handlers to implement**:
- **Timer interrupt**: Fires every 10-100 ms. Used for time-slicing (multitasking) and maintaining the system clock.
- **Disk interrupt**: Signals completion of a disk read/write operation.
- **Terminal interrupt**: Signals a character received from the keyboard.
- **Power-fail interrupt**: On systems that support it, gives the OS ~2 ms to save critical state before power dies.

## Stage 4: Process Management (Multitasking)

**Process control block (PCB)**: A data structure for each process containing:
- Saved register values (including PC, stack pointer, status register)
- Process state (running, ready, blocked)
- Memory allocation (base address, size)
- Open file list
- Scheduling priority

**Context switch** (triggered by timer interrupt):
1. Timer interrupt fires.
2. Save current process's registers to its PCB.
3. Select next process from the ready queue (scheduler).
4. Load the new process's registers from its PCB.
5. Return from interrupt → new process resumes.

**Round-robin scheduler**: Each process gets a time slice (e.g., 50 ms). When the timer interrupt fires, the scheduler moves to the next ready process. Simple, fair, adequate for most purposes.

## Stage 5: Memory Management

**Simple scheme (single-tasking)**: One program in memory at a time. The OS occupies low memory; the application occupies the rest.

**Fixed partition**: Divide memory into fixed-size partitions. Each process gets one partition. Wastes memory if the process is smaller than the partition. Simple to implement.

**Variable partition**: Allocate memory blocks on demand. Track free and allocated blocks with a linked list or bitmap. Coalesce adjacent free blocks when a process terminates. Problem: external fragmentation (free memory is scattered in small chunks too small to use).

**Base/limit registers**: Hardware provides two registers per process — base (lowest address the process can access) and limit (size of the process's address space). The OS sets these registers during context switch. Prevents processes from accessing each other's memory.

## Stage 6: File System

**File system data structures**:

**Disk layout**:
```
| Block 0: Boot sector | Block 1: Superblock | Blocks 2-N: Inodes | Blocks N+1 to end: Data blocks |
```

- **Superblock**: Total blocks, free block count, free block list, inode count. Read on mount; cached in memory.
- **Inode** (index node): Per-file metadata — size, permissions, timestamps, and block pointers (direct, indirect, double-indirect). A single inode might have 10 direct block pointers (covering 10 KB for 1 KB blocks), 1 single-indirect pointer (256 additional blocks = 256 KB), and 1 double-indirect pointer (65,536 additional blocks = 64 MB).
- **Directory**: A file containing a list of (filename, inode_number) pairs. The root directory is at a fixed inode number (inode 2 traditionally).

**Operations**:
- `open(path)`: Walk directory tree → find inode → load into memory → return file descriptor.
- `read(fd, buffer, count)`: Read from current file position → advance position → return bytes read.
- `write(fd, buffer, count)`: Write to current position → advance → allocate new blocks if needed → return bytes written.
- `close(fd)`: Flush buffers → release file descriptor → update inode on disk.

**File allocation strategies**:

| Strategy | Contiguous | Linked List | Indexed (inode) |
|----------|-----------|-------------|-----------------|
| Allocation | One contiguous block range | Each block points to next | Inode contains block pointers |
| Read performance | Excellent (sequential) | Poor (follow pointers) | Good (direct access) |
| Fragmentation | Severe external | None | Mild (indirect blocks) |
| Max file size | Limited by largest free gap | Unlimited | Limited by pointer count |
| Complexity | Simple | Simple | Moderate |

## Stage 7: Device Drivers

Each hardware device needs a driver — a software module that knows how to program the device's controller:

**Driver structure**:
1. **Open**: Initialize the device, allocate buffers.
2. **Read/Write**: Program the device controller (write command register, data register, start operation). For disk: specify cylinder/head/sector, data buffer address, direction (read/write), and start.
3. **Interrupt handler**: Called when the device signals completion. Copy data from device buffer to memory (or vice versa). Wake up any waiting process.
4. **Close**: Release buffers, power down device.

**Device independence**: The OS provides a uniform interface (open/read/write/close) regardless of device type. Application programs call `read(fd, buffer, count)` without knowing whether `fd` refers to a disk file, terminal, printer, or tape drive.

## Quantitative Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Monitor program size | 0.5-4 KB | Simple command loop + loader |
| Minimal kernel size | 4-16 KB | Interrupt handlers + basic I/O + loader |
| Full single-user OS | 16-64 KB | File system + shell + utilities |
| Multi-tasking OS kernel | 32-256 KB | Process management + memory protection + IPC |
| Context switch time | 10-500 μs | Save/restore registers + scheduler |
| Timer interrupt frequency | 10-100 Hz | 10-100 ms time slices |
| File system overhead | 1-5% of disk | Superblock + inodes + free list |
| Minimum disk block size | 512-4,096 bytes | Trade-off: small = less waste, large = less metadata |
| Boot time | 1-30 sec | From power-on to shell prompt |

## Memory Layout (Typical 64 KB System)

| Address Range | Contents | Size |
|--------------|----------|------|
| 0x0000-0x00FF | Interrupt vector table | 256 bytes |
| 0x0100-0x3FFF | OS kernel | ~16 KB |
| 0x4000-0x4FFF | OS buffers, stacks | 4 KB |
| 0x5000-0xEFFF | User program space | ~40 KB |
| 0xF000-0xFFFF | ROM / firmware | 4 KB |

## Scaling Notes

**From monitor to OS**: The monitor program (500-2,000 bytes) is the starting point. Add features incrementally: file system first (enables persistent storage), then command shell, then multitasking.

**From single-tasking to multi-tasking**: Single-tasking is adequate for most bootstrap purposes. Multi-tasking adds significant complexity (context switching, memory protection, synchronization primitives). Implement only when multiple interactive users or background tasks are needed.

**From flat memory to virtual memory**: Flat memory (all processes share one address space with base/limit protection) is sufficient for bootstrap. Virtual memory (each process has its own address space, with an MMU translating virtual to physical addresses) adds 5,000-20,000 lines of code and requires hardware MMU support.

**From single-processor to multi-processor**: Symmetric multiprocessing (SMP) — multiple CPUs sharing memory — adds lock-based synchronization throughout the kernel. Each shared data structure needs a spinlock or mutex. Starting point for SMP: add a lock to the scheduler, the memory allocator, and the device driver framework.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| System hangs on boot | Boot loader fails to read kernel from disk; wrong disk sector | Verify boot sector loads correctly by single-stepping; check disk controller programming |
| Crash on first interrupt | Interrupt vector table not initialized; handler at wrong address | Verify interrupt vector points to correct handler address; test handler with a software interrupt |
| File system corruption | Power loss during write; disk write not flushed | Implement write-ahead logging (journaling); flush metadata writes before data writes |
| Process crash corrupts OS | No memory protection; user process overwrites OS memory | Add base/limit registers; mark OS memory as privileged |
| System runs out of memory | Memory leak (allocated but never freed); fragmentation | Add memory allocation tracking; implement free list coalescing; limit process memory allocation |
| Deadlock (system freezes) | Two processes each holding a resource the other needs | Implement resource ordering (always acquire locks in same order); add timeout to lock acquisition |

## Safety

- **Data loss**: The most serious risk. A bug in the file system can destroy all stored data. Always maintain a backup strategy — duplicate critical files on a second storage medium.
- **Power failure**: Sudden power loss during disk writes corrupts open files and file system metadata. Use a UPS (uninterruptible power supply) or implement a journaling file system that recovers consistently after a crash.
- **No physical hazards**: OS construction is purely software. The hazards are data integrity, not personal safety.

## Quality Control

**OS test sequence**:
1. Boot from cold start — verify kernel loads and prints banner.
2. Load and run a test program — verify it produces correct output.
3. Create a file, write data, close, reopen, read back — verify data matches.
4. Run two programs sequentially — verify OS returns to shell after each.
5. (Multitasking) Run two programs simultaneously — verify both produce correct output.
6. Kill a misbehaving program — verify OS reclaims resources and continues.
7. Power-cycle during a file write — verify file system recovery.

**Stress test**: Run for 24+ hours with continuous program loading, file creation/deletion, and I/O operations. Monitor for memory leaks (gradually decreasing free memory) and crashes.

## Variations and Alternatives

| OS Type | Complexity | When to Use |
|---------|-----------|-------------|
| Monitor/monitor program | Minimal (0.5-4 KB) | First step; adequate for running single programs |
| Batch OS | Low (4-16 KB) | Automatic job sequencing without interactive use |
| Single-user interactive OS | Medium (16-64 KB) | Shell, file system, one program at a time |
| Multi-user, multi-tasking OS | High (64-256 KB+) | Multiple concurrent users; requires memory protection |
| Real-time OS (RTOS) | Medium-High | Deterministic response times for control systems |
| Embedded OS (no disk) | Low | ROM-based, runs from fixed memory |

## See Also

- [Assemblers, Linkers & Loaders](assemblers.md) — The toolchain for building OS kernels
- [Compiler Construction](compilers.md) — For writing the OS in a high-level language
- [Data Storage](../computing/data-storage.md) — Physical storage media that the file system manages
- [Electronic Computing](../computing/electronic.md) — Hardware architecture: interrupts, timers, I/O controllers
- [Development Tools](dev-tools.md) — Debuggers essential for OS kernel debugging


[← Back to Software Bootstrapping](index.md)
