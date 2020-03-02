#include <stdio.h>
#include <sys/msg.h>

#define BUFFER 50

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
	msgkey = ftok(".haha", 'm2');

	// obtain a queue id - should be same id as in send program
	rqueue = msgget(msgkey, 0660 | IPC_CREAT );



	while (1)
	{
		// retrieve message from queue
		status = msgrcv(rqueue, &rmessage, sizeof(rmessage.rdata), 0, 0);

		// check to see the message type - if 1 then print message out
		if (rmessage.mtype == 1)
			for (i = 0; i<BUFFER; i++) printf("Sequence [%d] : %d \n", i, rmessage.rdata[i]);
		// else print error message
		else printf("Wrong message type \n");
	}
	msgctl(rqueue,IPC_RMID,NULL);
	return 0;
}
