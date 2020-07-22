import os
import random


# очистка экрана
def cls(): os.system('cls')


# вспомогательные переменные
words = ("woman", "student", "teacher", "president", "motherbook", "computer",
         "place", "picture", "bottle", "table", "chair", "rabbit", "elephant",
         "chicken", "horse")
hidden_word = random.choice(words)
length = len(hidden_word)
hidden_word_length = length
field = '-'
mistake = 0
typed_letters = []
list_of_hidden_letters = list(hidden_word)

# скрытые буквы
while length > 1:
    part_of_the_field = '-'
    field = field + part_of_the_field
    length -= 1
list_field = list(field)

# основная часть в игре
while True:
    guessed_letters = 0
    number_of_entries = 0

    # рисунок виселицы
    if mistake == 0:
        print('\n |\n |\n |\n |\n |\n |\n |\n |\n------------------\n')
    elif mistake == 1:
        print('\n |--------\n |\n |\n |\n |\n |\n |\n |\n------------------\n')
    elif mistake == 2:
        print('\n |--------\n |     |\n |     |\n |\n |\n |\n |\n |'
              '\n------------------\n')
    elif mistake == 3:
        print('\n |--------\n |     |\n |     |\n |     O\n |\n |\n |\n |'
              '\n------------------\n')
    elif mistake == 4:
        print('\n |--------\n |     |\n |     |\n |     O\n |     |\n |\n |\n'
              ' |\n------------------\n')
    elif mistake == 5:
        print('\n |--------\n |     |\n |     |\n |     O\n |    /| \n |\n |\n'
              ' |\n------------------\n')
    elif mistake == 6:
        print('\n |--------\n |     |\n |     |\n |     O\n |    /|\\ \n |\n'
              ' |\n |\n------------------\n')
    elif mistake == 7:
        print('\n |--------\n |     |\n |     |\n |     O\n |    /|\\ \n'
              ' |    /\n |\n |\n------------------\n')

    # загаданное слово со скрытыми и открытыми буквами
    print("\nThe word is made up: ")
    for p in list_field:
        print(p, end='')

    # ввод буквы и проверка eё на правильность
    input_letter = input("\nEnter letter ")
    typed_letters.append(input_letter)
    cls()
    if len(input_letter) != 1 or typed_letters.count(input_letter) == 2:
        typed_letters.remove(input_letter)
        number_of_entries += 1
        mistake -= 1

    # проверка есть ли буква в слове и вывод её
    if number_of_entries == 0:
        cell = -1
        repetitions_in_a_word = 0
        for i in hidden_word:
            cell += 1
            if i == input_letter:
                del list_field[cell]
                list_field.insert(cell, list_of_hidden_letters[cell])
                if repetitions_in_a_word == 0:
                    print('\nYou opened the letter', i)
                repetitions_in_a_word += 1
                hidden_word_length -= 1
                guessed_letters += 1
    print('\nYou have already entered the letters:', typed_letters)

    # выигрыш
    if hidden_word_length == 0:
        cls()
        print('\nYou win\nThe hidden word:', hidden_word)
        break

    # отсутствие введенной буквы в слове
    if guessed_letters == 0:
        mistake += 1
        cls()
        print('\nThere is no letter in the string.'
              '\n\nYou have already entered the letters:', typed_letters)

        # проигрыш
        if mistake == 8:
            cls()
            print('\nThere is no letter in the string.'
                  '\n |--------\n |     |\n |     |\n |     O\n |    /|\\'
                  '\n |    / \\ \n |\n |\n------------------'
                  '\nSorry. You were hanged.\nThe hidden word:', hidden_word)
            break
