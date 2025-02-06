import random


class Gallows:
    def __init__(self, max_lives):
        self.max_lives = max_lives
        self.lives = 0
        self.stages = [
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

    def lose_life(self):
        self.lives += 1

    def is_alive(self):
        return self.lives < self.max_lives

    def display(self):
        return self.stages[self.lives]


class WordSelector:
    def __init__(self, word_dict):
        self.word_dict = word_dict

    def select_word(self):
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

        word_list = self.word_dict[categ - 1]
        word_list.sort(key=lambda word: (len(word), word))
        words = word_list[(level - 1) * 3: level * 3]
        word = random.choice(words)
        print(f"Выбранная категория: {categs[categ - 1]}")
        print(f"Выбранная сложность: {levels[level - 1]}")
        return word


class HangmanGame:
    def __init__(self, word_dict):
        self.word_selector = WordSelector(word_dict)
        self.word = ""
        self.guessed_word = []
        self.attempts = 0
        self.gallows = None
        self.used_letters = set()

    def start_game(self):
        self.word = self.word_selector.select_word()
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = len(self.word) + len(self.word) // 3
        self.gallows = Gallows(7)
        self.used_letters.clear()
        self.run_game()

    def run_game(self):
        while self.gallows.is_alive() and "_" in self.guessed_word and self.attempts > 0:
            print(self.gallows.display())
            print("Текущее слово: ", ' '.join(self.guessed_word))
            print(f"Осталось попыток: {self.attempts}")
            print(f"Использованные буквы: {', '.join(sorted(self.used_letters))}")
            letter = input("Введите букву: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("ЭТО НЕ 1 БУКВА!!! Пожалуйста, введите одну букву.")
                continue
            if letter in self.used_letters:
                print("Вы уже вводили эту букву! Попробуйте другую.")
                continue
            self.used_letters.add(letter)
            if letter in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.guessed_word[i] = letter
                print("Верно! Вы угадали букву.")
            else:
                print("Неверно! Такой буквы нет.")
                self.gallows.lose_life()
                self.attempts -= 1

        if "_" not in self.guessed_word:
            print(f"Победа! Вы угадали слово: {''.join(self.guessed_word)} 🎉")
        else:
            print(f"Игра окончена! Загаданное слово было: {self.word}.")


dict_words = [
    ['dog', 'elephant', 'rhinoceros', 'cat', 'lion', 'tiger', 'zebra', 'koala', 'panda'],
    ['apple', 'cabbage', 'asparagus', 'potato', 'carrot', 'tomato', 'broccoli', 'pumpkin', 'spinach'],
    ['banana', 'pear', 'orange', 'peach', 'grape', 'kiwi', 'mango', 'pomegranate', 'papaya'],
    ['car', 'bus', 'bicycle', 'scooter', 'motorcycle', 'trolleybus', 'helicopter', 'ship', 'submarine'],
    ['red', 'blue', 'green', 'yellow', 'orange', 'violet', 'turquoise', 'carmin', 'indigo']
]

game = HangmanGame(dict_words)
game.start_game()
