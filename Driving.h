#ifndef Driving
#define Driving

#include <avr/io.h>
#include <avr/sfr_defs.h>

#define PWM_LEFT		OCR1A
#define PWM_RIGHT		OCR1B
#define DRIVING_DDR         DDRC
#define DRIVING_PORT        PORTC
#define DIR_LEFT	    PINC0
#define DIR_RIGHT	    PINC1

void forward(void);
void backward(void);
void sharp_left(void);
void sharp_right(void);
void left_Turn(void);
void right_Turn(void);
void stop(void);

char m;
#endif