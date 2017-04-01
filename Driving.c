#include "Driving.h"

void forward(void)
{
	DRIVING_PORT|=0x00;
	USART_TransmitString("FORWARD",1);
}

void backward(void)
{
	DRIVING_PORT |= (1<<PINC1)|(1<<PINC0);
	USART_TransmitString("BACKWARD",1);
}


void sharp_right(void)
{
	DRIVING_PORT = (1<<DIR_LEFT);
	USART_TransmitString("SHRAP RIGHT",1);
}


void sharp_left(void)
{
	DRIVING_PORT = (1<<DIR_RIGHT);
	USART_TransmitString("SHARP LEFT",1);
}


void stop(void)
{
	PWM_LEFT  =  0;
	PWM_RIGHT =  0;
	
}


