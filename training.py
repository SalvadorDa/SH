from kivy.properties import Clock
import random

f_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32]


def corr_check(self):
    if rl == 1:
        self.ch1()
    if rl == 2:
        self.ch2()
    if rl == 3:
        self.ch3()
    if rl == 4:
        self.ch4()
    if rl == 5:
        self.ch5()
    if rl == 6:
        self.ch6()
    if rl == 7:
        self.ch7()
    if rl == 8:
        self.ch8()
    if rl == 9:
        self.ch9()
    if rl == 10:
        self.ch10()
    if rl == 11:
        self.ch11()
    if rl == 12:
        self.ch12()
    if rl == 13:
        self.ch13()
    if rl == 14:
        self.ch14()
    if rl == 15:
        self.ch15()
    if rl == 16:
        self.ch16()
    if rl == 17:
        self.ch17()
    if rl == 18:
        self.ch18()
    if rl == 19:
        self.ch19()
    if rl == 20:
        self.ch20()
    if rl == 21:
        self.ch21()
    if rl == 22:
        self.ch22()
    if rl == 23:
        self.ch23()
    if rl == 24:
        self.ch24()
    if rl == 25:
        self.ch25()
    if rl == 26:
        self.ch26()
    if rl == 27:
        self.ch27()
    if rl == 28:
        self.ch28()
    if rl == 29:
        self.ch29()
    if rl == 30:
        self.ch30()
    if rl == 31:
        self.ch31()
    if rl == 32:
        self.ch32()


def re_letter(self):
    if rl == 1:
        self.cl1()
    if rl == 2:
        self.cl2()
    if rl == 3:
        self.cl3()
    if rl == 4:
        self.cl4()
    if rl == 5:
        self.cl5()
    if rl == 6:
        self.cl6()
    if rl == 7:
        self.cl7()
    if rl == 8:
        self.cl8()
    if rl == 9:
        self.cl9()
    if rl == 10:
        self.cl10()
    if rl == 11:
        self.cl11()
    if rl == 12:
        self.cl12()
    if rl == 13:
        self.cl13()
    if rl == 14:
        self.cl14()
    if rl == 15:
        self.cl15()
    if rl == 16:
        self.cl16()
    if rl == 17:
        self.cl17()
    if rl == 18:
        self.cl18()
    if rl == 19:
        self.cl19()
    if rl == 20:
        self.cl20()
    if rl == 21:
        self.cl21()
    if rl == 22:
        self.cl22()
    if rl == 23:
        self.cl23()
    if rl == 24:
        self.cl24()
    if rl == 25:
        self.cl25()
    if rl == 26:
        self.cl26()
    if rl == 27:
        self.cl27()
    if rl == 28:
        self.cl28()
    if rl == 29:
        self.cl29()
    if rl == 30:
        self.cl30()
    if rl == 31:
        self.cl31()
    if rl == 32:
        self.cl32()


def rand_letter(self):
    global rl
    rl = random.choice(f_list)
    if rl == 1:
        self.cl1()
    if rl == 2:
        self.cl2()
    if rl == 3:
        self.cl3()
    if rl == 4:
        self.cl4()
    if rl == 5:
        self.cl5()
    if rl == 6:
        self.cl6()
    if rl == 7:
        self.cl7()
    if rl == 8:
        self.cl8()
    if rl == 9:
        self.cl9()
    if rl == 10:
        self.cl10()
    if rl == 11:
        self.cl11()
    if rl == 12:
        self.cl12()
    if rl == 13:
        self.cl13()
    if rl == 14:
        self.cl14()
    if rl == 15:
        self.cl15()
    if rl == 16:
        self.cl16()
    if rl == 17:
        self.cl17()
    if rl == 18:
        self.cl18()
    if rl == 19:
        self.cl19()
    if rl == 20:
        self.cl20()
    if rl == 21:
        self.cl21()
    if rl == 22:
        self.cl22()
    if rl == 23:
        self.cl23()
    if rl == 24:
        self.cl24()
    if rl == 25:
        self.cl25()
    if rl == 26:
        self.cl26()
    if rl == 27:
        self.cl27()
    if rl == 28:
        self.cl28()
    if rl == 29:
        self.cl29()
    if rl == 30:
        self.cl30()
    if rl == 31:
        self.cl31()
    if rl == 32:
        self.cl32()


def on_slider_value(self, widget):
    self.tm = int(widget.value) / - 100


def cl1(self):  # А
    Clock.schedule_once(self.a1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.a1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl2(self):  # Б
    Clock.schedule_once(self.c2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl3(self):  # В
    Clock.schedule_once(self.d2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl4(self):  # Г
    Clock.schedule_once(self.b1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl5(self):  # Д
    Clock.schedule_once(self.a2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl6(self):  # Е
    Clock.schedule_once(self.a2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.a2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl7(self):  # Ж
    Clock.schedule_once(self.d1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.a2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl8(self):  # З
    Clock.schedule_once(self.b1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl9(self):  # И
    Clock.schedule_once(self.c1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl10(self):  # Й
    Clock.schedule_once(self.c1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.a2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl11(self):  # К
    Clock.schedule_once(self.c1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl12(self):  # Л
    Clock.schedule_once(self.b1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl13(self):  # М
    Clock.schedule_once(self.d1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl14(self):  # Н
    Clock.schedule_once(self.a2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl15(self):  # О
    Clock.schedule_once(self.b1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl16(self):  # П
    Clock.schedule_once(self.a1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl17(self):  # Р
    Clock.schedule_once(self.c1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl18(self):  # С
    Clock.schedule_once(self.a1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.a2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl19(self):  # Т
    Clock.schedule_once(self.c1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl20(self):  # У
    Clock.schedule_once(self.d2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl21(self):  # Ф
    Clock.schedule_once(self.b1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl22(self):  # Х
    Clock.schedule_once(self.d2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl23(self):  # Ц
    Clock.schedule_once(self.b1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl24(self):  # Ч
    Clock.schedule_once(self.d1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl25(self):  # Ш
    Clock.schedule_once(self.b2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl26(self):  # Щ
    Clock.schedule_once(self.b2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl27(self):  # Ъ
    Clock.schedule_once(self.c2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl28(self):  # Ы
    Clock.schedule_once(self.c2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl29(self):  # Ь
    Clock.schedule_once(self.c2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl30(self):  # Э
    Clock.schedule_once(self.a2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.a2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl31(self):  # Ю
    Clock.schedule_once(self.b2, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b2, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def cl32(self):  # Я
    Clock.schedule_once(self.d1, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d1, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def res(self, dt):
    self.ids['A1'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['B1'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['C1'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['D1'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['A2'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['B2'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['C2'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['D2'].background_color = 0.0, 0.0, 0.3, 1.0


def a1(self, dt):
    self.ids['A1'].background_color = 1.0, 0.0, 0.0, 1.0


def b1(self, dt):
    self.ids['B1'].background_color = 1.0, 0.0, 0.0, 1.0


def c1(self, dt):
    self.ids['C1'].background_color = 1.0, 0.0, 0.0, 1.0


def d1(self, dt):
    self.ids['D1'].background_color = 1.0, 0.0, 0.0, 1.0


def a2(self, dt):
    self.ids['A2'].background_color = 1.0, 0.0, 0.0, 1.0


def b2(self, dt):
    self.ids['B2'].background_color = 1.0, 0.0, 0.0, 1.0


def c2(self, dt):
    self.ids['C2'].background_color = 1.0, 0.0, 0.0, 1.0


def d2(self, dt):
    self.ids['D2'].background_color = 1.0, 0.0, 0.0, 1.0


def res2(self, dt):
    self.ids['1'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['2'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['3'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['4'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['5'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['6'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['7'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['8'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['9'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['10'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['11'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['12'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['13'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['14'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['15'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['16'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['17'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['18'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['19'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['20'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['21'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['22'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['23'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['24'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['25'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['26'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['27'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['28'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['29'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['30'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['31'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['32'].background_color = 0.5, 0.5, 0.5, 1


def l1(self, dt):
    self.ids['1'].background_color = 0.0, 1.0, 0.0, 1.0


def l2(self, dt):
    self.ids['2'].background_color = 0.0, 1.0, 0.0, 1.0


def l3(self, dt):
    self.ids['3'].background_color = 0.0, 1.0, 0.0, 1.0


def l4(self, dt):
    self.ids['4'].background_color = 0.0, 1.0, 0.0, 1.0


def l5(self, dt):
    self.ids['5'].background_color = 0.0, 1.0, 0.0, 1.0


def l6(self, dt):
    self.ids['6'].background_color = 0.0, 1.0, 0.0, 1.0


def l7(self, dt):
    self.ids['7'].background_color = 0.0, 1.0, 0.0, 1.0


def l8(self, dt):
    self.ids['8'].background_color = 0.0, 1.0, 0.0, 1.0


def l9(self, dt):
    self.ids['9'].background_color = 0.0, 1.0, 0.0, 1.0


def l10(self, dt):
    self.ids['10'].background_color = 0.0, 1.0, 0.0, 1.0


def l11(self, dt):
    self.ids['11'].background_color = 0.0, 1.0, 0.0, 1.0


def l12(self, dt):
    self.ids['12'].background_color = 0.0, 1.0, 0.0, 1.0


def l13(self, dt):
    self.ids['13'].background_color = 0.0, 1.0, 0.0, 1.0


def l14(self, dt):
    self.ids['14'].background_color = 0.0, 1.0, 0.0, 1.0


def l15(self, dt):
    self.ids['15'].background_color = 0.0, 1.0, 0.0, 1.0


def l16(self, dt):
    self.ids['16'].background_color = 0.0, 1.0, 0.0, 1.0


def l17(self, dt):
    self.ids['17'].background_color = 0.0, 1.0, 0.0, 1.0


def l18(self, dt):
    self.ids['18'].background_color = 0.0, 1.0, 0.0, 1.0


def l19(self, dt):
    self.ids['19'].background_color = 0.0, 1.0, 0.0, 1.0


def l20(self, dt):
    self.ids['20'].background_color = 0.0, 1.0, 0.0, 1.0


def l21(self, dt):
    self.ids['21'].background_color = 0.0, 1.0, 0.0, 1.0


def l22(self, dt):
    self.ids['22'].background_color = 0.0, 1.0, 0.0, 1.0


def l23(self, dt):
    self.ids['23'].background_color = 0.0, 1.0, 0.0, 1.0


def l24(self, dt):
    self.ids['24'].background_color = 0.0, 1.0, 0.0, 1.0


def l25(self, dt):
    self.ids['25'].background_color = 0.0, 1.0, 0.0, 1.0


def l26(self, dt):
    self.ids['26'].background_color = 0.0, 1.0, 0.0, 1.0


def l27(self, dt):
    self.ids['27'].background_color = 0.0, 1.0, 0.0, 1.0


def l28(self, dt):
    self.ids['28'].background_color = 0.0, 1.0, 0.0, 1.0


def l29(self, dt):
    self.ids['29'].background_color = 0.0, 1.0, 0.0, 1.0


def l30(self, dt):
    self.ids['30'].background_color = 0.0, 1.0, 0.0, 1.0


def l31(self, dt):
    self.ids['31'].background_color = 0.0, 1.0, 0.0, 1.0


def l32(self, dt):
    self.ids['32'].background_color = 0.0, 1.0, 0.0, 1.0


def ch1(self):
    Clock.schedule_once(self.l1, 0)
    Clock.schedule_once(self.res2, 1)


def ch2(self):
    Clock.schedule_once(self.l2, 0)
    Clock.schedule_once(self.res2, 1)


def ch3(self):
    Clock.schedule_once(self.l3, 0)
    Clock.schedule_once(self.res2, 1)


def ch4(self):
    Clock.schedule_once(self.l4, 0)
    Clock.schedule_once(self.res2, 1)


def ch5(self):
    Clock.schedule_once(self.l5, 0)
    Clock.schedule_once(self.res2, 1)


def ch6(self):
    Clock.schedule_once(self.l6, 0)
    Clock.schedule_once(self.res2, 1)


def ch7(self):
    Clock.schedule_once(self.l7, 0)
    Clock.schedule_once(self.res2, 1)


def ch8(self):
    Clock.schedule_once(self.l8, 0)
    Clock.schedule_once(self.res2, 1)


def ch9(self):
    Clock.schedule_once(self.l9, 0)
    Clock.schedule_once(self.res2, 1)


def ch10(self):
    Clock.schedule_once(self.l10, 0)
    Clock.schedule_once(self.res2, 1)


def ch11(self):
    Clock.schedule_once(self.l11, 0)
    Clock.schedule_once(self.res2, 1)


def ch12(self):
    Clock.schedule_once(self.l12, 0)
    Clock.schedule_once(self.res2, 1)


def ch13(self):
    Clock.schedule_once(self.l13, 0)
    Clock.schedule_once(self.res2, 1)


def ch14(self):
    Clock.schedule_once(self.l14, 0)
    Clock.schedule_once(self.res2, 1)


def ch15(self):
    Clock.schedule_once(self.l15, 0)
    Clock.schedule_once(self.res2, 1)


def ch16(self):
    Clock.schedule_once(self.l16, 0)
    Clock.schedule_once(self.res2, 1)


def ch17(self):
    Clock.schedule_once(self.l17, 0)
    Clock.schedule_once(self.res2, 1)


def ch18(self):
    Clock.schedule_once(self.l18, 0)
    Clock.schedule_once(self.res2, 1)


def ch19(self):
    Clock.schedule_once(self.l19, 0)
    Clock.schedule_once(self.res2, 1)


def ch20(self):
    Clock.schedule_once(self.l20, 0)
    Clock.schedule_once(self.res2, 1)


def ch21(self):
    Clock.schedule_once(self.l21, 0)
    Clock.schedule_once(self.res2, 1)


def ch22(self):
    Clock.schedule_once(self.l22, 0)
    Clock.schedule_once(self.res2, 1)


def ch23(self):
    Clock.schedule_once(self.l23, 0)
    Clock.schedule_once(self.res2, 1)


def ch24(self):
    Clock.schedule_once(self.l24, 0)
    Clock.schedule_once(self.res2, 1)


def ch25(self):
    Clock.schedule_once(self.l25, 0)
    Clock.schedule_once(self.res2, 1)


def ch26(self):
    Clock.schedule_once(self.l26, 0)
    Clock.schedule_once(self.res2, 1)


def ch27(self):
    Clock.schedule_once(self.l27, 0)
    Clock.schedule_once(self.res2, 1)


def ch28(self):
    Clock.schedule_once(self.l28, 0)
    Clock.schedule_once(self.res2, 1)


def ch29(self):
    Clock.schedule_once(self.l29, 0)
    Clock.schedule_once(self.res2, 1)


def ch30(self):
    Clock.schedule_once(self.l30, 0)
    Clock.schedule_once(self.res2, 1)


def ch31(self):
    Clock.schedule_once(self.l31, 0)
    Clock.schedule_once(self.res2, 1)


def ch32(self):
    Clock.schedule_once(self.l32, 0)
    Clock.schedule_once(self.res2, 1)



