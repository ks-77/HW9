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
