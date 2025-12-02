from random import  random, choice
from string import ascii_letters

def gen_sentence(length = 50, space_prob = 0.15, chars = ascii_letters.lower()):
    line = ''.join(' ' if random() < space_prob else choice(chars) for _ in range(length)).capitalize() + '.'
    while '  ' in line:
        line = line.replace('  ', ' ')
    return line


def reverse(line):
    return line[::-1]

def count_words(line):
    return len(line.split())

def is_polindrom(word):
    return word == word[::-1]

sentence = gen_sentence()
number_words = count_words(sentence)
word = sentence.split()[0].lower()
is_pol = is_polindrom(word)

print(f'Случайное предложение: {sentence}')
print(f'Число слов: {number_words}')
print(f'Является ли первое слово предложения полиндромом: {['НЕТ', 'ДА'][is_polindrom(word)]}')