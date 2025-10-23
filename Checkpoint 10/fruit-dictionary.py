def main():
    word_list = [
    "banana", "milk", "soda", "cheese", "sourmilk", "juice", "sausage",
    "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
    "soda", "sourmilk", "sourmilk", "butter", "soda", "chocolate"
    ]

    count(word_list)

def count(list):
    word_dictionary = {}
    for word in list:
        if word not in word_dictionary:     # Checks if the word is already in the dictionary,
            word_dictionary[word] = 0       # if not, then it adds it to the dictionary,
        word_dictionary[word] += 1          # and adds 1 to its value
    
    print(word_dictionary)
        
main()
