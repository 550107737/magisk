#include <linux/module.h>
#include <linux/init.h>

#include <rtai.h>
#include <rtai_sched.h>
#include <rtai_shm.h>
#include <rtai_sched.h>
#include <rtai_nam2num.h>

#include <linux/comedi.h>
#include <linux/comedilib.h>

#define ARG 0
#define STACK_SIZE 1024
#define PRIORITY RT_SCHED_HIGHEST_PRIORITY
#define USE_FPU 1
#define NOW rt_get_time()
#define PERIOD nano2count(1e8)

#define READ_SUBDEVICE 0
#define WRITE_SUBDEVICE 1
#define READ_CHANNEL 0
#define WRITE_CHANNEL 0
#define RANGE 0
#define AREF AREF_GROUND

#define BUFFER 100
int lock=0,locknum;
int buffer[BUFFER];
int in = 0, out = 0;
void write(int value){ 
	buffer[in] = value;
	in++; 
	if (in == BUFFER){
		in = 0;
	}
}


int judge(){
	int sum=0,i; 
	int temp=in;
	float c;
	/*
	for(i=0;i<20;i++){
		sum=sum+buffer[temp-i];
	}
	sum=sum / 20;
	*/
		printk("temp=%d",buffer[temp-1]);
		if(buffer[temp-1]>330 || buffer[temp-1]<30){
			printk("lock 360");
			lock=1;
			locknum=0;
		}	
		if(buffer[temp-1]>150 && buffer[temp-1]<210){
			printk("lock 180");
			lock=1;
			locknum=1;
		}
			return locknum;
		
	
	/*
	printk("judge=%d\n",sum);
	if(sum>140&&sum<220){
			return 1;
	}else{
			return 0;
	}
	*/
}

int transform(int x)
{
    int y;
	if ((x>2000&&x<2100))
	{
		if(lock==0){
			if(judge()==1)
				y = 180;
			else
				y=0;
		}else{
			if(locknum==1)
				y = 180;
			else
				y=0;
		}
		
	}
	else
	{
		lock=0;
		y = (2047 - x) * 180;
		y = y / 2047;
		if (y<0) {
			y = y + 360;
		}
	}
	y=360-y;
    return y;
}

int *memBuffer,*memIn;
void share()
{
	
	memBuffer[in] = buffer[in];
	*memIn = in;
}

/* Store data needed for the thread */
RT_TASK thread_data;

/* Data needed by comedi */
comedi_t *comedi_dev;

/* The code that is run */
void thread_code(long arg)
{
  while (1)
  {
    int read_value, write_value = 0; /* What value should write_value be? */
    comedi_data_read(comedi_dev, READ_SUBDEVICE, READ_CHANNEL, RANGE, AREF, &read_value);
    int degree = transform(read_value);
    //temp = read_value;
    write(degree);
    share();
    comedi_data_write(comedi_dev, WRITE_SUBDEVICE, WRITE_CHANNEL, RANGE, AREF, write_value);
    printk("degree = %d  data=%d\n", degree,read_value);
    /* Add code here */
    rt_task_wait_period();
  }
}

/* Called when "insmod" is used */
static int __init template_init(void)
{
  /* Start the RT timer, NB only needs to be done once */
  rt_set_periodic_mode();
  start_rt_timer(PERIOD);

  memBuffer = rtai_kmalloc(nam2num("shmem0"), sizeof(int)*BUFFER);
  memIn = rtai_kmalloc(nam2num("shmem1"), sizeof(int));
	
  comedi_dev = comedi_open("/dev/comedi0");

  /* Initialise the data associated with a thread and make it periodic */
  rt_task_init(&thread_data, thread_code, ARG, STACK_SIZE, PRIORITY, USE_FPU, NULL);
  rt_task_make_periodic(&thread_data, NOW, PERIOD);

  /* Return success */
  return 0;
}

/* Called when "rmmod" is used */
static void __exit template_exit(void)
{
  rt_task_delete(&thread_data);
  rtai_kfree(nam2num("shmem0"));
  rtai_kfree(nam2num("shmem1"));
  comedi_close(comedi_dev);
}

module_init(template_init);
module_exit(template_exit);
