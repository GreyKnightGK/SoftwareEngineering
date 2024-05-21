from os.path import dirname
import re

with open(dirname(__file__) + '\\input.txt', 'r') as file:
    forbiddenWords = file.read().split(' ')

text = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!'
for word in forbiddenWords:
    text = re.sub(word, '*' * len(word), text, flags=re.IGNORECASE)

print(text)