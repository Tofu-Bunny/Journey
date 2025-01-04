# FANCY FLYING ENABLER V2 - By Tofu

import vgamepad as vg
import keyboard
import time
enabled = False

#///////////////////////////////|
# Set keybinds here:
BIND1 = 'q'
BIND2 = 'e'
TOGGLE = 't'
QUIT = 'F9'

# Set steer values (in %) here:
PER1 = 63
PER2 = 70

#///////////////////////////////|
gamepad = vg.VX360Gamepad()

# Convert percentage to steer value 
VALUE1 = round(32767/100*PER1)
VALUE2 = round(32767/100*PER2)

# Move left stick up PER1%
def move_left_stick_up_PER1():
    gamepad.left_joystick(x_value=0, y_value=VALUE1)
    gamepad.update()

# Move left stick up PER2%
def move_left_stick_up_PER2():
    gamepad.left_joystick(x_value=0, y_value=VALUE2)
    gamepad.update()

# Reset stick to neutral
def reset_left_stick():
    gamepad.left_joystick(x_value=0, y_value=0)
    gamepad.update()

print("  /)_/) ")
print(" („•֊•„) <3")
print("--U   U------------------------------")
print("Press", BIND1, "to move forward "+ str(PER1)+ "%.(y="+ str(VALUE1)+")")
print("Press", BIND2, "to move forward "+ str(PER2)+ "%.(y="+ str(VALUE2)+")")
print("Press", TOGGLE, "to turn controls ON or OFF")
print("Press", QUIT, "if something breaks")
print(" ")
print("Flight controls are OFF")

# Detect key press
while True:
    event = keyboard.read_event()

    #Toggle button
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == TOGGLE:
            enabled = not enabled #Turns flag ON
            print(f"Flight controls are {'ON -- Have a nice flight c:' if enabled else 'OFF'}")
    if enabled:
        if keyboard.is_pressed(BIND1):
            move_left_stick_up_PER1()
            
        elif keyboard.is_pressed(BIND2):
            move_left_stick_up_PER2()
            
        else:
            reset_left_stick()
    else:
        reset_left_stick()
            
    
# Ouch ouchie kill it
    if keyboard.is_pressed(QUIT):
        print("Bye bye :3")
        time.sleep(1.0)
        break
time.sleep(0.01)
