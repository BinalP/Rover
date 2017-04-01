#ifndef         drill
#define         drill
#include       <avr/io.h>
#include       <avr/interrupt.h>
#define Dir_drill_Vert		    PINC2
#define Dir_drill_Rot		    PINC3
#define Box_hor_                PINC4

#define Dir_drill_vert_PWM		PB5
#define Dir_drill_Rot_PWM		PB6
#define Box_hor_PWM				PB7
char m;

extern volatile int ovfcount ;
extern volatile int flag;
extern volatile int i;
void Bring_box_forward();
void Sent_box_backward();
void drill_up();
void drill_down_clock();
void stop_all();
void rotate_anti();
void trigger_drill();
int user_def_delay_sec(float seconds);




#endif