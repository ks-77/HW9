"""
HW9
Savchenko Kirill
"""

from lorem_text import lorem
import re
import random


# 1-2


def random_text_creator(words, paragraphs):
    text = ""
    for _ in range(paragraphs):
        paragraph = ''.join(lorem.words(words))
        text += paragraph + '\n'
    return text.strip()


random_text = random_text_creator(random.randint(7, 12), random.randint(2, 4))
print(f"TEXT:\n{random_text}\n")

with open("randomtext.txt", "w") as rantxt:
    rantxt.write(random_text)

with open("randomtext.txt", "r") as rantxt:
    textline = rantxt.read().split()
    words7_list = [word for word in textline if re.findall(r'\w{7,}', word)]
    print(f"Words quantity: {len(textline)} words")

with open("words7.txt", "w") as words7:
    words7.write('\n'.join(words7_list))

# 3

rawtxt = ("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer\n"
          "The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles,\n"
          "And by opposing end them? To die: to sleep; No more; and by a sleep to say we end \n"
          "The heart-ache and the thousand natural shocks That flesh is heir to,\n"
          "'tis a consummation Devoutly to be wish'd. To die, to sleep")

print(f"\nTEXT:\n{rawtxt}")

with open("text.txt", "w") as init_text:
    init_text.write(rawtxt)

with open("text.txt", "r") as init_text:
    textstr = init_text.read()

word_cens = input("What word you want to censor: ")
text_cens = textstr.replace(word_cens, '*' * len(word_cens))
cens_count = textstr.count(word_cens)
print(f"{cens_count} replaces of word '{word_cens}'")

with open("censored_text.txt", "w") as cens_text:
    cens_text.write(text_cens)
