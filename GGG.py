from tkinter import *
from _collections import OrderedDict


class App:
    def __init__(self):
        self.root = Tk()
        self.block_size = IntVar()
        self.current_column_step = IntVar()
        self.block_size.set(3)
        self.isDecode = False

    """Увеличиаем размер блока"""
    def update_block_size(self):
        self.block_size.set(self.spin.get());

    """Выделяем блок мышкой"""
    def markArea(self, event):
        # Если есть таблица какая-нибудь
        if (self.isDecode and event.x > 30):
            self.firstCanvas.delete("hello")
            # Надо выделить область по которой кликнули мышкой
            column_size = 270 // self.block_size.get()
            # определяем в какой мы колонке
            our_column = event.x // column_size;
            # выделяем
            self.firstCanvas.create_rectangle(40 + our_column * column_size, 25,
                                              column_size + column_size * our_column + 20, 30 + 15 * len(self.table[0]),
                                              outline="#ff0000", tags="hello")
            self.marked = our_column
            # Передаем данные полученные из частотного анализа
            self.draw_data(self.marked)
            if (our_column < self.block_size.get()):
                # передаем в ползунок
                self.current_column_step.set(self.steps[self.marked])
    """"""
    def peredecode(self, event):
        if (self.isDecode and self.marked < self.block_size.get()):
            self.steps[self.marked] = self.current_column_step.get()
            # Теперь перерисовываем
            self.create_message(self.steps, self.table)

    def draw_data(self, item):
        self.fq.delete("all")
        column = 0
        j = 0
        for (i, letter) in enumerate(self.super_dicts[item].keys()):
            if (10 + 15 * j > 350):
                column += 1
                j = 0
            self.fq.create_text(20 + 30 * column, 10 + 15 * j,
                                text=letter + ": " + str(self.super_dicts[item].get(letter)))
            j += 1

    def makeWidgets(self):
        self.firstFrame = Frame(self.root)
        self.firstFrame.pack(side=LEFT, anchor="nw", padx=10, pady=10)
        Label(self.firstFrame, text="Таблица для исходного сообщения").pack()
        self.firstAlterFrame = Frame(self.firstFrame)
        self.firstAlterFrame.pack()
        self.firstCanvas = Canvas(self.firstAlterFrame, width=300, height=500, bg="#ffffff")
        self.firstCanvas.bind("<Button-1>", self.markArea)
        self.firstCanvas.pack(side=LEFT)
        self.firstCanvasScroll = Scrollbar(self.firstAlterFrame, orient='vertical', command=self.firstCanvas.yview)
        self.firstCanvasScroll.pack(side=RIGHT, fill=Y, expand=True)
        self.firstCanvas.configure(yscrollcommand=self.firstCanvasScroll.set)
        Label(self.firstFrame, text="Введите исходное сообщение").pack(pady=10)
        self.firstText = Text(self.firstFrame, width=37, height=10)
        self.firstText.pack()

        self.secondFrame = Frame(self.root)
        self.secondFrame.pack(side=LEFT, anchor="n", padx=10, pady=10)
        Label(self.secondFrame, text="Таблица для конечного сообщения").pack()
        self.secondAlterFrame = Frame(self.secondFrame)
        self.secondAlterFrame.pack()
        self.secondCanvas = Canvas(self.secondAlterFrame, width=300, height=500, bg="#ffffff")
        self.secondCanvas.pack(side=LEFT)
        self.secondCanvasScroll = Scrollbar(self.secondAlterFrame, orient='vertical', command=self.secondCanvas.yview)
        self.secondCanvasScroll.pack(side=RIGHT, fill=Y, expand=True)
        self.secondCanvas.configure(yscrollcommand=self.secondCanvasScroll.set)
        Label(self.secondFrame, text="Конечный результат").pack(pady=10)
        self.secondText = Text(self.secondFrame, width=37, height=10)
        self.secondText.pack()

        self.lastFrame = Frame(self.root)
        self.lastFrame.pack(side=LEFT, anchor="n", padx=10, pady=10)
        Label(self.lastFrame, text="Панель управления").pack()
        Label(self.lastFrame, text="Размер блока").pack(pady=10)
        self.spin = Spinbox(self.lastFrame, from_=0, textvariable=self.block_size, to=10,
                            command=self.update_block_size)
        self.spin.pack()
        Label(self.lastFrame, text="Частотный анализ").pack(pady=10)
        self.fq = Canvas(self.lastFrame, width=150, height=400, bg="#ffffff")
        self.fq.pack()
        # Наш ползунок
        Label(self.lastFrame, text="Ручная корректировка").pack(pady=10)
        self.scale = Scale(self.lastFrame, from_=0, to=33, length=150, tickinterval=6, orient='horizontal',
                           showvalue=YES, variable=self.current_column_step, command=self.peredecode)
        self.scale.pack()
        Button(self.lastFrame, text="Расшифровать!", width=15, height=5, command=self.decode).pack(pady=20)

    """Инициализирукм гуй"""
    def start(self):
        self.root.title("Лабораторная работа номер 2")
        # self.root.geometry("900x500")
        self.makeWidgets()
        self.root.mainloop()

    def decode(self):
        self.isDecode = True
        self.super_dicts = []
        # Берем сообщение из текстового блока и загоняем в столбец по размеру блока
        self.table = ['' for i in range(self.block_size.get())]
        message = "лькпызйнлфю гйдгносугт гщюя ятьапчягирпшнаяссайуапйюнгомоидаю тэпжтдмумоидаязт дниъаэню ннатаыдтънуююаы аэппясп таянт гщюяжзцнзцн думуьбгнноцяньвф ясучб ыаякпфмьуяиогбдзйнйп нсидаряоуйп нсифаякфд вягнжооцй дмймпчят друмйносубье я яйыгйрзеа мймьуятэнтьаоьруцяп гжщыоьвпнлфю гйюаьаморуйянапбрыйыъцн мснсцсньбацжфд ж яньгжщзйнопщтшумоидаэтуулаы вщэеумймяиоярьбжтдоцдннпжокэыъцнлфю гйдгряйнзтэнмйжфусаксйнлптдмцяаэпйносьдл зсьббызйнмпръцн мснсцсньбатк нпжедоцюах еоцаьоуцлйх чцзацясоррюдеукжымпснашно ппщю мю"
        for (i, letter) in enumerate(message):
            self.table[i % self.block_size.get()] += letter
        self.draw(self.firstCanvas, self.table)
        # Теперь мы должны сделать словари с частотными анализами для каждой колонки ох, говорю я
        self.steps = [self.analis(self.table[i]) for i in range(self.block_size.get())]
        # Так, у нас массив сдвигов, нам надо каждый столбец сдвинуть на это число
        # Нам нужен не только массив сдвигов, но и словари с частоными анализами
        # Теперь берем каждую строку и сдвигаем на сдвиги, но это все в отдельной функции
        self.create_message(self.steps, self.table)

    """Собираем исходное сообщение"""
    def create_message(self, steps, table):
        self.alterTable = ['' for i in table]
        for i in range(len(table)):
            self.alterTable[i] = App.caesar(table[i], 33 - steps[i])
        self.draw(self.secondCanvas, self.alterTable)
        out = ''
        for i in range(len(self.alterTable[0])):
            for j in range(self.block_size.get()):
                try:
                    out += self.alterTable[j][i]
                except IndexError:
                    out += ''
        self.secondText.delete('1.0', "end")
        self.secondText.insert('1.0', out)

    """Функция для сдвига по шифру цезаря Можно конечно в одну строчку через bytes.translate, но этот вариант мне больше нравится"""
    def caesar(message, step):
        alpha = [' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        res = []
        for item in range(len(alpha)):
            if item + step >= len(alpha):
                res += alpha[item + step - len(alpha)]
            elif item + step < 0:
                res += alpha[len(alpha) - item + step]
            else:
                res += alpha[item + step]
        wow = list(zip(alpha, res))
        msq = ''
        for letter in message:
            for item in wow:
                if letter == item[0]:
                    msq += item[1]
                    break
            else:
                msq += letter
        return msq

    """Анализ частотностит символов"""
    def analis(self, column):
        alphabet = " абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.dicts = {letter: 0 for letter in alphabet}
        dict_step = {letter: i for (i, letter) in enumerate(alphabet)}
        for i in column:
            self.dicts[i] += 1
        self.dicts = OrderedDict(sorted(self.dicts.items(), key=lambda t: -t[1]))
        self.super_dicts.append(self.dicts)
        azaza = list(self.dicts.keys())
        return dict_step.get(azaza[0])

    """Заполнянм кавас столбиками с буквами"""
    def draw(self, obj, table):
        # наша исходная таблица готова, нам необходимо теперь заполнить канвас
        obj.delete("all")
        obj.create_line(30, 0, 30, 30 + len(table[0]) * 15, fill="#000000")
        obj.create_line(30, 20, 300, 20, fill="#000000")
        # Делим оставшееся пространство для того что бы положить туда столбцы
        column_size = 270 // self.block_size.get()
        # теперь в цикле раставляем цифры и сообщение
        for i in range(self.block_size.get()):
            obj.create_text(column_size / 1.2 + column_size * i, 10, text=str(i + 1))
            for (j, letter) in enumerate(table[i]):
                obj.create_text(column_size / 1.2 + column_size * i, 30 + j * 15, text=letter)
                # Нумерация строк
        for i in range(len(table[0])):
            obj.create_text(10, 30 + i * 15, text=str(i + 1))
        obj.configure(scrollregion=obj.bbox("all"))


if __name__ == "__main__":
    app = App()
    app.start()
