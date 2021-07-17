from kivy.properties import Clock
import random


ra = ""


def on_slider_value(self, widget):
    self.tm = int(widget.value) / - 100


def repeat_list(self):
    global ra
    list(ra)
    wlong = len(ra)
    for i in range(wlong):
        # print(list(ra)[i])
        if list(ra)[i] == "а":
            Clock.schedule_once(self.cl1, i * self.tm)
        if list(ra)[i] == "б":
            Clock.schedule_once(self.cl2, i * self.tm)
        if list(ra)[i] == "в":
            Clock.schedule_once(self.cl3, i * self.tm)
        if list(ra)[i] == "г":
            Clock.schedule_once(self.cl4, i * self.tm)
        if list(ra)[i] == "д":
            Clock.schedule_once(self.cl5, i * self.tm)
        if list(ra)[i] == "е":
            Clock.schedule_once(self.cl6, i * self.tm)
        if list(ra)[i] == "ж":
            Clock.schedule_once(self.cl7, i * self.tm)
        if list(ra)[i] == "з":
            Clock.schedule_once(self.cl8, i * self.tm)
        if list(ra)[i] == "и":
            Clock.schedule_once(self.cl9, i * self.tm)
        if list(ra)[i] == "й":
            Clock.schedule_once(self.cl10, i * self.tm)
        if list(ra)[i] == "к":
            Clock.schedule_once(self.cl11, i * self.tm)
        if list(ra)[i] == "л":
            Clock.schedule_once(self.cl12, i * self.tm)
        if list(ra)[i] == "м":
            Clock.schedule_once(self.cl13, i * self.tm)
        if list(ra)[i] == "н":
            Clock.schedule_once(self.cl14, i * self.tm)
        if list(ra)[i] == "о":
            Clock.schedule_once(self.cl15, i * self.tm)
        if list(ra)[i] == "п":
            Clock.schedule_once(self.cl16, i * self.tm)
        if list(ra)[i] == "р":
            Clock.schedule_once(self.cl17, i * self.tm)
        if list(ra)[i] == "с":
            Clock.schedule_once(self.cl18, i * self.tm)
        if list(ra)[i] == "т":
            Clock.schedule_once(self.cl19, i * self.tm)
        if list(ra)[i] == "у":
            Clock.schedule_once(self.cl20, i * self.tm)
        if list(ra)[i] == "ф":
            Clock.schedule_once(self.cl21, i * self.tm)
        if list(ra)[i] == "х":
            Clock.schedule_once(self.cl22, i * self.tm)
        if list(ra)[i] == "ц":
            Clock.schedule_once(self.cl23, i * self.tm)
        if list(ra)[i] == "ч":
            Clock.schedule_once(self.cl24, i * self.tm)
        if list(ra)[i] == "ш":
            Clock.schedule_once(self.cl25, i * self.tm)
        if list(ra)[i] == "щ":
            Clock.schedule_once(self.cl26, i * self.tm)
        if list(ra)[i] == "ъ":
            Clock.schedule_once(self.cl27, i * self.tm)
        if list(ra)[i] == "ы":
            Clock.schedule_once(self.cl28, i * self.tm)
        if list(ra)[i] == "ь":
            Clock.schedule_once(self.cl29, i * self.tm)
        if list(ra)[i] == "э":
            Clock.schedule_once(self.cl30, i * self.tm)
        if list(ra)[i] == "ю":
            Clock.schedule_once(self.cl31, i * self.tm)
        if list(ra)[i] == "я":
            Clock.schedule_once(self.cl32, i * self.tm)
        if list(ra)[i] == "_":
            Clock.schedule_once(self.cl33, i * self.tm)


def combination_list(self):
    a_file = open("combination.txt", "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    a_file.close()
    # print(list_of_lists)
    global ra
    ra = random.choice(line_list)
    # print(ra)
    list(ra)
    wlong = len(ra)
    for i in range(wlong):
        # print(list(ra)[i])
        if list(ra)[i] == "а":
            Clock.schedule_once(self.cl1, i * self.tm)
        if list(ra)[i] == "б":
            Clock.schedule_once(self.cl2, i * self.tm)
        if list(ra)[i] == "в":
            Clock.schedule_once(self.cl3, i * self.tm)
        if list(ra)[i] == "г":
            Clock.schedule_once(self.cl4, i * self.tm)
        if list(ra)[i] == "д":
            Clock.schedule_once(self.cl5, i * self.tm)
        if list(ra)[i] == "е":
            Clock.schedule_once(self.cl6, i * self.tm)
        if list(ra)[i] == "ж":
            Clock.schedule_once(self.cl7, i * self.tm)
        if list(ra)[i] == "з":
            Clock.schedule_once(self.cl8, i * self.tm)
        if list(ra)[i] == "и":
            Clock.schedule_once(self.cl9, i * self.tm)
        if list(ra)[i] == "й":
            Clock.schedule_once(self.cl10, i * self.tm)
        if list(ra)[i] == "к":
            Clock.schedule_once(self.cl11, i * self.tm)
        if list(ra)[i] == "л":
            Clock.schedule_once(self.cl12, i * self.tm)
        if list(ra)[i] == "м":
            Clock.schedule_once(self.cl13, i * self.tm)
        if list(ra)[i] == "н":
            Clock.schedule_once(self.cl14, i * self.tm)
        if list(ra)[i] == "о":
            Clock.schedule_once(self.cl15, i * self.tm)
        if list(ra)[i] == "п":
            Clock.schedule_once(self.cl16, i * self.tm)
        if list(ra)[i] == "р":
            Clock.schedule_once(self.cl17, i * self.tm)
        if list(ra)[i] == "с":
            Clock.schedule_once(self.cl18, i * self.tm)
        if list(ra)[i] == "т":
            Clock.schedule_once(self.cl19, i * self.tm)
        if list(ra)[i] == "у":
            Clock.schedule_once(self.cl20, i * self.tm)
        if list(ra)[i] == "ф":
            Clock.schedule_once(self.cl21, i * self.tm)
        if list(ra)[i] == "х":
            Clock.schedule_once(self.cl22, i * self.tm)
        if list(ra)[i] == "ц":
            Clock.schedule_once(self.cl23, i * self.tm)
        if list(ra)[i] == "ч":
            Clock.schedule_once(self.cl24, i * self.tm)
        if list(ra)[i] == "ш":
            Clock.schedule_once(self.cl25, i * self.tm)
        if list(ra)[i] == "щ":
            Clock.schedule_once(self.cl26, i * self.tm)
        if list(ra)[i] == "ъ":
            Clock.schedule_once(self.cl27, i * self.tm)
        if list(ra)[i] == "ы":
            Clock.schedule_once(self.cl28, i * self.tm)
        if list(ra)[i] == "ь":
            Clock.schedule_once(self.cl29, i * self.tm)
        if list(ra)[i] == "э":
            Clock.schedule_once(self.cl30, i * self.tm)
        if list(ra)[i] == "ю":
            Clock.schedule_once(self.cl31, i * self.tm)
        if list(ra)[i] == "я":
            Clock.schedule_once(self.cl32, i * self.tm)
        if list(ra)[i] == "_":
            Clock.schedule_once(self.cl33, i * self.tm)

def short_list(self):
    a_file = open("short.txt", "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    a_file.close()
    # print(list_of_lists)
    global ra
    ra = random.choice(line_list)
    # print(ra)
    list(ra)
    wlong = len(ra)
    for i in range(wlong):
        # print(list(ra)[i])
        if list(ra)[i] == "а":
            Clock.schedule_once(self.cl1, i * self.tm)
        if list(ra)[i] == "б":
            Clock.schedule_once(self.cl2, i * self.tm)
        if list(ra)[i] == "в":
            Clock.schedule_once(self.cl3, i * self.tm)
        if list(ra)[i] == "г":
            Clock.schedule_once(self.cl4, i * self.tm)
        if list(ra)[i] == "д":
            Clock.schedule_once(self.cl5, i * self.tm)
        if list(ra)[i] == "е":
            Clock.schedule_once(self.cl6, i * self.tm)
        if list(ra)[i] == "ж":
            Clock.schedule_once(self.cl7, i * self.tm)
        if list(ra)[i] == "з":
            Clock.schedule_once(self.cl8, i * self.tm)
        if list(ra)[i] == "и":
            Clock.schedule_once(self.cl9, i * self.tm)
        if list(ra)[i] == "й":
            Clock.schedule_once(self.cl10, i * self.tm)
        if list(ra)[i] == "к":
            Clock.schedule_once(self.cl11, i * self.tm)
        if list(ra)[i] == "л":
            Clock.schedule_once(self.cl12, i * self.tm)
        if list(ra)[i] == "м":
            Clock.schedule_once(self.cl13, i * self.tm)
        if list(ra)[i] == "н":
            Clock.schedule_once(self.cl14, i * self.tm)
        if list(ra)[i] == "о":
            Clock.schedule_once(self.cl15, i * self.tm)
        if list(ra)[i] == "п":
            Clock.schedule_once(self.cl16, i * self.tm)
        if list(ra)[i] == "р":
            Clock.schedule_once(self.cl17, i * self.tm)
        if list(ra)[i] == "с":
            Clock.schedule_once(self.cl18, i * self.tm)
        if list(ra)[i] == "т":
            Clock.schedule_once(self.cl19, i * self.tm)
        if list(ra)[i] == "у":
            Clock.schedule_once(self.cl20, i * self.tm)
        if list(ra)[i] == "ф":
            Clock.schedule_once(self.cl21, i * self.tm)
        if list(ra)[i] == "х":
            Clock.schedule_once(self.cl22, i * self.tm)
        if list(ra)[i] == "ц":
            Clock.schedule_once(self.cl23, i * self.tm)
        if list(ra)[i] == "ч":
            Clock.schedule_once(self.cl24, i * self.tm)
        if list(ra)[i] == "ш":
            Clock.schedule_once(self.cl25, i * self.tm)
        if list(ra)[i] == "щ":
            Clock.schedule_once(self.cl26, i * self.tm)
        if list(ra)[i] == "ъ":
            Clock.schedule_once(self.cl27, i * self.tm)
        if list(ra)[i] == "ы":
            Clock.schedule_once(self.cl28, i * self.tm)
        if list(ra)[i] == "ь":
            Clock.schedule_once(self.cl29, i * self.tm)
        if list(ra)[i] == "э":
            Clock.schedule_once(self.cl30, i * self.tm)
        if list(ra)[i] == "ю":
            Clock.schedule_once(self.cl31, i * self.tm)
        if list(ra)[i] == "я":
            Clock.schedule_once(self.cl32, i * self.tm)


def normal_list(self):
    a_file = open("normal.txt", "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    a_file.close()
    # print(list_of_lists)
    global ra
    ra = random.choice(line_list)
    # print(ra)
    list(ra)
    wlong = len(ra)
    for i in range(wlong):
        # print(list(ra)[i])
        if list(ra)[i] == "а":
            Clock.schedule_once(self.cl1, i * self.tm)
        if list(ra)[i] == "б":
            Clock.schedule_once(self.cl2, i * self.tm)
        if list(ra)[i] == "в":
            Clock.schedule_once(self.cl3, i * self.tm)
        if list(ra)[i] == "г":
            Clock.schedule_once(self.cl4, i * self.tm)
        if list(ra)[i] == "д":
            Clock.schedule_once(self.cl5, i * self.tm)
        if list(ra)[i] == "е":
            Clock.schedule_once(self.cl6, i * self.tm)
        if list(ra)[i] == "ж":
            Clock.schedule_once(self.cl7, i * self.tm)
        if list(ra)[i] == "з":
            Clock.schedule_once(self.cl8, i * self.tm)
        if list(ra)[i] == "и":
            Clock.schedule_once(self.cl9, i * self.tm)
        if list(ra)[i] == "й":
            Clock.schedule_once(self.cl10, i * self.tm)
        if list(ra)[i] == "к":
            Clock.schedule_once(self.cl11, i * self.tm)
        if list(ra)[i] == "л":
            Clock.schedule_once(self.cl12, i * self.tm)
        if list(ra)[i] == "м":
            Clock.schedule_once(self.cl13, i * self.tm)
        if list(ra)[i] == "н":
            Clock.schedule_once(self.cl14, i * self.tm)
        if list(ra)[i] == "о":
            Clock.schedule_once(self.cl15, i * self.tm)
        if list(ra)[i] == "п":
            Clock.schedule_once(self.cl16, i * self.tm)
        if list(ra)[i] == "р":
            Clock.schedule_once(self.cl17, i * self.tm)
        if list(ra)[i] == "с":
            Clock.schedule_once(self.cl18, i * self.tm)
        if list(ra)[i] == "т":
            Clock.schedule_once(self.cl19, i * self.tm)
        if list(ra)[i] == "у":
            Clock.schedule_once(self.cl20, i * self.tm)
        if list(ra)[i] == "ф":
            Clock.schedule_once(self.cl21, i * self.tm)
        if list(ra)[i] == "х":
            Clock.schedule_once(self.cl22, i * self.tm)
        if list(ra)[i] == "ц":
            Clock.schedule_once(self.cl23, i * self.tm)
        if list(ra)[i] == "ч":
            Clock.schedule_once(self.cl24, i * self.tm)
        if list(ra)[i] == "ш":
            Clock.schedule_once(self.cl25, i * self.tm)
        if list(ra)[i] == "щ":
            Clock.schedule_once(self.cl26, i * self.tm)
        if list(ra)[i] == "ъ":
            Clock.schedule_once(self.cl27, i * self.tm)
        if list(ra)[i] == "ы":
            Clock.schedule_once(self.cl28, i * self.tm)
        if list(ra)[i] == "ь":
            Clock.schedule_once(self.cl29, i * self.tm)
        if list(ra)[i] == "э":
            Clock.schedule_once(self.cl30, i * self.tm)
        if list(ra)[i] == "ю":
            Clock.schedule_once(self.cl31, i * self.tm)
        if list(ra)[i] == "я":
            Clock.schedule_once(self.cl32, i * self.tm)


def long_list(self):
    a_file = open("long.txt", "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    a_file.close()
    # print(list_of_lists)
    global ra
    ra = random.choice(line_list)
    # print(ra)
    list(ra)
    wlong = len(ra)
    for i in range(wlong):
        # print(list(ra)[i])
        if list(ra)[i] == "а":
            Clock.schedule_once(self.cl1, i * self.tm)
        if list(ra)[i] == "б":
            Clock.schedule_once(self.cl2, i * self.tm)
        if list(ra)[i] == "в":
            Clock.schedule_once(self.cl3, i * self.tm)
        if list(ra)[i] == "г":
            Clock.schedule_once(self.cl4, i * self.tm)
        if list(ra)[i] == "д":
            Clock.schedule_once(self.cl5, i * self.tm)
        if list(ra)[i] == "е":
            Clock.schedule_once(self.cl6, i * self.tm)
        if list(ra)[i] == "ж":
            Clock.schedule_once(self.cl7, i * self.tm)
        if list(ra)[i] == "з":
            Clock.schedule_once(self.cl8, i * self.tm)
        if list(ra)[i] == "и":
            Clock.schedule_once(self.cl9, i * self.tm)
        if list(ra)[i] == "й":
            Clock.schedule_once(self.cl10, i * self.tm)
        if list(ra)[i] == "к":
            Clock.schedule_once(self.cl11, i * self.tm)
        if list(ra)[i] == "л":
            Clock.schedule_once(self.cl12, i * self.tm)
        if list(ra)[i] == "м":
            Clock.schedule_once(self.cl13, i * self.tm)
        if list(ra)[i] == "н":
            Clock.schedule_once(self.cl14, i * self.tm)
        if list(ra)[i] == "о":
            Clock.schedule_once(self.cl15, i * self.tm)
        if list(ra)[i] == "п":
            Clock.schedule_once(self.cl16, i * self.tm)
        if list(ra)[i] == "р":
            Clock.schedule_once(self.cl17, i * self.tm)
        if list(ra)[i] == "с":
            Clock.schedule_once(self.cl18, i * self.tm)
        if list(ra)[i] == "т":
            Clock.schedule_once(self.cl19, i * self.tm)
        if list(ra)[i] == "у":
            Clock.schedule_once(self.cl20, i * self.tm)
        if list(ra)[i] == "ф":
            Clock.schedule_once(self.cl21, i * self.tm)
        if list(ra)[i] == "х":
            Clock.schedule_once(self.cl22, i * self.tm)
        if list(ra)[i] == "ц":
            Clock.schedule_once(self.cl23, i * self.tm)
        if list(ra)[i] == "ч":
            Clock.schedule_once(self.cl24, i * self.tm)
        if list(ra)[i] == "ш":
            Clock.schedule_once(self.cl25, i * self.tm)
        if list(ra)[i] == "щ":
            Clock.schedule_once(self.cl26, i * self.tm)
        if list(ra)[i] == "ъ":
            Clock.schedule_once(self.cl27, i * self.tm)
        if list(ra)[i] == "ы":
            Clock.schedule_once(self.cl28, i * self.tm)
        if list(ra)[i] == "ь":
            Clock.schedule_once(self.cl29, i * self.tm)
        if list(ra)[i] == "э":
            Clock.schedule_once(self.cl30, i * self.tm)
        if list(ra)[i] == "ю":
            Clock.schedule_once(self.cl31, i * self.tm)
        if list(ra)[i] == "я":
            Clock.schedule_once(self.cl32, i * self.tm)


def cl1(self, text):  # А
    print("а")


def cl2(self, text):  # Б
    print("б")


def cl3(self, text):  # В
    print("в")


def cl4(self, text):  # Г
    print("г")


def cl5(self, text):  # Д
    print("д")


def cl6(self, text):  # Е
    print("е")


def cl7(self, text):  # Ж
    print("ж")


def cl8(self, text):  # З
    print("з")


def cl9(self, text):  # И
    print("и")


def cl10(self, text):  # Й
    print("й")


def cl11(self, text):  # К
    print("к")


def cl12(self, text):  # Л
    print("л")


def cl13(self, text):  # М
    print("м")


def cl14(self, text):  # Н
    print("н")


def cl15(self, text):  # О
    print("о")


def cl16(self, text):  # П
    print("п")


def cl17(self, text):  # Р
    print("р")


def cl18(self, text):  # С
    print("с")


def cl19(self, text):  # Т
    print("т")


def cl20(self, text):  # У
    print("у")


def cl21(self, text):  # Ф
    print("ф")


def cl22(self, text):  # Х
    print("х")


def cl23(self, text):  # Ц
    print("ц")


def cl24(self, text):  # Ч
    print("ч")


def cl25(self, text):  # Ш
    print("ш")


def cl26(self, text):  # Щ
    print("щ")


def cl27(self, text):  # Ъ
    print("ъ")


def cl28(self, text):  # Ы
    print("ы")


def cl29(self, text):  # Ь
    print("ь")


def cl30(self, text):  # Э
    print("э")


def cl31(self, text):  # Ю
    print("ю")


def cl32(self, text):  # Я
    print("я")


def cl33(self, text):  # _
    print(" ")
