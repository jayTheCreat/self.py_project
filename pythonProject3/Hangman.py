HANGMAN_ASCII_ART = r"""Welcome to the game Hangman
   _    _
  | |  | |
  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |
                      |___/
"""
MAX_TRIES = 6
HANGMAN_PHOTOS = {0: r"""x-------x""", 1: r"""x-------x
|
|
|
|
|""", 2: r"""x-------x
|       |
|       0
|
|
|""", 3: r"""x-------x
|       |
|       0
|       |
|
|""", 4: r"""x-------x
|       |
|       0
|      /|\
|
|""", 5: r"""x-------x
|       |
|       0
|      /|\
|      /
|""", 6: r"""x-------x
|       |
|       0
|      /|\
|      / \
|"""}


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Check if the input letter is valid (1 letter, english letter, not guessed before)
    :param letter_guessed: the letter that  was guessed by the player
    :param old_letters_guessed: the previous letters guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True, if the letter is valid. False if not
    :rtype: bool
    """
    if (len(letter_guessed) > 1) or (not letter_guessed.isalpha()) or (letter_guessed.lower() in old_letters_guessed):
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    if the letter_guessed is valid, the function adds it to the old_letters_guessed.
    if he print X and the old_letters_guessed in alphabetical order
    :param letter_guessed: the letter that  was guessed by the player
    :param old_letters_guessed: the previous letters guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True, if the letter is valid. False if not
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print(f'X\n{"->".join(sorted(old_letters_guessed))}')
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    the function returns the current state of the secret_word base on the old_letters_guessed
    :param secret_word: the word that the player has to guess
    :param old_letters_guessed: the previous letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: returns a string consisting of letters and underscores
    :rtype: str
    """
    new_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            new_word += secret_word[i] + ' '
        else:
            new_word += '_ '
    return new_word


def check_win(secret_word, old_letters_guessed):
    """
    Check if the player guessed the secret word
    :param secret_word:
    :param old_letters_guessed:
    :type secret_word: str
    :type old_letters_guessed: list
    :return:
    :rtype: bool
    """
    if '_' in show_hidden_word(secret_word, old_letters_guessed):
        return False
    return True


def print_hangman(num_of_tries):
    if num_of_tries in range(0, 7):
        print(HANGMAN_PHOTOS[num_of_tries])
    else:
        print("invalid number of guesses")


def choose_word(file_path, index):
    """
    The function choose a word form the text file given to it.
    :param file_path: path to a text file containing words separated by spaces
    :param index: position of a certain word in the file
    :type file_path: str
    :type index: int
    :return: returns a tuple consisting
    of two elements in the following order:
    (1) the number of different words in the file
    (2) a word in the position
    :rtype: tuple
    """
    with open(file_path, 'r') as words_file:
        words_ls = words_file.read().split(' ')
    i_word = words_ls[(index - 1) % len(words_ls)]
    words_ls = list(dict.fromkeys(words_ls))
    return len(words_ls), i_word


def print_welcome_screen():
    """
    The function print the welcome screen of the game.
    :return: None
    """
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def show_victory_screen():
    """
    The function print the victory screen of the game.
    :return: None
    """
    print("""
            .::^~~!!7:           ^^:.         .^!7??????7!^.     !PJ?^     :5YJ7!^.                 
          JBYYYYYYYYY5   :!^    PGYYYJ7!^. .!JYYYYYYYYYYYYYY7:   Y&YY5J!.  .&BYYYYYJ?!~.            
          ~&BJJJJJJJJ57 !B55^  Y#JJJJJYYYPYP5JJJJJJJJJJJJJJJY5?. Y&JJJJYY?^ Y@JJJJJJJYP~            
           ~@GJJJJJJJJ5YBYJJ5.?&JJJJJJJJG&PJJJJJJJJJJJJJJJJJJJYY Y&JJJJJJJYJJ@PJJJJJJJ5~            
            !@P???????JPJ???JP&Y??????JP@P?????????JJ??????????Y?J&????????JJ5P???????5~            
             ?@5?????????????JY??????JYY&?????????YJYBP?????????Y5&???????????????????Y~            
              J@Y???????????????????JY.J&????????Y7  ^&P????????Y5&???????????????????Y~            
               Y@J7777777?J77777777?Y. 7@J7777777?J. :#57777777?YY&777777777YJ77777777Y~            
                P&?77777?P&Y777777?J.  .B#77777777???JJ77777777Y^J&7777777775#GJ777777Y~            
                 G#77777Y.7@57777?J.    :B#?!7777777777777777?J^ Y&777777777J!7BGJ7777J~            
                 .BB7!7Y:  !&P!!?J.       J#P?!!!!!!!!!!!!7??!.  Y#!!!!!!!!!?7 .7BBJ!!J~            
                  :#B7Y:    ^#G??          .?PP5Y??777????7^.    Y&!!!!777??J?    7GBJJ~            
                   ^G?:      :J~              .~!7777!~^:        ?BJ???77!!~^.      !PJ:""")


def show_loss_screen():
    """
    The function print the loss screen of the game.
    :return: None
    """
    print("""
            . ......              .:^^^^:.              ...::::..           ..::::..               
          :5YJJJJJJY:          :~?JYYYYYYYYJ?~.      .^!?JJYYYYYYJ?!^   .^!7JYYYYYYYJJ7~.           
          :&5JJJJJJ5^        ^J5YYJJJJJJJJJJYYY!.  !JYYYYJJJJJJJJJY5! ^?YYYYJJJJJJJJJJ5J.           
          :&5JJJJJJ5^      .JPYJJJJJJJJJJJJJJJJYJ:YGJJJJJJJJYY5JJYY^ 7BYJJJJJJJYY5YJJY!             
          .#5?JJJJ?Y^      YG????JJ??JJ????JJ???J5&Y????JJ?YJ?P#5?.  BG???JJJJYY7J#PY^              
          .B5??????Y:     ^&J???????JJYP5????????5PB5J?????????YY?7~.!BPY?????????JYJ7!:            
           BP??????Y~:^^^^?&????????J. ~#57??????Y^^?Y5555YJ???????JJ^.7Y5555YYJ??????JJ!           
           GP777777???????Y@J7777777J^.:BY7777777Y. !J?~^~!J#J777777?Y.:JJ!^^~7B57777777Y~          
           PP7777777777777JG#?7777777?7??7777777J~ ?G?7?7!!?J77777777J7GJ7??7!7J?7777777J7          
           5G7777777777777J^J#J!!!7777777777!7??~ YP77777777!7777777?PG?7777777!77777777J:          
           YB!!!!!!!!!!!!!J^ ~PGY?!!!!!!!!!7??~. 5G!!!!!!!!!!!!!!!775#?!!!!!!!!!!!!!!7?7:           
           ?B?JJJJJJ?J?????:   ^?YYYJJJ???7~:.  .!Y55J?77!!!77777!^.^J55Y?777!!!77777~:             
           .::::..........        ..::::..         .^!7???777!^:.     .:~7????77!~:. """)


def main():
    print_welcome_screen()
    old_letters_guessed = []
    num_of_tries = 0
    file_path = input("Enter file path: ")
    word_index = int(input("Enter index: "))
    print("Let’s start!")
    p, secret_word = choose_word(file_path, word_index)
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    won = False
    while num_of_tries < MAX_TRIES and not won:
        letter_guessed = input("Guess a letter: ")
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed.lower() in secret_word:
                won = check_win(secret_word, old_letters_guessed)
            else:
                num_of_tries += 1
                print_hangman(num_of_tries)
            print(show_hidden_word(secret_word, old_letters_guessed))

    if won:
        show_victory_screen()
    else:
        show_loss_screen()


if __name__ == '__main__':
    main()
