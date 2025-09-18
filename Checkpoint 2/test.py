import getpass

# Prompt the user for input without displaying it
hidden_input = getpass.getpass("Enter your secret: ")

print("Your input has been securely received!")
print(hidden_input)