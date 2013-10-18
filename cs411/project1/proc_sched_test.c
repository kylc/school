#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sched.h>

#define MAX 100000000000

/* Modified from:
 * http://www.zacharyfox.com/blog/fibonacci-project/fibonacci-in-c
 */
int fibonacci(int n)
{
        int a = 0;
        int b = 1;
        int sum;
        int i;

        for (i = 0; i < n; i++) {
                sum = a + b;
                a = b;
                b = sum;
        }

        return 0;
}

int main(void)
{
        pid_t pid = getpid();

        struct sched_param param;
        param.sched_priority = 1;

        // int err = sched_setscheduler(pid, SCHED_FIFO, &param);
        int err = sched_setscheduler(pid, SCHED_RR, &param);
        printf("Error: %d\n", err);

        int f = fibonacci(MAX);
        printf("Fib: %d\n", f);

        return 0;
}
