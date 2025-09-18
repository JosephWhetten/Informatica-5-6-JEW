def main():

    characters = ["Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser"]
    for person in characters:
        if person != "Princess Peach":
            letter(person,"Princess Peach")

def letter(receiver,sender): 
    print(f"""
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},
        
        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """)

main()