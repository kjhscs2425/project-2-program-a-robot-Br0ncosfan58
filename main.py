from simulator import robot  
import time  

left_distance, right_distance = robot.sonars()  
robot.sonars()  
  
def forward(distance):  
   robot.motors(1, 1, distance)  
  
def backward(distance):  
   robot.motors(-1, -1, distance)  
  
def left(angle):  
   distance = angle  
   robot.motors(-1, 1, distance)  
  
def right(angle):  
   distance = angle  
   robot.motors(1, -1, distance)  
  
def draw_M():  
   print("Drawing M...")  
   forward(10)  
   left(45)  
   forward(10)  
   right(90)  
   left(45)  
   backward(10)  
   print("M drawn!") 
  
def draw_A():  
   print("Drawing A...")  
   forward(10)  
   left(60)  
   forward(10)  
   right(120)  
   forward(10)  
   left(60)  
   backward(10)  
   print("A drawn!")  
  
def draw_X():  
   print("Drawing X...")  
   forward(10)  
   left(45)  
   forward(10)  
   right(90)  
   forward(10)  
   left(45)  
   backward(10)  
   right(45)  
   forward(10)  
   left(90)  
   forward(10)  
   right(45)  
   backward(10)  
   print("X drawn!")  
  
draw_M()  
draw_A()  
draw_X()