from pynput import mouse, keyboard

# Variable to keep track of the last mouse click coordinates
last_click_coordinates = (None, None)
stop_flag = False  # Flag to stop the mouse listener when 'Esc' is pressed

def on_click(x, y, button, pressed):
    global last_click_coordinates
    if pressed:
        last_click_coordinates = (x, y)  # Store the coordinates
        print(f"Mouse clicked at ({x}, {y})")

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

print("Test")

print(f'The coordinate is {last_click_coordinates[0]}, {last_click_coordinates[1]}')
