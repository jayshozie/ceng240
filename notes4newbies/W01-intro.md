MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

You'll notice some concepts in this file are explained in two ways. This is
because, in my opinion, the CENG240 approach these topics often lacks the depth
needed to build a strong foundational understanding of computers. I've provided
additional detail to help bridge that gap.

# Computers

## What is a computer?

A computer is an electronic object that can do some sort of calculation. This
may sound like a calculator, but guess what? The very thing you're reading this
on is an extremely overpowered calculator, and it can only do addition. If you
would like to learn even deeper stuff like how does a computer do subtraction
with addition, visit my
[cs-studies](https://github.com/jayshozie/cs-studies) repository. Generally,
Alan Turing is the accepted father of the computer. He's the inventor of the
Turing machine, which is a theoretical machine that manipulates a tape with
infinite 0s and 1s on it. This machine is a complete equivalent of the machine
you're reading this right now. It can do whatever a modern computer can,
because that is exactly what your machine is doing right now. Although more
complicated, every modern computer is a Turing machine on steroids.

-------------------------------------------------------------------------------

## Components of a Computer

There are multiple crucial components of a computer, namely the motherboard,
power supply unit (PSU) central-processing unit (CPU), memory (a.k.a.
random-access memory, RAM), graphics processing unit (GPU), storage devices,
and peripherals.

Before diving into the components, you need to learn how a computer works. We
will start with the CPU, then get to the bigger picture.

### The von Neumann (Princeton) Architecture

This is the blueprint of the great-great grandpa of your computer. It has 2
parts: the CPU and the memory. The main difference between the Princeton
architecture and the Harvard architecture is that in the Princeton architecture
both the instructions and the values are stored in the same memory. In Harvard
architecture, however, there are 2 separate memories, where one holds the
instructions and the other holds the values that are needed on runtime.

The von Neumann architecture has these components:

- A processing unit with both an arithmetic logic unit and processor registers
- A control unit that includes an instruction register and a program counter
- Memory that stores data and instructions
- External mass storage
- Input and output mechanisms
[Von Neumann architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture)

#### Central-Processing Unit (CPU)

The central-processing unit, or abbreviated as CPU, is the brain of the
computer. It's the component that handles all of the computation. It starts as
soon as you start your computer and it executes instruction after instruction.
Modern computers are way more complex than what von Neumann designed, but the
idea stays the same. It is composed of multiple parts. The arithmetic logic
unit, and processor registers are located here.

##### Register & Cache

These are spots on a CPU that hold some values. The reason why these exist and
why the CPU doesn't just store them in the memory is the speed difference. In
modern computers there are 4 ways we can store data (from fastest to slowest):
registers, cache, RAMs, HDDs. If you read this from last to first now you have
the list from highest storage to lowest. Assigning a separate speed to
registers is a bit misleading, as they operate at the native speed of the CPU's
clock cycles, being integral to its calculations.

Registers are the fastest way CPU accesses data, because it is the CPU itself.
It takes 1 clock cycle, because at every clock cycle register values change.

Cache is the second fastest way a CPU can access to data. They are placed right
at the die itself, where die is the silicon die of the CPU (for further
reading:
[Die (integrated circuit)](https://en.wikipedia.org/wiki/Die_(integrated_circuit)).
CPU waits about 2-100 cycles for a data stored on the cache. 

The next in the speed comparison list is the RAM, if the CPU needs a data from
the RAM it can take up to 1000 cycles.

The slowest storage in our list are HDDs (hard disk drives). It can take up to
100.000.000 cycles for the CPU to acquire a data located on a HDD.

These clock speeds may be a little misleading, though. Your machine probably
has a CPU that has a clock speed way above 1.0GHz. 1.0GHz mean that every
single second your CPU's clock ticks more than a billion times.

Now that we understand how unbelievably fast these machines are, let's get to
how they do arithmetical and logical calculations.

##### Arithmetic-Logic Unit (ALU)

This is the part of the CPU that handles all of arithmetic and logical
calculations. This is the place where 1+1 equals 10. A weird world, surely.
ALU has a lot of electrical logic gates (e.g.: AND, OR), which are connected to
perform computations and process instructions.

P.S.: 10 is the binary representation of the decimal number 2.

#### Control Unit

This is the part of the CPU that handles the reading and writing values to the
memory part. It has an instruction register, which holds the memory address of
the current instruction being executed and the program counter (PC) which holds
the memory address of the next instruction to be fetched.

#### Random Access Memory (RAM)

Random Access Memory (RAM), often simply referred to as memory, is a long list
of values and instructions stored in addresses. Addresses may look a bit scary
(e.g.: 11000011 (binary), 0xC3 (hexadecimal), ebx (Assembly)), but you don't
need to worry about them too much, Python handles all of that.

#### External Mass Storage

This is your computer's actual storage. It can be more than terabytes (TB) of
data in modern day computers. There are multiple types of it, but the two types
you should know are HDDs (hard disk drives) and SSDs.

##### Hard Disk Drives (HDDs)

A hard disk is a sealed unit containing a number of platters (magnetic storage
devices that are similar in looks and principle to optic storage devices like
CDs and DVDs) in a stack. These are electro-mechanical data storage devices.
Electromagnetic read/write heads are positioned above and below each platter.
As the platters spin, the drive heads move in toward the center surface and out
toward the edge. In this way, the drive heads can reach the entire surface of
each platter.

[Hard disk drive](https://en.wikipedia.org/wiki/Hard_disk_drive)
[Hard Disk Drive Basics](https://ntfs.com/hard-disk-basics.htm)

##### Solid State Drives (SSDs)

A solid-state drive (SSD) is a type of solid-state storage device that uses
integrated circuits to store data persistently
[Solid-state drive](https://en.wikipedia.org/wiki/Solid-state_drive). This is
a bit of a technical definition, I think the best way to understand is to
compare them to RAMs and HDDs. Unlike HDDs, SSDs have no moving parts which
allows them to be way faster than a traditional HDD. Instead of storing data
magnetically, they store data in semiconductor components.

Putting the actual architecture aside, if they ask you what are the components
of the von Neumann architecture, say the CPU and the memory.

<details>
    <summary>Fetch-Decode-Execute Cycle</summary>

#### Fetch-Decode-Execute (Fetch-Execute) Cycle

In the von Neumann architecture, he explained how a "cycle" should be like.
There are 3 main stages at every cycle of the CPU: fetch, decode, execute.

There are some extra registers that you don't have to know, but I'll give you
what they are and what they do so that you can understand the process better.

###### Memory Address Register (MAR)
A memory address register is the CPU register that either stores the memory
address from which data will be fetched to the CPU registers, or the address to
which data will be sent and stored via system bus.

###### Memory Data Register (MDR)
A memory data register, a.k.a. memory buffer register (MBR), is the register in
a computer's CPU that stores the data being transferred to and from the
immediate access storage.

###### Current Instruction Register (CIR)
A current instruction register, a.k.a. instruction register (IR), is the part
of a CPU's control unit that holds the instruction currently being executed or
decoded. In simple processors, each instruction to be executed is loaded into
the instruction register, which holds it while it is decoded, prepared, and
ultimately executed, which can take several steps.

##### Fetch

Everything starts with fetching information from somewhere.

1. Address in program counter (PC) is copied to memory address register (MAR).
2. PC incremented to "point" to the next instruction.
3. Instruction found at the address described by MAR copied to the memory data
register (MDR).
4. Instruction in MDR, is copied to the current instruction register (CIR).

##### Decode

Now that we have an instruction, we need to decode it so that we know what to
do. In the decode stage, the control unit (CU) decodes the contents of the CIR.
That's the only thing happening in the decode stage.

##### Execute

We know what to do, let's do it. Control unit (CU) sends signals to relevant
components (e.g. ALU). Whatever that instruction asks the CPU to do, it happens
right here.

What happens after that? Go back to the fetch stage and do it a couple billion
times a second and you have a modern day CPU.

For a more in-depth explanation you can check
[Instruction cycle](https://en.wikipedia.org/wiki/Instruction_cycle)

#### A Slightly Detailed Explanation of Fetch-Decode-Execute Cycle

The most complex stage in the fetch-decode-execute cycle is the fetch stage;
however, it's still simple enough if you think it through.

First we need to find where the instruction is located, that's stored in the
program counter (PC). We copy that address to the memory address register
(MAR), because we need to empty the program counter at some point.

Now the value stored in the PC needs to be changed, so that we know which
instruction to execute next, since that's the reason PC exists in the first
place.

Now, we find the address described by the MAR in the memory, and copy that
instruction into memory data register (MDR), so we know what to do.

Then the instruction from the MDR is copied to the current instruction
register (CIR, a.k.a. instruction register (IR)) for decoding and execution.

The Control Unit then begins to decode the instructions in the CIr,
interpreting the thing we're going to do.

After the decode, CU sends signals to relevant components in the CPU such as
the ALU.

Your cycle is finished, now do it again. If you read it one more time you'll
see how this self-corrects the registers and you can continue doing the same
thing indefinitely.
</details>

-------------------------------------------------------------------------------

<details>
    <summary>Some Proprietary Stuff</summary>

#### Instructions

Instructions are how the user interacts with the CPU. They are the fundamental
commands that software (programs) uses to interact with the CPU. Here is an
example: (This is not how we actually write code, well, there are some people
who have to code like this, but that's not what we're going to do.)

##### Machine Code (Binary)
100000111100001100001010
(10000011 11000011 00001010 for easier reading)
##### Machine Code (Hexadecimal)
0x83 0xC3 0x0A
##### Assembly (x86_64)
add ebx, 10

All of these mean exactly the same thing, add the value 10 to the ebx register.

</details>

<details>
    <summary>Other Components</summary>

Now that we know how a computer works at the very deep, we need to learn some
other components that helps us using a computer.

First of all, all input-output devices are connected to the CPU via a wiring
system called bus. Most simply put, buses are metallic cables that connect
everything to each other. Subtopics are listed in order of importance.

### Input Devices

#### Keyboard

A [computer keyboard](https://en.wikipedia.org/wiki/Computer_keyboard) is a
built-in or peripheral input device modeled after the typewriter keyboard.

It's the thing that is right in front of you. The one with the keys on it, with
letters and numbers on them.

#### Mouse

A [computer mouse](https://en.wikipedia.org/wiki/Computer_mouse) (plural mice;
rarely also mouses) is a hand-held pointing device that detects two-dimensional
motion relative to a surface. This motion is typically translated into the
motion of the pointer (called a cursor) on a display, which allows a smooth
control of the graphical user interface (GUI) of a computer.

It's the thing in your hand, or the surface you're touching to move the cursor.
The second is called a touchpad, not a mouse, same idea different device.

#### Microphone

A [microphone](https://en.wikipedia.org/wiki/Microphone), colloquially called a
mic, or mike, is a transducer that converts sound into an electrical signal.

It's the thing you're talking into when you're talking with someone over your
phone, through the microphone of your headset, or through the computer itself.

### Output Devices

#### Monitor

A [computer monitor](https://en.wikipedia.org/wiki/Computer_monitor) is an
output device that displays information in pictorial or textual form. A
discrete monitor comprises a visual display, support electronics, power supply,
housing, electrical connectors, and external user controls.

It's the thing that you're reading this from.

#### Speakers

A [loudspeaker](https://en.wikipedia.org/wiki/Loudspeaker) (commonly referred
to as a speaker, or more fully, a speaker system) is a combination of one or
more speaker drivers, an enclosure, and electrical connections (possible
including a crossover network). The speaker driver is an electroacoustic
transducer that converts an electrical audio signal into a corresponding sound.

A [computer speaker](https://en.wikipedia.org/wiki/Computer_speaker) are
speakers marketed for use with computers, although usually capable of other
audio uses, e.g. for a shelf stereo or television.

It's the thing that makes the computer go beep.

#### Headphones

[Headphones](https://en.wikipedia.org/wiki/Headphones) are a pair of small
loudspeaker drives worn on or around the head over a user's ears. They are
electroacoustic transducers, which convert an electrical signal to a
corresponding sound.

It's the thing that you put in/on to your ears.

### Input/Output Devices

#### Storage Device

We've talked about these in a previous section, but let us go through them one
more time.

A [storage device](https://en.wikipedia.org/wiki/Computer_data_storage), a.k.a.
computer data storage or digital data storage, is a technology consisting of
computer components and recording media that are used to retain digital data.
</details>

-------------------------------------------------------------------------------

## How does a computer start?

There are multiple steps of instructions happening when you press the on/off
button of your computer. I'll give you what the CENG240 wants you to know, but
also give you a more in-depth look at a system power-up for the ones who want
to know more.

<details>
    <summary>CENG240 Way</summary>

### BIOS (Basic Input-Output System) is loaded.

Before BIOS is loaded, the computer needs a Power Good signal from the
power supply unit (PSU), which ensures the rest of the system that the
electricity connected to is stable. After that signal the motherboard starts
the CPU, and tests its very basic capabilities. These tests include very basic
functionality like basic arithmetic. The CPU then begins executing instructions
from the BIOS firmware directly from the ROM chip on the motherboard. BIOS takes
control of the system for the time being.

### POST (Power-On Self-Test) is performed.

BIOS initiates a proprietary test called Power-On Self-Test (POST) to be
sure that everything works as intended. This tests everything from the
the CPU itself to peripherals. The most important checks are as follows:

1. More In-Depth Test of the CPU
2. Detailed Test of RAM

### BIOS Searches for an operating system to load.

If the POST is successful, then the BIOS searches the storage devices, such
as HDDs and SSDs, for bootable operating systems. If it finds a bootable
OS, then it tries to find its Master Boot Record (MBR) and loads it into
the system memory.

Master Boot Record (MBR) of a disk contains a table and code piece for
loading the OS on that disk. The MBR contains a small executable program
(bootstrap code) and a partition table that points to an active partition. If a
disk has multiple bootable operating systems, a more advanced bootloader (often
residing in the Volume Boot Record of a partition) is used ot manage selection.

### MBR is Executed to load the OS.

BIOS executes MBR, and gives control of the system to
it. MBR then tries to find the rest of the OS, and if it does it loads it
into the system memory and gives control of the system to the OS.

### BIOS and MBR are extended by

- Unified Extensible Firmware Interface (UEFI)
- GPT (GUID Partition Table)

Note: UEFI and GPT represent modern advancements over the traditional BIOS/MBR
system, offering enhanced boot capabilities and disk partitioning schemes.
For a more detailed explanation, refer to the More Detailed Way section.

</details>

<details>
    <summary>More Detailed Way</summary>

### Power Applied/Power Good Signal

- When the power button is pressed, the Power Supply Unit (PSU), which is the
block where you connect to the outlet and to your computer, delivers power to
the motherboard and components.
- Once stable power is available, the PSU sends a "Power Good" signal to the
motherboard this signal prevents the CPU from starting prematurely with
unstable power.

### CPU Initialization and Reset Vector

- Upon receiving the Power Good signal, the CPU is released from its reset
state.
- The CPU's internal registers are set to predefined initial values. Crucially,
the program counter (PC) is loaded with specific memory addresses, known as the
"reset vector" (typically FFFF0h for older BIOS, or different address for
UEFI). This address points to the start of the Basic Input/Output System (BIOS)
or Unified Extensible Firmware Interface (UEFI) firmware.

### BIOS/UEFI Firmware Loading and Execution

- The CPU begins executing instructions from the address pointed to by the
reset vector. These instructions reside in a non-volatile memory chip on the
motherboard (ROM, EEPROM, or Flash memory), which stores the BIOS or UEFI
firmware.
- Early Firmware Initialization: The firmware performs the setup of the CPU and
memory controller, allowing access to the main system RAM.

### Power-On Self-Test (POST)

- The firmware initiates the POST process to check the integrity and presence
of essential hardware components.
- CPU Test: Verifies basic CPU functionality.
- RAM Test: Performs a quick check of the main system memory (RAM). Failures
here often result in beep codes.
- Video Card Initialization: Detects and initializes the graphics adapter. If
successful, a display is initialized.
- Keyboard Controller Test: Checks the keyboard and mouse interface.
- Peripheral Device Detection: Detcets and initializes other crucial components
like hard drives, solid-state drives, optical drives, and USB controllers
connected to the motherboard.
- BIOS/UEFI Self-Test: Checks the integrity of the firmware itself.
- Error Reporting: If any critical errors are detected during POST, the system
typcilaly halts and reports the error via beep codes, error messages on the
screen, or diagnostic LEDs.

### BIOS/UEFI Configuration Loading and Hardware Environment Setup

- If POST is successful, the firmware loads its configuration settings (stored
in NVRAM or CMOS memory, powered by a small battery).
- It continues to initialize peripheral devices and controllers not covered in
the basic POST.
- It enumerates and configures hardware resources (I/O addresses, IRQs, DMA
channels) for all selected devices.

### Boot Device Selection

- The BIOS/UEFI uses its configured boot order (e.g., CD/DVD, USB, Hard Drive,
Network) to find a bootable device.
- It reads the Master Boot Record (MBR) from the selected traditional hard
drive or the EFI System Partition (ESP) from a UEFI-enabled drive.

### Bootloader Execution (Stage 1 & 2)

- MBR Boot (Legacy BIOS)
    - The firmware loads the first sector of the boot device (the MBR) into
    RAM.
    - The MBR contains a small piece of code (Stage 1 bootloader) and the
    partition table.
    - The Stage 1 bootloader executes, its primary job being to find and load
    the next stage of the bootloader. It typically scans the partition table
    for an active/bootable partition.
    -It then loads the Volume Boot Record (VBR) or a specific bootloadr from
    the active partition. This is often the Stage 2 bootloader (e.g., GRUB for
    Linux, BOOTMGR for Windows).

- UEFI Boot:
    - The UEFI firmware directly reads the EFI System Partition (ESP), which
    contains EFI applications (bootloaders).
    - It executed the EFI boot application specified in the UEFI boot entry
    (e.g., `bootmgfw.efi` for Windows, `grubx64.efi` for GRUB/Linux).
    - UEFI bootloaders can be more sophisticated and directly load the kernel.

### Operating System Kernel Loading

- The Stage 2 bootloader (e.g., GRUB, Windows Boot Manager (BOOTMGR)) takes
over.
- It may present a boot menu to the user (e.g., allowing selection of different
operating systems or kernel versions).
- Upon selection (or timeout), the bootloader's main task is to load the 
Operating System (OS) kernel into RAM.
- For Linux, this typically involves loading the kernel image and an initial
RAM disk (initramfs/initrd). For Windows, it loads `ntoskrnl.exe` and other
core system files.
- If the kernel is compressed, the bootloader or a small stub within the kernel
itself will decompress it into memory.

### Kernel Initialization (Kernel Space)

- Once loaded, the OS kernel gains control.
- it initializes its own internal structures (e.g., memory management units,
virtual memory tables).
- It sets up interrupt handlers, and the process scheduler.
- The kernel then begins to probe and initialize the vast majority of the
system's hardware components and their respective device drivers. This involves
allocating resources (memory, I/O ports) for them.
- It mounts the root filesystem (the primary file system where the OS files
reside). If an `initramfs`/`initrd` was loaded, it might perform temporary
tasks and then switch to the real root filesystem.

### Operating System Initialization (Userspace - Init System)

- After the kernel has initialized sufficiently it starts the very first
user-space process, traditionally known as `init` (with Process ID 1, PID 1).
Modern Linux systems often use `systemd`, while older ones used `SysVinit` or
`Upstart`. Windows has its own equivalent system.
- The `init` system reads its configuration files to determine which services
and processes need to be started.
- It mounts other necessary filesystems (e.g., `/home`, `/var`, `/tmp`,
`/proc`, `/sys`).
- It starts essential system services and daemons (e.g., networking services,
logging daemons, D-Bus, cron, security services).
- It may run various startup scripts (`rc.local` on some Linux systems, startup
scripts for installed applications).

### User Environment Loading

- Once core system services are running, the init system starts the display
manager or login manager (e.g., GDM, LightDM, SDDM on Linux; Winlogon on
Windows).
- This component presents the graphical login screen or a command-line prompt.
- Upon successful user authentication, the system loads the user's specific
environment, which includes:
    - Loading user profiles and settings.
    - Starting the chosen desktop environment (e.g., GNOME, KDE, XFCE on Linux;
    Windows Explorer on Windows).
    - Launching any applications configured to start automatically at login.

This is way more than what you need to pass this course, but I believe seeing
how many things happen in about 3-10 seconds when you turn-on your computer
makes everything that much more impressive, and I believe this has the
capability to actually change some students' minds about CS as a career.
</details>

-------------------------------------------------------------------------------

## Operating Systems (OSs)

### What is an operating system (OS)?

An operating system (OS) serves as the fundamental layer of software that
manages computer hardware and software resources, providing common services for
computer programs. It acts as an intermediary between the hardware and the
applications, abstracting the complexities of the underlying hardware and
presenting a consistent, high-level interface to application software and
users. Its primary objectives include managing system resources, facilitating
program execution, ensuring system security, and providing a stable environment
for all operations.

<details>
    <summary>CENG240 Way</summary>

The operating system (OS) has a number of responsibilities:

- Memory Management
- Process Management
- Device Management
- File Management
- Security
- User Interface

Note: That's literally the only information about an operating system in the
official slides. If you want to learn how an operating system works, please
check the More Detailed Way dropdown.
</details>

<details>
    <summary>More Detailed Way</summary>

### The Kernel

The kernel is the core of the operating system, resident in memory. It holds
complete control over everything in the system and operates in a special
protected mode (kernel mode or supervisor mode), granting it direct access to
all hardware resources. Its primary responsibilities are;

1. **Process Management**

    - **Process Scheduling:** Manages the allocation of CPU time to various
    processes. This involves complex algorithms (e.g., First-Come, First-Served
    (FCFS), Shortest Job First (SJF), Priority Scheduling, Round Robin,
    Multilevel Feedback Queue) to determine which process runs at what time,
    aiming to optimize system throughput, turnaround time, waiting time, and
    response time.

    - **Process Control Block (PCB):** For each process, the kernel maintains a
    data structure called a PCB, which stores crucial information such as
    process state (running, waiting, ready), program counter, CPU registers,
    memory management information, I/O status information, and accounting
    information.

    - **Context Switching:** The mechanism by which the CPU saves the state of
    the current process and loads the savved state of another process, allowing
    multiple process to share the CPU.

    - **Inter-Process Communication (IPC):** Provides mechanisms (e.g., pipes,
    message queues, shared memory, semaphores, mutexes) for processes to
    communicate and synchronize their activities, preventing race conditions
    and deadlocks.

    - **Threads:** Supports the creation and management of threads, which are
    lightweight units of execution within a process, allowing for concurrent
    execution within a single program.

2. **Memory Management**

    - **Virtual Memory:** A technique that allows processos to use more memory
    than physically available. It provides an illusion of a large, contiguous
    address space by mapping virtual addresses to physical addresses, primarily
    using disk space as an extension of RAM.
        - **Paging:** Divides memory into fixed-size blocks called "pages" (for
        virtual memory) and "frames" (for physical memory). This allows
        non-contiguous allocation of memory to processes.
        - **Segmentation:** Divides memory into variable-sized logical units
        called "segments", which correspond to logical divisions of a program
        *e.g., code, data, stack).
        - **Swapping:** The process of temporarily moving a process (or parts
        of it) from main memory to secondary storage (swap space on disk) and
        back to allow more processes to run than can fit in physical memory.

    - **Memory Allocation/Deallocation:** Manages the allocation and
    deallocation of memory spacee to processes and applications dynamically.

    - **Memory Protection:** Implements mechanisms *e.g., base and limit
    registers, segmentation, paging) to ensure that processes cannot access
    memory regions belonging to other processes or the OS itself, maintaining
    system stability and security.

3. **Storage Management (File System Management)**

    - **File System:** Organizes data on stareg devices (hard drives, SSDs, USB
    drives) into files and directories (folders for Windows users). It provides
    a logical vie of data storage, abstracting the physical block-level
    storage.

    - **File Allocation Methods:** Determines how files are stored on disk
    (e.g., contiguous allocation, linked allocation, indexed allocation).

    - **Directory Structure:** Manages the hierarchical organization of files,
    allowing for easy navigation and management (e.g., tree-structured
    directories).

    - **Disk Scheduling:** Optimizes the movement of the disk's read/write
    heads (on hard disk drives) to reduce seek time and improve I/O performance
    (e.g., FCFS, SSTF, SCAN, C-SCAN).

    - **Data Buffering and Caching:** Uses main memory as a buffer and cache
    for disk I/O operations to improve performance by reducing the number of
    direct disk accesses.

4. **Device Management (I/O Management)**

    - **Device Drivers:** Specialized software modules that act as
    intermediaries between the operating system's kernel and specific hardware
    devices (e.g., printers, network cards, graphics cards, USB devices). They
    translate OS requests into hardware-specific commands and handle hardware
    interurpts.

    - **I/O Control:** Manages input and output operations to and from devices,
    ensuring efficient and error-free data transfer.

    - **Buffering and Spooling:** Uses memory buffers to temporarily hold data
    during I/O operations. Spooling (Simultaneous Peripheral Operations
    On-Line) is a technique for buffering data for slower devices like
    printers, allowing the CPU to proceed with other tasks.

5. **Security and Protection**

    - **Authentication and Authorization:** Verifies user identities
    (authentication) and determines what resources users or processes are
    allowed to access (authorization) through mechanisms like passwords,
    biometric data, and access control lists (ACLs).

    - **Privilege Levels:** Enforces distinct modes of operation (kernel mode
    for the OS, user mode for applications) to protect critical system
    resources from unauthorized access or malicious processes.

    - **System Calls (syscalls):** Provides a controlled interface for
    user-mode programs to request services from the kernel, ensuring that all
    interactions with hardware or protected resources are mediated and
    validated by the OS.

6. **Networking**

    - **Network Stack:** Implements the various layers of networking protocls
    (e.g., TCP/IP stack), allowing the computer to communicate over networks.

    - **Socket Interface:** Provides a programming interface (API) for
    applications to establish network connections and send/receive data.

### The Shell (User Interface)

This component provides the means for users to interact with the operating
system, acting as a bridge between the human and the machine. It has two main
parts.

1. **Command Line Interface (CLI)**

    - **Command Interpreter (Shell):** A text-based interface where users type
    commands. The interpreter parses these commands and sends them to the
    kernel for execution. Examples include Bash (Linux/macOS), PowerShell
    (Windows), and Command Prompt (Windows).
    - **Shell Scripts:** Allows users to automate sequences of commands by
    writing them into a script file, providing powerful capabilities for system
    administration and task automation.

2. **Graphical User Interface (GUI)**

    - **Windowing System:** Manages the display of multiple application windows
    on the screen, handling their creation, resizing, movement, and drawing.

    - **Desktop Enviornment:** Provides a comprehensive visual metaphor for
    user interaction, complete with icons, menus, panels, widgets, and a
    background. Popular examples include GNOME, KDE, and XFCE for Linux, the
    Windows Desktop; and macOS Aqua.

    - **Event Handling:** Processes user input from pointing devices (mouse,
    touchpad) and keyboards, translating physical actions into system events
    that applications can respond to.

### System Utilities and Application Programming Interfaces (APIs)

These components extend the functionality of the OS, providing tools for
maintenance, configuration, and management tasks. It has two main branches:
system utilities and application programming interfaces (APIs).

System utilities are standalone programs that perform routine system
maintenance, configuration, and management tasks. APIs are crucial for software
development, providing a standardized bridge for applications to request OS
services.

1. **System Utilities**

    - **Maintenance Tools:** Examples include disk defragmenters/optimizers,
    backup utilities, system monitors (for CPU, memory, network usage), and
    task managers.

    - **Configuration Tools:** Utilities for managing network settings, user
    accounts, hardware configurrations, and installing/removing software (e.g.,
    package managers on Linux).

2. **Application Programming Interfaces (APIs)

    - **System Call Interface:** A set of defined routines and protocols that
    allow applications to request services from the kernel (e.g.,
    reading/writing files, creating new processes, network communication,
    memory allocation). This abstraction layer frees developers from needing to
    know the low-level hardware specifics.

    - **Libraries:** Collections of pre-written code (functions, routines) that
    applications can use to perform common tasks. These libraries simplify
    application development, ensure consistency, and often sit on top of the
    system call interface.
</details>

# Reading Recommendations from the Official Lecture Slides

- History of Computing:
    - <https://www.computersciencelab.com/ComputerHistory/History.htm>
    - <https://www.youtube.com/playlist?list=PL1331A4548513EA81>
