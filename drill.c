#include "drill.h"
volatile int ovfcount=0 ;
volatile int flag=0;
volatile int i=0.5;
void  drill_down_clock(void)
{
	PORTC = 0x00;
	OCR3A =50;
	OCR3B =100;
	OCR3C=00;
}
void drill_up(void)
{
	PORTC =(1<<Dir_drill_Vert);
	OCR3A =50;
	OCR3B =0;
	OCR3C=0;
}
void rotate_anti(void)
{
	PORTC =(1<<Dir_drill_Rot);
	OCR3A =0;
	OCR3B =100;
	OCR3C =0;
}
void Bring_box_forward(void)
{
	OCR3A = 0;
	OCR3B = 0;
	OCR3C = 100;
}
void Sent_box_backward(void)
{
	PORTC = (1<<Box_hor_);
	OCR3A = 0;
	OCR3B = 0;
	OCR3C = 100;
}
void stop_all(void)
{
	OCR3C=0;
	OCR3B=0;
	OCR3A=0;
}
int user_def_delay_sec(float seconds)
{
	double desired_overflow,T=0.000128;
	desired_overflow =seconds/(256*T);
	round(desired_overflow);
	ovfcount=0;
	TCNT0=0;
	while(ovfcount < desired_overflow)
	{
		
	}
	TCNT0=0;
	ovfcount=0;
}

void trigger_drill(void)
{
	stop_all();
	Bring_box_forward();
	user_def_delay_sec(2.15) ;
	rotate_anti();
	user_def_delay_sec(2.5);
	Sent_box_backward();
	user_def_delay_sec(2.15);
	drill_down_clock();
	user_def_delay_sec(i+7);
	drill_up();
	user_def_delay_sec(7);
	i++;
	
}
