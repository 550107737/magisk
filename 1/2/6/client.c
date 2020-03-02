#include <stdio.h>
#include <rtai.h>
#include <rtai_nam2num.h>
#include <rtai_shm.h>
#include <sys/msg.h>


#define BUFFER 1

int *mem2;
struct mymsgbuf {
	long mtype;
	int rdata[BUFFER];
}rmessage;


int main(void)
{
	int status, i;
	int rqueue;
	key_t msgkey;

	// generate the message key to obtain a queue id - same as in send program
	msgkey = ftok(".haha", 'm2222');

	// obtain a queue id - should be same id as in send program
	rqueue = msgget(msgkey, 0660 | IPC_CREAT );

	mem2 = rtai_kmalloc(nam2num("shmem2"), sizeof(int));

	while (1)
	{
		// retrieve message from queue
		status = msgrcv(rqueue, &rmessage, sizeof(rmessage.rdata), 0, 0);

		// check to see the message type - if 1 then print message out
		if (rmessage.mtype == 1){
			*mem2 = rmessage.rdata[0];
            printf("%d\n",*mem2);
        }
		// else print error message
		else printf("Wrong message type \n");
	}
	msgctl(rqueue,IPC_RMID,NULL);
	rtai_free(nam2num("shmem2"), *mem2);
	return 0;
}
