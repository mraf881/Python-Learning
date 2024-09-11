import time
import pyautogui
from pynput import mouse, keyboard

#Initial Note
print("Remember to clean up the defined answer with Notepad++!!!!")
time.sleep(5)
print("Cursor Coordinate Detector Started!")
time.sleep(0.5)
print("Click the mouse to detect the coordinate!")
##### MOUSE LISTENER ######
# Variable to keep track of the last mouse click coordinates
last_click_coordinates = (None, None)
stop_flag = False  # Flag to stop the mouse listener when 'Esc' is pressed

def on_click(x, y, button, pressed):
    global last_click_coordinates
    if pressed:
        last_click_coordinates = (x, y)  # Store the coordinates
        print(f"Cursor coordinate at ({x}, {y}); Left-click again to detect the coordinate or press 'esc' key to capture the coordinate")

def on_press(key):
    global stop_flag
    try:
        if key == keyboard.Key.esc:
            stop_flag = True
            return False  # Stop the keyboard listener
    except AttributeError:
        pass

# Set up the mouse listener
def start_listeners():
    with mouse.Listener(on_click=on_click) as mouse_listener, \
         keyboard.Listener(on_press=on_press) as keyboard_listener:
        
        while not stop_flag:
            mouse_listener.join(0.1)
            keyboard_listener.join(0.1)

    print("Done")
    if last_click_coordinates != (None, None):
        print(f"Last captured coordinate: x = {last_click_coordinates[0]}, y = {last_click_coordinates[1]}")
    else:
        print("No mouse clicks detected.")

start_listeners()

print(f'The captured cursor coordinate is {last_click_coordinates[0]}, {last_click_coordinates[1]}')
time.sleep(0.5)
##############################

print("Proceeding to insertdefined answer in form question")
time.sleep(2)

#Enter the drop down starting coordinate
dropdown_x = last_click_coordinates[0]
dropdown_y = last_click_coordinates[1]

#Iterate through list of drop down answer
dropdown_answer_list = ["Answer1","Answer2", "Answer3"]


#To count how many answer
count_dropdown_answer_list = len(dropdown_answer_list)

#To click starting point
pyautogui.click(dropdown_x,dropdown_y, button="left")
time.sleep(0.1)

#To enter first answer
print(f"Inserting... {dropdown_answer_list[0]}")
time.sleep(0.1)
pyautogui.write(dropdown_answer_list[0])
print(f"{dropdown_answer_list[0]} is inserted")
time.sleep(0.1)

#To iterate the rest ofthe list

for n in range(1,count_dropdown_answer_list):
    pyautogui.press('enter')
    time.sleep(0.1)
    print(f"Inserting... {dropdown_answer_list[n]}")
    pyautogui.write(dropdown_answer_list[n])
    print(f"{dropdown_answer_list[n]} is inserted")
    time.sleep(0.1)

print(f"All {count_dropdown_answer_list} have been inserted succesfully")
