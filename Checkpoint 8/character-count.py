def main():
    word = input("Type in any word: ")
    character_counter(word)
    


def character_counter(word):
    # i = 0
    # list = []
    dictionary = {}
    # while i < len(word):
    #     list.append(word[i])
    #     dictionary[word[i]] = list.count(word[i])
    #     i += 1
    for character in word.replace(" ",""):
        dictionary.setdefault(character, 0)
        dictionary[character] += 1
    print(dictionary)
    print(f"There are {len(word.replace(" ",""))} characters in the message")
    print(f"The most repeated letter is {list(dictionary.keys())[list(dictionary.values()).index(max(dictionary.values()))]}")
                                        #List of keys[(List of values).index(Most repeated letter)]

main()