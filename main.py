from simulator import robot
import time

# Get the sonar readings
def get_sonar_readings():
    left_distance, right_distance = robot.sonars()
    return left_distance, right_distance

# Stop the robot
def stop():
    robot.motors(0, 0, 0)

# Move forward function
def forward(distance):
    robot.motors(1, 1, distance)
    print("Moving forward for", distance)

# Move backward function
def backward(distance):
    robot.motors(-1, -1, distance)
    print("Moving backward for", distance)

# Turn left function
def left(angle):
    robot.motors(1, -1, (angle * 1.5) / 90)
    print("Turning left by", angle)

# Turn right function
def right(angle):
    robot.motors(-1, 1, (angle * 1.5) / 90)
    print("Turning right by", angle,)

def autonomous_move():
    forward(0.5)
    time.sleep(20)
    stop()
    print("Autonomous movement completed")

def first_move():
    choice1 = float(input("How far should the robot move? (1-20) "))
    choice2 = input("What direction should the robot turn? (left or right) ")
    choice3 = input("Should the robot move forward or backward? ")
    choice4 = float(input("How far should the robot move? (1-10) "))
    choice5 = float(input("How many seconds should the robot dance for? "))

    left_distance, right_distance = get_sonar_readings()
    print(f"Initial left sonar: {left_distance}, right sonar: {right_distance}")

    forward(choice1 * 0.1)
   
    left_distance, right_distance = get_sonar_readings()
    print(f"After moving forward: left sonar: {left_distance}, right sonar: {right_distance}")
   
    if choice2 == "left":
        print("Turning left")
        left(90)
    elif choice2 == "right":
        print("Turning right")
        right(90)

    left_distance, right_distance = get_sonar_readings()
    print(f"After turning: left sonar: {left_distance}, right sonar: {right_distance}")

    if choice3 == "backward":
        print("Moving backward")
        backward(choice4 * 0.1)
    elif choice3 == "forward":
        print("Moving forward")
        forward(choice4 * 0.1)

    left_distance, right_distance = get_sonar_readings()
    print(f"After moving: left sonar: {left_distance}, right sonar: {right_distance}")
    
    time.sleep(choice5)
    print(f"Danced for {choice5} seconds")

first_move()

def move_robot():
    while True:
        direction = input("Enter direction (forward, backward): ")
        if direction == "quit":
            print("Stopping the robot.")

        distance_input = input("Enter distance to move (e.g., 0.5, 1, 1.5): ")
        try:
            distance = float(distance_input)
            if distance > 0:
                if direction == "forward":
                    forward(distance)
                elif direction == "backward":
                    backward(distance)
                else:
                    print("Invalid direction! Please enter forward or backward.")
            else:
                print("Distance must be greater than 0.")
        except ValueError:
            print("Invalid input for distance. Please enter a positive number.")

move_robot()