#!/usr/bin/env python3
import sys


class DigitsToWords:
    def __init__(self, number_to_word):
        self.number_to_word = number_to_word

    def __repr__(self):
        return "Convert number [{}] to word: {}" \
            .format(str(self.num_to_word),
                    str(self.convert_to_word(self.num_to_word)))

    @property
    def num_to_word(self):
        return self.number_to_word

    @num_to_word.setter
    def num_to_word(self, value):
        self.number_to_word = value

    @staticmethod
    def detect_word_case(num):
        word_endings = []
        if num < 1000000:
            num = num // 1000
            word_endings = [' тысяча ', ' тысячи ', ' тысяч ']
        if 1000000000 > num >= 1000000:
            num = num // 1000000
            word_endings = [' миллион ', ' миллиона ', ' миллионов ']
        if 1000000000000 > num >= 1000000000:
            num = num // 1000000000
            word_endings = [' миллиард ', ' миллиарда ', ' миллиардов ']
        if 1000000000000000 > num >= 1000000000000:
            num = num // 1000000000000
            word_endings = [' триллион ', ' триллиона ', ' триллионов ']
        num = num % 10 if (num % 100) > 20 else num % 20

        if num == 1:
            return word_endings[0]
        elif num == 2 or num == 3 or num == 4:
            return word_endings[1]
        else:
            return word_endings[2]

    def convert_to_word(self, num):
        converted_words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три',
                           4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь',
                           8: 'восемь', 9: 'девять', 10: 'десять',
                           11: 'одиннадцать', 12: 'двенадцать',
                           13: 'тринадцать', 14: 'четырнадцать',
                           15: 'пятнадцать', 16: 'шестнадцать',
                           17: 'семнадцать', 18: 'восемнадцать',
                           19: 'девятнадцать', 20: 'двадцать',
                           30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
                           60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
                           90: 'девяносто', 100: 'сто', 200: 'двести',
                           300: 'триста', 400: 'четыреста', 500: 'пятьсот',
                           600: 'щестьсот', 700: 'семьсот', 800: 'восемьсот',
                           900: 'девятсот'}
        kilo = 1000
        millions = kilo * 1000
        billions = millions * 1000
        trillions = billions * 1000

        if num < 0:
            return "Минус " + self.convert_to_word(-num)

        if num < 20:
            return converted_words[num]

        if num < 100:
            if num % 10 == 0:
                return converted_words[num]
            else:
                return converted_words[num // 10 * 10] + ' ' \
                       + self.convert_to_word(num % 10)

        if num < kilo:
            if num % 100 == 0:
                return converted_words[num]
            else:
                return converted_words[num // 100 * 100] + ' ' \
                       + self.convert_to_word(num % 100)

        if num < millions:
            if num % kilo == 0:
                return self.convert_to_word(num // kilo)\
                       + DigitsToWords.detect_word_case(num)
            else:
                return self.convert_to_word(num // kilo)\
                       + DigitsToWords.detect_word_case(num) \
                       + self.convert_to_word(num % kilo)

        if num < billions:
            if (num % millions) == 0:
                return self.convert_to_word(num // millions) \
                       + DigitsToWords.detect_word_case(num)
            else:
                return self.convert_to_word(num // millions) \
                       + DigitsToWords.detect_word_case(num) \
                       + self.convert_to_word(num % millions,)

        if num < trillions:
            if num % billions == 0:
                return self.convert_to_word(num // billions) \
                       + DigitsToWords.detect_word_case(num)
            else:
                return self.convert_to_word(num // billions) \
                       + DigitsToWords.detect_word_case(num) \
                       + self.convert_to_word(num % billions)

        if num % trillions == 0:
            return self.convert_to_word(num // trillions) \
                   + DigitsToWords.detect_word_case(num)
        else:
            return self.convert_to_word(num // trillions) \
                   + DigitsToWords.detect_word_case(num) \
                   + self.convert_to_word(num % trillions)


def get_arguments_data():
    if len(sys.argv) != 2:
        print("\n******* Digits to words converter *******\n"
              "Instructions for using program:\n"
              "Please enter two correct argument\n"
              "Note: arguments must be a positive numbers\n")
        sys.exit()
    else:
        return int(sys.argv[1])


def main():
    number_to_word = get_arguments_data()
    converter_obj = DigitsToWords(number_to_word)
    print(converter_obj)


if __name__ == '__main__':
    main()
