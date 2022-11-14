def check_win(secret_word, old_letters_guessed):
    """check if the secred word is guessed
    :param secret_word: the word the user is trying to guess
    :param old_letters_guessed: list of guesses letters
    :return: true if it guesses, false otherwise
    """
    for i in secret_word:
        if i not in old_letters_guessed:
            return False

    you_won()
    return True;


def show_hidden_word(secret_word, old_letters_guessed):
    """print the current state of the guesses word
    :param secret_word: the word
    :param old_letters_guessed: list of used letters
    :return: none
    """
    output = ""

    for i in secret_word:
        if i in old_letters_guessed:
            output += i + " "
        else:
            output += "_ "

    print(output[:-1])


def check_valid_input(letter_guessed):
    """Check for a proper user input
    :param letter_guessed: the letter the user have guesses
    :param old_letters_guessed: already used letters
    :return: True - valid input     False - invalid input
    """
    letter_guessed = letter_guessed.lower()

    if len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """a function that receive a letter guesses by the user and a string of already used letters and try to assign the
    newly guessed letter to the list if it is valid.
    :param secret_word: the secret word the user need to guess
    :param letter_guessed: the letter the used guesses
    :param old_letters_guessed: list of used letters
    :return: False - doesn't count as bad guess        True - count as bad guess
    """
    if not check_valid_input(letter_guessed):
        print("invalid input!")
        return False
    else:
        if letter_guessed in old_letters_guessed:
            print("you have already guessed this letter!\nLetters guessed: ")
            print(format_list(old_letters_guessed))
            return False
        elif letter_guessed in secret_word:
            print("You have guessed a letter!")
            old_letters_guessed.append(letter_guessed)
            return False;
        else:
            print("this letter is not in the word!")
            print("Letters guessed: \n "+format_list(old_letters_guessed))
            old_letters_guessed.append(letter_guessed)
            return True


def format_list(my_list):
    """a function that recive a list of strings and return a string of all the concatenated strings separated by an
    arrow in a sorted alphabetical order.

    :param my_list: list of string
    :return: the concatenated string
    """
    my_list.sort()
    return ', '.join(my_list[:])


def choose_word(file_path, index):
    """receive a path to file containing list of words and return the index-th one
    :param file_path: path to file
    :param index: the index-th word
    :return: the word in place index from the file
    """
    try:
        words_file = open(file_path, "r")
        word_list = words_file.read()
        words_file.close()
    except:  # catch *all* exceptions
        print("ERROR! file not found in the given path!\nThe program will exit.")
        exit()

    try:
        word_list = word_list.split(" ")
        return word_list[index]
    except:
        print("ERROR! illigal index!\nThe program will exit.")
        exit()

def print_welcome_menu():
    """print the welcome menu screen
    :return: none
    """
    print("\nWelcome to the game Hangman")

    print("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
    """)


def print_game_state(number_of_errors):
    """print the state of the hangman based on the amount of error the player made
    :param number_of_errors:  number of errors
    :return: none
    """
    match number_of_errors:
        case 0:
            # image 1
            print("""
                x-------x
            """)
        case 1:
            # image 2
            print("""
                x-------x
                |
                |
                |
                |
                |""")
        case 2:
            # image 3
            print("""
                x-------x
                |       |
                |       0
                |
                |
                |
            """)
        case 3:
            # image 4
            print("""
                x-------x
                |       |
                |       0
                |       |
                |
                |
            """)
        case 4:
            # image 5
            print("""
                x-------x
                |       |
                |       0
                |      /|\\
                |
                |
            """)
        case 5:
            # image 6
            print("""
                    x-------x
                    |       |
                    |       0
                    |      /|\\
                    |      /
                    |
            """)
        case 6:
            # image 7
            print("""
                x-------x
                |       |
                |       0
                |      /|\\
                |      / \\
                |
            """)
            game_over()

        case default:
            print("An error occurred! the program will exit now.")
            exit()


def game_over():
    """ print the game over screen and exit the program
    :return: none
    """
    print("""
       _____          __  __ ______    ______      ________ _____  
      / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
     | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
     | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
     | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
      \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\\
    """)
    exit()


def you_won():
    """print the you won! screen and exit the program
    :return: none
    """
    print("""
     __     ______  _    _  __          ______  _   _   _ 
     \ \   / / __ \| |  | | \ \        / / __ \| \ | | | |
      \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| | | |
       \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` | | |
        | | | |__| | |__| |    \  /\  / | |__| | |\  | |_|
        |_|  \____/ \____/      \/  \/   \____/|_| \_| (_)
    """)
    exit()


def get_word():
    """ask the user for path file and the word's index inside of it and get it
    :return: the chosen word
    """
    print("Enter the path for the file: ")
    path_for_file = input()

    print("Enter word index (counting from 0): ")
    try:
        word_index = int(input())
    except:
        print("An error occured! the program will now exit.")
        exit()

    return choose_word(path_for_file, word_index)


def guess_letter(old_letters_guessed, secret_word):
    """ask the user to guess a letter, if it is a valid guess but a false one increase the counter by 1
    :param secret_word: the string the user try to guess
    :param old_letters_guessed: list of already guesses letters
    :return: 0 - good guess     1 - bad guess
    """
    letter = input("guess a letter: ")

    if try_update_letter_guessed(letter, old_letters_guessed, secret_word):
        return 1
    return 0


def main():
    print_welcome_menu()
    secret_word = get_word()  
    
    number_of_errors = 0
    old_letters_guessed = []

    while True:
        print_game_state(number_of_errors)
        show_hidden_word(secret_word, old_letters_guessed)

        number_of_errors += guess_letter(old_letters_guessed, secret_word)

        check_win(secret_word, old_letters_guessed)


if __name__ == '__main__':
    main()
