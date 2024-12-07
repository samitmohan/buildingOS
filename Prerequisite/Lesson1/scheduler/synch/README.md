# Critical Section
The critical-section problem is to design a protocol that the processes can use to synchronize their
activity so as to cooperatively share data. Each process must request permission to enter its critical
section. The section of code implementing this request is the entry section. The critical section may
be followed by an exit section. The remaining code is the remainder section.

A solution to the critical-section problem must satisfy the following three requirements:

a) Mutual exclusion. If process Pi is executing in its critical section, then no other processes can be executing in their critical sections.

b) Progress. If no process is executing in its critical section and some processes wish to enter
their critical sections, then only those processes that are not executing in their remainder
sections can participate in deciding which will enter its critical section next, and this selection
cannot be postponed indefinitely (indefinitely = अनिश्‍चित).

With above two process we can ensure that there will be exactly one process in critical section.

c) Bounded waiting. There exists a bound, or limit, on the number of times that other processes
are allowed to enter their critical sections after a process has made a request to enter its
critical section and before that request is granted.


Q : How to check these three in questions ? –
Mutual Exclusion.
• One process in critical section, another process tries to enter → show that second process will
block in entry code
• Two (or more) processes are in the entry code → show that at most one will enter critical
section. Here at most is used meaning if deadlock happens when two process are in entry
code then ME will satisfy.
Progress (== absence of deadlock)
• No process in critical section, p1 arrives → p1 enters
• Two (or More) processes are in the entry code → show that at least one will enter critical
section.
Bounded waiting (== fairness)
• One process in critical section, another process is waiting to enter → show that if first process
exits the critical section and attempts to re-enter, show that first must not be able to get in.


Peterson’s solution and hardware solutions : (only works for 2 processes at max)

# pseudo code
```c++
int turn; // i might be ready but it's okay if you execute others
boolean interested[2]; // who's ready to enter it's CS
while (true) {
	interested[person1] = true; // person1 is interested to go in but it's person2's turn
	turn = person2;
	while (interested[person2] and turn == person2); // if person2 interested and his turn also : let him go
	// else let person 1 enter CS

	// person1 leaves critical section
	interested[person1] = false;
	// remainder section
}
```
Both processes can be ready to execute in it's CS so this will be handled by interested[2] but who's going to execute CS is decided by turn

Peterson’s solution is software-based solution and software-based solutions are not guaranteed to
work on modern computer architectures. As it is code and slow as compared to hardware. Peterson's
algorithm is a mutual exclusion algorithm that can be used on multiprocessor systems. It works by
using shared memory to coordinate the threads.

## Hardware Solutions

1) Disable Interrupt : CS problem can be solved if we could prevent interrupts from occuring while a shared variable was being modified

```c++
while (true) {
    // disable interrupts
    // CS
    // enable interrupts
    // remainder
}
```
Disadv : starvation allowed

2) Atomic Operations : execute read-modify-write operations atomically on a memory location

Adv : applicable to any number of processes on single/multiple processors sharing memory
Disadv : busy waiting is possible : starvation possible

To solve this we have Semaphores.
