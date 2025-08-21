def main():

    is_armed = True
    motion_detected = True
    door_open = False
    is_dark = True
    display_alarm(is_armed, motion_detected, door_open, is_dark)

def display_alarm(armed, motion, door, dark):
    if armed:
        if motion:
            print("Alarm: HERE COMES BRANDON")
        if door:
            print("Silent Alert: Door is open")
    else:
        if dark and motion:
            print("Welcome home my guy")
    
main()