from os.path import dirname

def read_file(fileName):
    with open(dirname(__file__) + f'\\{fileName}', 'r', encoding='utf-8') as file:
        text = file.read().strip()

    if (len(text) == 0):
        raise ValueError()
    else:
        return text
    
files = ('Lab10_2_not_empty.txt', 'Lab10_2_empty.txt')

for file in files:
    try:
        print(f'{file}: {read_file(file)}')
    except ValueError:
        print (f'{file}: Файл пустой')