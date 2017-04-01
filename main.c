/*
 * Drill_final_rover.c
 *
 * Created: 20-03-2017 22:41:05
 * Author : Chirag
 */ 
#include  <avr/io.h>
#include  <avr/interrupt.h>
#include  <util/delay.h>  
#include  <math.h>
#include  <avr/sfr_defs.h>   
#include  "USART_128.h"
#include  "drill.h"
#include  "Driving.h"

/*
up-down________OCR1A_________0-down
rotate_________OCR1B_________0-clockwise
box_motion_____OCR1C_________0-Forward
	2 Motors for box
	2 motors for drill
	
	L293D for Box 
	Cytron for drill
*/



int main (void)
{
	DRIVING_DDR=0xFF;
	DDRB=0xFF;
	DDRE = 0xFF;
 
	sei();
	USART_Init(51,1);
	USART_InterruptEnable(1);

	TCCR3A |= 1<<WGM31|(1<<COM3A1)|(1<<COM3B1)|(1<<COM3C1);
	TCCR3B |=(1<<WGM32)|( 1<<WGM33)|(1<<CS31);
	TCCR1A |= (1<<WGM11)|(1<<COM1A1)|(1<<COM1B1)|(1<<COM1C1);   //Fast PWM,Non Inverting mode
	TCCR1B |=(1<<WGM12)|( 1<<WGM13)|(1<<CS11);
	
	TCCR0 |= (1<<CS00) | ( 1<<CS01) | (1<<CS02);
	TIMSK |= (1<<TOIE0);
	
	
	ICR1 =10000;
	ICR3 = 100;
	
 		while(1)
        {	 
		
		}
 }
ISR(TIMER0_OVF_vect)
{
	ovfcount++;
}
ISR(USART1_RX_vect)
{
	m = USART_Receive(1);
	USART_Transmitchar(m,1);
	switch (m)
	{
		case 'F':
		forward();
		// 		_delay_ms(2000);
		// 		stop();
		
		break;

		case 'B':
		backward();
		// 		_delay_ms(2000);
		// 		stop();
		break;

		case 'R':
		sharp_right();
		// 		_delay_ms(500);
		// 		stop();
		break;

		case 'L':
		sharp_left();
		// 		_delay_ms(500);
		// 		stop();
		break;

		case 'Q' :
		PWM_LEFT  = 10000;
		PWM_RIGHT = 10000;
		
		break;
		case 'S' :
		stop();
		break;
		case 'D':
		trigger_drill;
		break;
		
		
		
		
		
		default:
		stop();
		
	}

	if (m>='0' && m<='9')
	{
		//PWM_LEFT = 10000*((m-'0')/10.0);
		PWM_RIGHT = 10000*((m-'0')/10.0);
		
	}

	
}


