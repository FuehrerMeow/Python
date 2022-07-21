# Problem Set 2, wordle.py
# Name: Ife
# Collaborators:
# Time spent:


import random
import string
WORDLIST_FILENAME = "word.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
     """
     wordlist (list): list of words (strings)

     Returns a word from wordlist at random
     """

     return random.choice(wordlist)


def check_user_input(secret_word, user_guess):
    """
    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, the users guess
    :return: True/False - is the user input of valid type
    1. must be only characters
    2. must be the same length as the secret word
    3. extension: must be a valid word use the word list
    """

    if user_guess.isalpha() == False:
        print("Invalid word! Please try again.")
        return False
    if len(user_guess) != len(secret_word):
        print("Incorrect word length! Please try again.")
        return False
    return True


def get_guessed_feedback(secret_word, guess_word):
    """
    :param secret_word: a string - the word to be guessed
    :param user_guess: a string - a valid user guess
    :return: a string with uppercase/lowercase and _ e.g. 'B _ _ S u'
    """

    out = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess_word[i]:
            out += secret_word[i].upper() + " "
        elif guess_word[i] in secret_word:
            char = guess_word[i]
            if guess_word[:i].count(char) < secret_word.count(char):
                out += guess_word[i].lower() + " "
            else:
                out += "_ "
        else:
            out += "_ "
    return out


def get_alphabet_hint(secret_word, all_guesses):
    """
    takes in the secret word and a list of all_previous guesses and returns a string of hint text
    :param secret_word: a string - the word to be guessed
    :param all_guesses: a list of all the previous valid guesses the user inputed
    :return: a string - which deletes letters which were incorrect guesses and puts semi-correct guesses in /x/
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    out_list = []
    for char in alphabet:
        out_list.append(" " + char + " ")
    for guess in all_guesses:
        for i, char in enumerate(list(guess)):
            if char not in secret_word:
                out_list[alphabet.find(char)] = " _ "
            elif char != secret_word[i]:
                out_list[alphabet.find(char)] = "/" + char + "/"
            elif char == secret_word[i]:
                if secret_word.count(char) > guess.count(char):
                    out_list[alphabet.find(char)] = "/" + char + "/"
                else:
                    out_list[alphabet.find(char)] = "|" + char.upper() + "|"
    return "".join(out_list)


def wordle(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Wordle.
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    '''

    print("Secret word is", len(secret_word), "letters long.")

    num_of_guesses = 0
    while num_of_guesses < 6:
        print("You have",6 - num_of_guesses, "guesses left.")
        user_guess = input("Guess a word ")
        print("You have guessed", user_guess)
        num_of_guesses += 1
        correct_guess = check_user_input(secret_word, user_guess)
        print(get_guessed_feedback(secret_word, user_guess))
        if user_guess == secret_word:
            print("Correct!")
            break

    if user_guess == secret_word:
        print(secret_word)


if __name__ == "__main__":
    secret_word = choose_word(load_words())
    print(secret_word)
    wordle(secret_word)
