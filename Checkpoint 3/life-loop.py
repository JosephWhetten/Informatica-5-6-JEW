import time

def main():

    sg = "green"
    sb = "blue"
    sbl = "black"
    sy = "yellow"
    sp = "purple"
    sgo = "gold"
    spi = "pink"
    majiger = [sg, sb,sbl, sy, sp, sgo, spi]

    rem = 2
    while rem > 0:
        sock = input(f"What type of sock do you want? {majiger} ")
        rem -= 1

    day = 7
    while day > 0:
        socks = input("Good morning! What socks do you want to use? = ")
        print(f"You selected the {socks} socks, have a good day!\n")
        day -= 1
        time.sleep(2)
    print("You ran out of socks, time to wash the laundry!")

main()