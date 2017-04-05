import serial
import time
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class control(object):
	def turn_left(self,event):
		print 'turn left'
		file = open('navigate.txt','w')
		file.write('l')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()
		

		
	def turn_right(self,event):
		print 'turn right'
		file = open('navigate.txt','w')
		file.write('r')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()
		
		
	def move_forward(self,event):
		print 'move forward'
		file = open('navigate.txt','w')
		file.write('f')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()
		
	def move_back(self,event):
		print 'move back'
		file = open('navigate.txt','w')
		file.write('b')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()
		

	def mot1_forward(self,event):
		print 'motor1 forward'
		file = open('navigate.txt','w')
		file.write('a')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()
		

	def mot1_back(self,event):
		print 'motor1 back'
		file = open('navigate.txt','w')
		file.write('c')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()


	def mot2_forward(self,event):
		print 'motor2 forward'
		file = open('navigate.txt','w')
		file.write('d')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()
		

	def mot2_back(self,event):
		print 'motor2 back'
		file = open('navigate.txt','w')
		file.write('e')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot3_forward(self,event):
		print 'motor3 forward'
		file = open('navigate.txt','w')
		file.write('g')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot3_back(self,event):
		print 'motor3 back'
		file = open('navigate.txt','w')
		file.write('h')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot4_forward(self,event):
		print 'motor4 forward'
		file = open('navigate.txt','w')
		file.write('i')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot4_back(self,event):
		print 'motor4 back'
		file = open('navigate.txt','w')
		file.write('j')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot5_forward(self,event):
		print 'motor5 forward'
		file = open('navigate.txt','w')
		file.write('k')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot5_back(self,event):
		print 'motor5 back'
		file = open('navigate.txt','w')
		file.write('m')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot6_forward(self,event):
		print 'motor6 forward'
		file = open('navigate.txt','w')
		file.write('n')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def mot6_back(self,event):
		print 'motor6 back'
		file = open('navigate.txt','w')
		file.write('o')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()

	def drill_up(self,event):
		print 'drill up'
		file = open('navigate.txt','w')
		file.write('p')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()
	def drill_down(self,event):
		print 'drill down'
		file = open('navigate.txt','w')
		file.write('q')
		file.close()
		time.sleep(0.005)
		file = open('navigate.txt','w')
		file.write('s')
		file.close()



callback = control()
plt.ion()




plt.figure(1)

plt.figtext(0.1,0.95,'Bot',fontsize='20')

turnright = plt.axes([0.3, 0.8, 0.1, 0.075])
t_right=Button(turnright,'>')
t_right.on_clicked(callback.turn_right)

turnleft = plt.axes([0.1, 0.8, 0.1, 0.075])
t_left=Button(turnleft,'<')
t_left.on_clicked(callback.turn_left)

forward = plt.axes([0.2, 0.9, 0.1, 0.075])
m_forward=Button(forward,'^')
m_forward.on_clicked(callback.move_forward)

backward = plt.axes([0.2, 0.7, 0.1, 0.075])
m_back=Button(backward,'v')
m_back.on_clicked(callback.move_back)

plt.figtext(0.6,0.7,'Arm Motor',fontsize='20')

motor1f = plt.axes([0.7, 0.6, 0.1, 0.075])
m1_forward=Button(motor1f,'>')
m1_forward.on_clicked(callback.mot1_forward)

plt.figtext(0.62,0.62,'M1',fontsize='20')

motor1b = plt.axes([0.5, 0.6, 0.1, 0.075])
m1_back=Button(motor1b,'<')
m1_back.on_clicked(callback.mot1_back)

motor2f = plt.axes([0.7, 0.5, 0.1, 0.075])
m2_forward=Button(motor2f,'>')
m2_forward.on_clicked(callback.mot2_forward)

plt.figtext(0.62,0.52,'M2',fontsize='20')

motor2b = plt.axes([0.5, 0.5, 0.1, 0.075])
m2_back=Button(motor2b,'<')
m2_back.on_clicked(callback.mot2_back)

motor3f = plt.axes([0.7, 0.4, 0.1, 0.075])
m3_forward=Button(motor3f,'>')
m3_forward.on_clicked(callback.mot3_forward)

plt.figtext(0.62,0.42,'M3',fontsize='20')

motor3b = plt.axes([0.5, 0.4, 0.1, 0.075])
m3_back=Button(motor3b,'<')
m3_back.on_clicked(callback.mot3_back)

motor4f = plt.axes([0.7, 0.3, 0.1, 0.075])
m4_forward=Button(motor4f,'>')
m4_forward.on_clicked(callback.mot4_forward)

plt.figtext(0.62,0.32,'M4',fontsize='20')

motor4b = plt.axes([0.5, 0.3, 0.1, 0.075])
m4_back=Button(motor4b,'<')
m4_back.on_clicked(callback.mot4_back)

motor5f = plt.axes([0.7, 0.2, 0.1, 0.075])
m5_forward=Button(motor5f,'>')
m5_forward.on_clicked(callback.mot5_forward)

plt.figtext(0.62,0.22,'M5',fontsize='20')

motor5b = plt.axes([0.5, 0.2, 0.1, 0.075])
m5_back=Button(motor5b,'<')
m5_back.on_clicked(callback.mot5_back)

motor6f = plt.axes([0.7, 0.1, 0.1, 0.075])
m6_forward=Button(motor6f,'>')
m6_forward.on_clicked(callback.mot6_forward)

plt.figtext(0.62,0.12,'M6',fontsize='20')

motor6b = plt.axes([0.5, 0.1, 0.1, 0.075])
m6_back=Button(motor6b,'<')
m6_back.on_clicked(callback.mot6_back)

plt.figtext(0.15,0.5,'Drill Control',fontsize='20')

drillup = plt.axes([0.2, 0.35, 0.1, 0.075])
d_up=Button(drillup,'^')
d_up.on_clicked(callback.drill_up)

drilldown = plt.axes([0.2, 0.2, 0.1, 0.075])
d_down=Button(drilldown,'v')
d_down.on_clicked(callback.drill_down)


#added spare button to solve the problem of graph being plotted in pushbutton
#needs to look into

sparebutton = plt.axes([0.0001, 0.0001, 0.0001, 0.0001])
s_button=Button(sparebutton,'')


plt.figure(2)



while True:
	
	plt.figure(2)
	file = open('ser_data.txt','r')
	ydata = map(int,file.readlines())
	print ydata
	file.close()
	plt.plot(ydata)
	plt.show()
	plt.pause(0.5)
	plt.cla()
