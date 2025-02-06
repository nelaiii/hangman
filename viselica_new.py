from random import *


def select_word(dict):
    print("Выберите категорию из: животные (1), продукты (2), фрукты (3), транспорт (4), цвета (5)")
    categ = input()
    levels = ['light', 'middle', 'hard']
    categs = ['животные', 'продукты', 'фрукты', 'транспорт', 'цвета']
    if not categ.isdigit() or int(categ) < 1 or int(categ) > 5:
        print("Некорректный выбор категории. Выбрана категория по умолчанию: животные.")
        categ = 1
    else:
        categ = int(categ)

    print("Выберите сложность: light (1), middle (2), hard (3)")
    level = input()
    if not level.isdigit() or int(level) < 1 or int(level) > 3:
        print("Некорректный выбор сложности. Выбрана сложность по умолчанию: light.")
        level = 1
    else:
        level = int(level)

    word_list = dict[categ - 1]
    word_list.sort(key=lambda word: (len(word), word))
    if level == 1:
        words = word_list[:3]
    elif level == 2:
        words = word_list[3:6]
    else:
        words = word_list[6:]

    word = choice(words)
    print(f"Выбранная категория: {categs[categ - 1]}")
    print(f"Выбранная сложность: {levels[level - 1]}")
    return word


def gallows(mistakes):
    gallow = [
        """
         ------
          |    
          |
          |
          |
          |
        ----------
        """,
        """
         ------
          |    |
          |
          |
          |
          |
        ----------
        """,
        """
         ------
          |    |
          |    0
          |
          |
          |
        ----------
        """,
        """
         ------
          |    |
          |    0
          |    |
          | 
          |      
        ----------
        """,
        """
         ------
          |    |
          |    0
          |   /|
          |   
          |     
        ----------
        """,
        """
         ------
          |    |
          |    0
          |   /|\\
          |   
          |       
        ----------
        """,
        """
         ------
          |    |
          |    0
          |   /|\\
          |   /
          |     
        ----------
        """,
        """
         ------
          |    |
          |    0
          |   /|\\
          |   / \\
          |    
        ----------
        """
    ]
    return gallow[min(mistakes, len(gallow) - 1)]


def correct(guessed_word, letter, word, flag):
    for i in range(len(word)):
        if letter == word[i]:
            guessed_word[i] = letter
    if '_' not in guessed_word:
        print(f"Победа! Вы угадали слово: {''.join(guessed_word)} 🎉")
        return True
    return flag


def check_letter(letter, word, mistakes, guessed_word, flag, used_letters):
    if letter in used_letters:
        print("Вы уже вводили эту букву! Попробуйте другую.")
        return flag, mistakes, False
    used_letters.add(letter)
    if letter in word:
        print("Верно! Вы угадали букву.")
        return correct(guessed_word, letter, word, flag), mistakes, False
    else:
        print("Неверно! Такой буквы нет.")
        mistakes += 1
    return flag, mistakes, True


dict = [
    ['dog', 'elephant', 'rhinoceros', 'cat', 'lion', 'tiger', 'zebra', 'koala', 'panda'],
    ['apple', 'cabbage', 'asparagus', 'potato', 'carrot', 'tomato', 'broccoli', 'pumpkin', 'spinach'],
    ['banana', 'pear', 'orange', 'peach', 'grape', 'kiwi', 'mango', 'pomegranate', 'papaya'],
    ['car', 'bus', 'bicycle', 'scooter', 'motorcycle', 'trolleybus', 'helicopter', 'ship', 'submarine'],
    ['red', 'blue', 'green', 'yellow', 'orange', 'violet', 'turquoise', 'carmin', 'indigo']
]

flag = 0
word = select_word(dict)
guessed_word = ["_"] * len(word)
attempts = len(word) + len(word) // 3
mistakes = 0
used_letters = set()

while not flag and attempts:
    print(gallows(mistakes))
    print("Текущее слово: ", ' '.join(guessed_word))
    print(f"Осталось попыток: {attempts}")
    print(f"Использованные буквы: {', '.join(sorted(used_letters))}")
    letter = input("Введите букву: ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print("ЭТО НЕ 1 БУКВА!!! Пожалуйста, введите одну букву.")
        continue
    flag, mistakes, attempt_used = check_letter(letter, word, mistakes, guessed_word, flag, used_letters)
    if attempt_used:
        attempts -= 1

if attempts == 0 and not flag:
    print(f"Игра окончена! Загаданное слово было: {word}.")
