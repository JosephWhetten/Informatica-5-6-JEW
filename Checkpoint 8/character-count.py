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
    for character in word:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1
    print(dictionary)
    print(f"There are {len(word)} characters in the word")
    print(max(dictionary.values()))

main()