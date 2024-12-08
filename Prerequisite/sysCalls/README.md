# system calls are same as interrupt / trap calls
system call is basically entry to kernel mode.

how system calls are executed -:
    printf("hello") : since printf is a system call (we need kernel to print on
    the monitor : this gets stored in a register {special register called rax})
    there is a table of numbers and system_call_function
    1 : address of printf
    2 : address of scanf
    3 : address of fork

    mov rax 1
    then it'll go to address of printf (where printf wrapper function is
    actually written (it's called write() in assembly))
    this write() is the actual write which handles IO operations.
    now what about arguments? (like printf("hello")) how to know what to print?
    for this there are other registers/stack to store all the args..

    move rax 1
    move R1 "hello" # similarily for other arguments we store it in a stack
    sys_call # this tells computer to switch to kernel mode (mode 0) and
    implement (look for 1 in the lookup table : find printf : go to that address
    of actual printf (write() function) and then using R1 register/stack of
    arguments, print it on the screen (how? -:)
	actual function puts the real output in another register and then user reads
	that register : hello

table = system call table (same as interrupt service in COA) pauses the current
execution and runs on kernel mode and then returns back to user mode once done.
this is how an actual printf or system call function works

how fork works, how exec works we've already seen with code.

-- High Level --

~CPU will pause the curretn execution (after syscall written in user mode)
~Save the registers value
~Switch the mode
~Load RAX value and got o system call table (Interrupt Vector Table)
~Find the address of kernel code (Interrupt Service Routine)
~If Kernel function requires arguments then check stack/specific location of
arguments (like in printf(**args))
~Execute the interrupt service routine (kernel code)
~Placing the return value in some register / location
~Switch mode bit from 0 to 1 (reti command basically how a subroutine works)

As you can tell, system calls are very slow. Function calls are much faster (no
transfer to kernel and no overheads)
-----------
Threads : lightweight process, great invention

Why not create different processes all the time?
~ Context Switching takes time
~ Different address space
~ Interprocess communication is required (big headache)

Threads are so cool cuz they support concurrency (single core) and parallelism (multiple core CPUs)

Memory management is the core of OS

Every transition in process states is a system call. If interrupt / syscall
occurs in c code, it goes to the assembly code function of scheduler which
handles the scheduler (more on this when scheduling algorithms come)

Need to write my own scheduler, libraries are there.

User Level Threads
Disadvantages -:
    Not visible to kernel hence OS can't make decisions about scheduling.
    OS doesn't know about user level threads so if one thread gets blocked, all
    does
Advantages -:
    Fast to create (no sys call needed)
    No Context Switch (Kernel doesn't have to maintain different states)

# How Scheduler Works
Every process has some info to store -> PCB, Registers in use etc  ... Where do
we store this information ? in memory (privileged area of memory : kernel stack)
in user mode : p1 is running, p1 timer is over, p1 wants to leave cpu by choice
: bcs of this P1 will be in kernel mode (system call will be made) : context of
p1 saved in kernel mode and then you run the scheduler which decides what process should run now.
