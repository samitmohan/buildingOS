#include <stdio.h>
#include <unistd.h>

int main() {
    printf("this is first program");
    fflush(stdout);
//	exec("b.out");
    execl("./b.out", "b.out", NULL);

    printf("this will not get printed");
    return 0;
}
