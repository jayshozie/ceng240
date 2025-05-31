MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

Since they do ask these things as questions in the midterm and final exams, I
also will explain you what they mean. Sorry in advance.

# Computers

-------------------------------------------------------------------------------

## What is a computer?

A computer is an electronic object that can do some sort of calculation. This
may sound like a calculator, but guess what? The very thing you're reading this
on is an extremely over-powered calculator, and it can only do addition. If you
would like to learn even more deeper stuff like how does a computer do
subtraction with addition, visit my
[cs-studies](https://github.com/jayshozie/cs-studies) repository. Generally,
Alan Turing is the accepted father of the computer. He's the inventor of the
Turing machine, which is a theoretical machine that manipulates a tape with
infinite 0s and 1s on it. This machine is a complete equivalent of the machine
you're reading this right now. It can do whatever a modern computer can,
because that is exactly what your machine is doing right now. Even though more
complicated, every modern computer is a Turing machine on steroids.

-------------------------------------------------------------------------------

## Components of a Computer

There are multiple cruical components of a computer, namely the CPU, RAM, and
storage.

### The von Neumann (Princeton) Architecture

This is the blueprint of the great-great grandpa of your computer. It has 2
parts: the CPU and the memory. The main difference between the Princeton
architecture and the Harvard architecture is that in the Princeton architecture
both the instructions and the value are stored in the same memory. In Harvard
architecture, however, there are 2 separate memories, where one holds the
instructions and the other holds the values that are needed on runtime.

The von Neumann architecture have these components:

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
idea stays the same. It itself has multiple parts. The arithmetic logic unit,
and processor registers are located here.

##### Register & Cache

These are spots on a CPU that holds some values. The reason why these exist
and why the CPU doesn't just store them in the memory is the speed difference.
In modern computers there are 4 ways we can store data (from fastest to
slowest): registers, cache, RAMs, HDDs. If you read this from last to
first now you have the list from highest storage to lowest. Actually, assigning
speed to registers is a bit of misleading, because since that's where the CPU
is doing its calculations, its speed is the speed of the CPU itself.

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

Now that we got how fricking fast these machines are, let's get to how they do
arithmetic and logic.

##### Arithmetic-Logic Unit (ALU)

This is the part of the CPU that handles all of arithmetic and logical
calculations. This is the place where 1+1 equals 10. A weird world, surely.
ALU has a lot of electrical logic gates (e.g.: AND, OR), which is connected so
that it can do computations and process instructions.

P.S.: 10 is the binary representation of the decimal number 2.

#### Control Unit

This is the part of the CPU that handles the
reading-and-writing-values-to-the-memory-part. It has an instruction register,
which holds the memory address of the current instruction being executed and
the program counter (PC) which holds the memory address of the next instruction
to be fetched.

#### Random Access Memory (RAM)

Memory (or its more modern name, RAM) is a long list of values and instructions
stored in addresses. Addresses may look a bit scary (e.g.: 11000011 (binary),
0xC3 (hexadecimal), ebx (Assembly)), but you don't need to worry about them too
much, Python handles all of that.

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

A solid-state drive (SSD) is a type of solid-state storage device that use
integrated circuits to store data persistently
[Solid-state drive](https://en.wikipedia.org/wiki/Solid-state_drive). This is
a bit of a technical definition, I think the best way to understand is to
compare them to RAMs and HDDs. Unlike HDDs, SSDs have no moving parts which
allows them to be way faster than a traditional HDD. Instead of storing data
magnetically, they store data in semiconductor components.

Putting the actual architecture aside, if they ask you what are the components
of the von Neumann architecture, say the CPU and the memory.

-------------------------------------------------------------------------------

#### Instructions

Instructions are how the user interacts with the CPU. Here is an example:
(This is not how we actually, well, there are some people who has to code like
this, but that's not what we're going to do.)

##### Machine Code (Binary)
100000111100001100001010
(10000011 11000011 00001010 for easier reading)
##### Machine Code (Hexadecimal)
0x83 0xC3 0x0A
##### Assembly (x86_64)
add ebx, 10

All of these mean exactly the same thing, add the value 10 to the ebx memory
location.

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

1. Address in program counter (PC) is copies to memory address register (MAR).
2. PC incremented to "point" to the next instruction.
3. Instruction found at address described by MAR copied to the memory data
    register (MDR).
4. Instruction in MDR, copied to the current instruction register (CIR).

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

Now we need to to change the value stored in the PC, so that we know which
instruction to execute next, since that's the reason PC exists in the first
place.

Now, we find the address described by the MAR in the memory, and copy that
instruction into memory data register (MDR), so we know what to do.

Then we copy that to the current instruction register (CIR) so we can decode
and execute it.

Now, the control unit starts to decode the instruction located in CIR, so that
we understand the thing we're going to do.

After the decode, CU sends signals to relevant components in the CPU such as
the ALU.

Your cycle is finished, now do it again. If you read it one more time you'll
see how this self-corrects the registers and you can continue doing the same
thing indefinitely.

-------------------------------------------------------------------------------

### How does a computer start?

There are multiple steps of instructions happening when you press the on/off
button of your computer. I'll give you what the CENG240 wants you to know, but
also give you a more in-depth look at a system power-up for the ones who want
to know more.

<details>
    <summary>CENG240 Way</summary>

##### BIOS (Basic Input-Output System) is loaded.
##### POST (Power-On Self Test) is performed.
##### BIOS Searches for an operating system to load.
##### MBR is Executed to load the OS.
##### BIOS and MBR are extended by
<details>

<details>
    <summary>More Detailed Way</summary>

##### Power Applied/Power Good Signal

- When the power button is pressed, the Power Supply Unit (PSU), which is the
block where you connect to the outlet and to your computer, delivers power to
the motherboard and components.
- Once stable power is available, the PSU sends a "Power Good" signal to the
motherboard this signal prevents the CPU from starting prematurely with
unstable power.

##### CPU Initialization and Reset Vector

- Upon receiving the Power Good signal, the CPU is released from its reset
state.
- The CPU's internal registers are set to predefined initial values. Crucially,
the program counter (PC) is loaded with specific memory addresses, known as the
"reset vector" (typically FFFF0h for older BIOS, or different address for
UEFI). This address points to the start of the Basic Input/Output System (BIOS)
or Unified Extensible Firmware Interface (UEFI) firmware.

##### BIOS/UEFI Firmware Loading and Execution

- The CPU begins executing instructions from the address pointed to by the
reset vector. These instructions reside in a non-volatile memory chip on the
motherboard (ROM, EEPROM, or Flash memory), which stores the BIOS or UEFI
firmware.
- Early Firmware Initialization: The firmware performs the setup of the CPU and
memory controller, allowing access to the main system RAM.

##### Power-On Self-Test (POST)

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

##### BIOS/UEFI Configuration Loading and Hardware Environment Setup

- If POSt is successful, the firmware loads its configuration settings (stored
in NVRAM or CMOS memory, powered by a small battery).
- It continues to initialize peripheral devices and controllers not covered in
the basic POST.
- It enumerates and configures hardware resources (I/O addresses, IRQs, DMA
channels) for all selected devices.

##### Boot Device Selection

- The BIOS/UEFI uses its configured boot order (e.g., CD/DVD, USB, Hard Drive,
Network) to find a bootable device.
- It reads the Master Boot Record (MBR) from the selected traditional hard
drive or the EFI System Partition (ESP) from a UEFI-enabled drive.

##### Bootloader Execution (Stage 1 & 2)

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

##### Operating System Kernel Loading

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

##### Kernel Initialization (Kernel Space)

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

##### Operating System Initialization (Userspace - Init System)

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

##### User Environment Loading

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
capability to actually change some students' mind about CS.
</details>

### Other Components

Now that we know how a computer works at the very deep, we need to learn some
other components that helps us using a computer.

#### Input-Output Devices

First of all, all input-output devices are connected to the CPU via a wiring
system called bus. Most simply put, buses are metallic cables that connect
everything to each other.

##### Keyboard
##### Monitor
##### Speakers
##### Mouse
