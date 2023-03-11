"""
1. методами строк очистить текст от знаков препинания;
2. сформировать list со словами (split);
3. привести все слова к нижнему регистру (map);
4. получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
5. вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

"""
class txtParser:     # the program for parsing

    # список нежелательных символов (знаки препинания, скобки и т.п.)
    badSignes = ['.', ',', ';', ':', '(', ')', '«', '»']
    def __init__(self, fnameIn, substrLen):
        self.fileIn = open(fnameIn, 'r', encoding='utf16')
        self.txtArr = self.fileIn.readlines()   # прочитать ВСЕ строки в файле в буфер (массив)
                                                # txtArr, который состоит из len(txtArr) строк,
                                                # считая и пустые, которые содержат символ '\n'
                                                # и больше ничего

        self.strings = ''   # рабочий буфер приложения
        self.wordsArray = []  # список слов
        self.uniqueWords = []
        self.substrLen = substrLen
        # self.txtFormat(txtArr, substrLen)
        # self.signDelete()

    # из txtArr в sthbngs. Форматирование буфера строк txtArr:
    # каждая строка из txtArr разбивается на
    # фрагменты размером substrLen. В конец каждого фрагмента,
    # если его длина равна substrLen записывается символ '\n'
    def txtFormat(self, txtArr, substrLen):

        for i in range(0, len(txtArr)):

            # строка текстового буфера txtArr
            strTxt = txtArr[i]

            # пропуск строк, которые состоят только из '\n'
            if strTxt == '\n':
                continue

            q = 0
            for j in range(0, len(strTxt)):
                # посимвольный перебор строки strTxt и
                # определение очередного места вставки '\n'
                # в self.strings
                self.strings = self.strings + strTxt[j]
                q += 1
                if q > 0 and q >= substrLen and strTxt[j] == ' ':
                    self.strings = self.strings + '\n'
                    q = 0

        print(self.strings)

    # удаление нежелательных символов
    def signDelete(self):

        buff = ''
        for i in range(0, len(self.strings)):
            signX = self.strings[i]
            for s in txtParser.badSignes:  # цикл по списку нежелательных символов
                if signX == s:  # нежелательный символ в строке
                    signX = ''  # заменяется пустым
                    break

            buff = buff + signX  # проверенные символы записываются в буфер
        self.strings = buff  # зачищенный буфер записывается в исходную строку

        print(self.strings)  # печать результата

    def splitRunner(self):
        # копия рабочего буфера приложения
        buff = str(self.strings)
        # разделение строки по разделителю 'по умолчанию' (пробелу)
        buff = buff.split()

        for word in buff:
            if word not in self.uniqueWords:
                self.uniqueWords.append(word)
                print(f'{word} ==>')
            else:
                print(f'{word} <--')

        print(self.uniqueWords)


def DoIt(name, substrLen):
    pars = txtParser(name, substrLen)

    pars.txtFormat(pars.txtArr, substrLen)
    pars.signDelete()
    pars.splitRunner()

    pars.fileIn.close()

def main(name, substrLen):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}\n')  # Press Ctrl+F8 to toggle the breakpoint.
    DoIt(name, substrLen)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main("C:\\PythonDrom\\Texts_2022\\InputDuate.txt", 90)



