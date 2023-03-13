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

        self.strings = ''       # рабочий буфер приложения
        self.stringsLower = ''  # буфер для приведения слов к нижнему регистру (map)
        self.wordsArray = []    # список слов
        self.uniqueWords = []   # список всех слов без повторения
        self.baseWords = []     # список для определения количества разных слов в тексте
        self.frqDict = dict()   # frequency dictionary частотный словарь
        self.setWords = set()   # множество для определения количества разных слов в тексте
        self.substrLen = substrLen


    # из txtArr в sthbngs. Форматирование буфера строк txtArr:
    # каждая строка из txtArr разбивается на
    # фрагменты размером substrLen. В конец каждого фрагмента,
    # если его длина равна substrLen записывается символ '\n'
    def txtFormat(self):

        for i in range(0, len(self.txtArr)):

            # строка текстового буфера txtArr
            strTxt = self.txtArr[i]

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
                if q > 0 and q >= self.substrLen and strTxt[j] == ' ':
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

    # сформировать list со словами
    def splitRunner(self):
        # копия рабочего буфера приложения
        buff = str(self.strings)
        # разделение строки по разделителю 'по умолчанию' (пробелу)

        buff = buff.split()

        # ================================================================
        self.baseWords = buff.copy()  # подготовка списка для определения
                                      # количества разных слов в тексте
                                      # для метода diffRunner
        # ================================================================

        for word in buff:
            if word not in self.uniqueWords:
                # подготовка списка для определения количества разных слов в тексте (set)
                self.uniqueWords.append(word)
                print(f'{word} =====>')
            else:
                print(f'{word} <-----')

        print(self.uniqueWords)

    # привести все слова к нижнему регистру (map) с применением map ======
    def lowerRunner(self):

        # строка - список
        buff = self.strings.split()

        # перевод к нижнему регистру
        for i in range(len(buff)):
            buff[i] = buff[i].lower()

        # сборка строки из списка приведённых слов с применением функции map
        self.stringsLower = ' '.join(map(str, buff))
        print(self.stringsLower)

    # из list в dict, ключами которого являются слова, ===================
    # значениями -  количество их появления
    def dictRunner(self):

        words = []
        for i in range(0, len(self.uniqueWords)):
            words.append(self.uniqueWords[i].lower())

        # инициализация словаря ==========================================
        self.frqDict = dict.fromkeys(words, 0)

        # копия рабочего буфера приложения
        buff = str(self.stringsLower)
        # разделение строки по разделителю 'по умолчанию' (пробелу)
        buff = buff.split()

        # заполнение значений словаря ====================================
        for i in range(0, len(buff)):
            key = buff[i]
            self.frqDict[key] += 1

        print(self.frqDict)

    # вывести 5 наиболее часто встречающихся слов (sort) =================
    def freqStrRunner(self):
        freqArr = []
        # копия рабочего буфера приложения
        buff = str(self.strings)
        # разделение строки по разделителю 'по умолчанию' (пробелу)
        buff = buff.split()

        for w in self.uniqueWords:
            n = buff.count(w)
            if n == 0:
                print(w)
            freqArr.append([n, w])

        freqArr.sort(reverse=True)
        print(freqArr)

        res = []
        n = 0
        nFreq = len(freqArr)
        for freq in freqArr:
            if n < 5:
                if freq[0] < nFreq:
                    nFreq = freq[0]
                    n += 1
                res.append(freq)
            elif n == 5 and freq[0] == nFreq:
                res.append(freq)
            else:
                break

        # вывод 5 наиболее часто встречающихся слов
        n = 0
        print(f'~~~~~{n}~~~~~')
        nFreq = res[0][0]
        for elem in res:
            if elem[0] < nFreq:
                nFreq = elem[0]
                n += 1
                print(f'~~~~~{n}~~~~~')
            print(elem)
        print('~~~~~~~~~~~~~~~~~~~~~~')

    # вывести количество разных слов в тексте (set) ======================
    def diffRunner(self):

        self.setWords = set(self.baseWords)  # сформирован в методе splitRunner
        # print(self.setWords)
        print(f'full quantity: {len(self.baseWords)} - different quantity: {len(self.setWords)}')


def DoIt(name, substrLen):
    pars = txtParser(name, substrLen)

    print('\n*****txtFormat*************************************************************')
    pars.txtFormat()
    print('\n*****signDelete************************************************************')
    pars.signDelete()
    print('\n*****splitRunner***********************************************************')
    pars.splitRunner()
    print('\n*****lowerRunner***********************************************************')
    pars.lowerRunner()
    print('\n*****dictRunner*************************************************************')
    pars.dictRunner()
    print('\n*****freqStrRunner**********************************************************')
    pars.freqStrRunner()
    print('\n*****diffRunner*************************************************************')
    pars.diffRunner()
    print('\n****************************************************************************')

    pars.fileIn.close()

def main(name, substrLen):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}\n')  # Press Ctrl+F8 to toggle the breakpoint.
    DoIt(name, substrLen)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main("C:\\PythonDrom\\Texts_2022\\InputDuate.txt", 90)






