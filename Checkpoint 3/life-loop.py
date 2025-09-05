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
            majiger.remove(sg)
        if sock == sb:
            majiger.remove(sb)
        if sock == sbl:
            majiger.remove(sbl)
        if sock == sy:
            majiger.remove(sy)
        if sock == sp:
            majiger.remove(sp)
        if sock == sgo:
            majiger.remove(sgo)
        if sock == spi:
            majiger.remove(spi)
    print("You ran out of socks! Time to do your laundry...")

    # day = 7
    # while day > 0:
    #     time.sleep(2)
    #     socks = input("Good morning! What socks do you want to use? = ")
    #     print(f"You selected the {socks} socks, have a good day!\n")
    #     day -= 1
        
    # print("You ran out of socks, time to wash the laundry!")

main()