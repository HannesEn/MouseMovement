import pyautogui
import time

def positiveMove():
    # Get the current mouse position
    current_x, current_y = pyautogui.position()
    # Define the distance to move the mouse (adjust as needed)
    move_distance = 30
    new_x = current_x + move_distance
    new_y = current_y + move_distance
    # Move the mouse to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.2)
def negativeMove():
    # Get the current mouse position
    current_x, current_y = pyautogui.position()
     # Define the distance to move the mouse (adjust as needed)
    move_distance = 30
    new_x = current_x - move_distance
    new_y = current_y - move_distance
    # Move the mouse to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.2)
def move_mouse(value):
    # Calculate the new mouse position
    if value == 'positive':
        positiveMove();
    else:
        negativeMove()
    print("Main function executed")

# Perform the mouse movement every 10 seconds(adjust as needed)
timeToSleep = 10
while 0==0:
    move_mouse(value = 'positive')
    time.sleep(timeToSleep)
    move_mouse(value = 'negative')
    time.sleep(timeToSleep)