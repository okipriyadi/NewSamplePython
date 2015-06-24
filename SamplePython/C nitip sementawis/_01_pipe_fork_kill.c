#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/stat.h>

int is_regular_file(const char *path)
{
		struct stat path_stat;
		stat(path, &path_stat);
		return S_ISREG(path_stat.st_mode);
}

int main(int argc, char **argv)
{
    printf("--beginning of program\n");

    int counter = 0;
    int status;
    pid_t child_pid , wpid;
    char a = 'b' ;
    int i = 0;
    char const *exec_arg1 = argv[1];
	char const *exec_arg2 = argv[2];
	int return_from_exec;
	int fd[2];
	pipe(fd);
	/*
	 * printf("arg1 = %s \n", exec_arg1);
	 * printf("arg2 = %s \n", exec_arg2);
	 * int bole  = is_regular_file(exec_arg1);
	 * printf("is file = %d \n", bole);
	 * if (bole == 0)
	{
			return 0;
	} 
	*/
    //printf("argv1 = %s",argv[1]);
    //printf("argv2 = %s",argv[2]);
    while (a == 'b') 
    {
		pid_t pid = fork();
		i = i + 1;
		if (pid == 0)
		{
			//child cuman nulis, jd close read-descriptor
			close(fd[0]);
			printf("get pid child = %d\n", getpid());
			printf("child : %d \n", i); 
			/*
			 * execl argumen1: perintah shell
			 * argumen2 : nama process yang berjalan(terserah kita)
			 * argumen3 : argumen untuk shell yg dijalankan tadi
			 * argumen4 : biarkan aja null, teu ngartos saya oge
			 */
			
			//char const d = execl("/bin/ping", "pong", "www.google.com", NULL); 
			return_from_exec = execl(exec_arg1, "pong", exec_arg2, NULL); 
			printf("di child return dari exec = %d \n", return_from_exec);
			write(fd[1], &return_from_exec, sizeof(return_from_exec));
			// fd sudah tak diperlukan, tutup!
			close(fd[1]);
			sleep(10);
			a = 'c';
		}
		else if (pid > 0)
		{
			//read only, jadi close aja write-descriptor
			close(fd[1]);
			read(fd[0], &return_from_exec, sizeof(return_from_exec));
			printf("parent dapat kiriman dari anak = %d", return_from_exec);
			// fd sudah tak diperlukan, tutup!
			close(fd[0]);
			if(return_from_exec == -1)
			{
				printf("seharusnya exit sih \n");
				return 0;
			}
			printf("get pid parent = %d\n", getpid());
			printf("parent :%d \n", i); 
			do {
					wpid = waitpid(pid, &status, WUNTRACED
						#ifdef 						WCONTINUED       					/* Not all implementations support this */
												| WCONTINUED
						#endif
						);
			
					printf("parent getpid : %d\n", getpid());
					if (wpid == -1) {
						perror("waitpid");
						exit(EXIT_FAILURE);
						}

					if (WIFEXITED(status)) {
						printf("child exited, status=%d\n", WEXITSTATUS(status));
						} 
					else if (WIFSIGNALED(status)) {
						printf("child killed (signal %d)\n", WTERMSIG(status));
						} 
					else if (WIFSTOPPED(status)) {
						printf("child stopped (signal %d)\n", WSTOPSIG(status));
						#ifdef WIFCONTINUED     /* Not all implementations support this */
						} 
					else if (WIFCONTINUED(status)) {
						printf("child continued\n");
						#endif
						} 
					else {    /* Non-standard case -- may never happen */
						printf("Unexpected status (0x%x)\n", status);
						}
			} while (!WIFEXITED(status) && !WIFSIGNALED(status));
			
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






















    /*
    if (pid == 0)
    {
        // child process
        printf("get pid child = %d\n", getpid());
        sleep(10000);
        int i = 0;
        for (; i < 5; ++i)
        {
            printf("child process: counter=%d\n", ++counter);
        }
    }
    else if (pid > 0)
    {
        // parent process
        printf("get pid parent = %d\n", getpid());
        sleep(10000);
        int j = 0;
        for (; j < 5; ++j)
        {
            printf("parent process: counter=%d\n", ++counter);
        }
    }
    else
    {
        // fork failed
        printf("fork() failed!\n");
        return 1;
    }
    printf("--end of program--\n");
    return 0;
}
*/
