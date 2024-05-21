from os.path import dirname

dirName = dirname(__file__) + '\\'
inputFiles = ('file1.txt', 'file2.txt', 'file3.txt')

with open(dirName + 'output.txt', 'a+') as outputFile:
    for file in inputFiles:
        with open(dirName + file, 'r') as inputFile:
            text = inputFile.read()
        outputFile.write(text + '\n')
        print(f'Текст файла {file}:\n{text}\n')
    outputFile.seek(0)
    print(f'Текст объединенного файла:\n{outputFile.read()}')