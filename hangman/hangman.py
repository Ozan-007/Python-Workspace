from words import words
import random
import string


#
def get_valid_word():
    word = random.choice(words)
    if "-" in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word()
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    word_letters = set(word)

    while len(word_letters) > 0:

        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print("Your Stage: ", " ".join(word_list))
        print("Words you already used: ", " ".join(used_letters))
        user_letters = input("Enter a letter : ").upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word:
                word_letters.remove(user_letters)
        elif user_letters in used_letters:
            print("You already used this letter ")
        else:
            print("Invalid Option")

    print(f"\n !! Congratulations you find the {word} !!")
hangman()
# word = "OzannaO"
# print(set(word))
# letters = string.ascii_lowercase
# print(letters)
# # setler icerisinde en yalin halini tuple gibi depolar bir harften yalnizca bir tane bulunur ve harflerin sirasi yoktur.
# # Setker arasinda cikarma islemi yapilabiliyoruz setin arasindaki farkli olani kullanabiliyoruz
# a = {1, 2, 3, 4}
# b = {2, 3, 4}
# print(a - b)
#
# loop = ["O","O","z","a","n"]
# for i in loop:
#     print(i)
#
# names = ["a","c","d"]
# a = "hello"
#
# print("".join(names))
# # Join(list) gibi ekledigimizde joinledigimiz kisimi joinleyip birlestiriyor parantez icindekiyle.
