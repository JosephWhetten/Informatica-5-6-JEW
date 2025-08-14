x = input("Put an emoji face\n")
x = x.strip().replace(":)", "😊").replace(":(", "😞")
print(f"This is how it should look like = {x}")