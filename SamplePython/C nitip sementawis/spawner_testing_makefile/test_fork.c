#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char **argv)
{
	pid_t wpid;
	char a = 'b' ;
    char const *exec_arg1 = argv[1];
	char const *exec_arg2 = argv[2];
    int status;
    int i = 0;
	
	printf("--beginning of program\n");
    while (a == 'b') 
    {
		pid_t pid = fork();
		i = i + 1;
		if (pid == 0)
		{
			printf("get pid child%d = %d\n", i, getpid()); 
			execl(exec_arg1, "child", exec_arg2, NULL); 
			exit(0);
		}
		else if (pid > 0)
		{
			printf("get pid parent = %d\n", getpid()); 
			do {
					wpid = waitpid(pid, &status, WUNTRACED
						#ifdef 					WCONTINUED       					
												| WCONTINUED
						#endif
						);
						
					if (wpid == -1) {
						perror("waitpid");
						exit(EXIT_FAILURE);
						}

					if (WIFEXITED(status)) {
						printf("child exited, status=%d\n", WEXITSTATUS(status));
						if(WEXITSTATUS(status) == 0){
							exit(0);
							}
						} 
					else if (WIFSIGNALED(status)) {
						printf("child killed (signal %d)\n", WTERMSIG(status));
						} 
						
					else if (WIFSTOPPED(status)) {
						printf("child stopped (signal %d)\n", WSTOPSIG(status));
						#ifdef WIFCONTINUED     
						}
						 
					else if (WIFCONTINUED(status)) {
						printf("child continued\n");
						#endif
						}
						 
					else {    
						printf("Unexpected status (0x%x)\n", status);
						}
						
			} while (!WIFEXITED(status) && !WIFSIGNALED(status));
			sleep(1);
		}	
		
		else
		{
			printf("fork() failed!\n");
			return 1;
		}
	}	
	printf("--end of program--\n");
    return 0;
}
