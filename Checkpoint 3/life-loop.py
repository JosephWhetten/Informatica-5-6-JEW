import time

def main():

    sg = "green"
    sb = "blue"
    sbl = "black"
    sy = "yellow"
    sp = "purple"
    sgo = "gold"
    spi = "pink"
    majiger = [sg, sb, sbl, sy, sp, sgo, spi]

    rem = 7
    while rem > 0:
        sock = input(f"What type of sock do you want? {majiger} ")
        rem -= 1
        if sock == sg:
            majiger = majiger - sg
        if sock == sb:
            majiger = [sg, sbl, sy, sp, sgo, spi]
        if sock == sbl:
            majiger = [sg, sb, sy, sp, sgo, spi]
        if sock == sy:
            majiger = [sg, sb, sbl, sp, sgo, spi]
        if sock == sp:
            majiger = [sg, sb, sbl, sy, sgo, spi]
        if sock == sgo:
            majiger = [sg, sb, sbl, sy, sp, spi]
        if sock == spi:
            majiger = [sg, sb, sbl, sy, sp, sgo]

    day = 7
    while day > 0:
        time.sleep(2)
        socks = input("Good morning! What socks do you want to use? = ")
        print(f"You selected the {socks} socks, have a good day!\n")
        day -= 1
        
    print("You ran out of socks, time to wash the laundry!")

main()