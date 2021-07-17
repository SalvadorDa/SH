from kivy.properties import Clock
import random

n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


def rand_time(self):
    h = random.randint(1, 12)
    if h == 1:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a4, 2 * self.tm)
        Clock.schedule_once(self.d4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.m_funk, 4 * self.tm)
    elif h == 2:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.a4, 4 * self.tm)
        Clock.schedule_once(self.d4, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.m_funk, 6 * self.tm)
    elif h == 3:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a4, 2 * self.tm)
        Clock.schedule_once(self.d4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.m_funk, 4 * self.tm)
    elif h == 4:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.b5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.a4, 4 * self.tm)
        Clock.schedule_once(self.d4, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.m_funk, 6 * self.tm)
    elif h == 5:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a4, 2 * self.tm)
        Clock.schedule_once(self.d4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.m_funk, 4 * self.tm)
    elif h == 6:
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.c5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.a4, 4 * self.tm)
        Clock.schedule_once(self.d4, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.m_funk, 6 * self.tm)
    elif h == 7:
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a4, 2 * self.tm)
        Clock.schedule_once(self.d4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.m_funk, 4 * self.tm)
    elif h == 8:
        Clock.schedule_once(self.d5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.d5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.a4, 4 * self.tm)
        Clock.schedule_once(self.d4, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.m_funk, 6 * self.tm)
    elif h == 9:
        Clock.schedule_once(self.d5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a4, 2 * self.tm)
        Clock.schedule_once(self.d4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.m_funk, 4 * self.tm)
    elif h == 10:
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.d5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a4, 2 * self.tm)
        Clock.schedule_once(self.d4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.m_funk, 4 * self.tm)
    elif h == 11:
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.d5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.a4, 4 * self.tm)
        Clock.schedule_once(self.d4, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.m_funk, 6 * self.tm)
    elif h == 12:
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.d5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.a5, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.a4, 6 * self.tm)
        Clock.schedule_once(self.d4, 6 * self.tm)
        Clock.schedule_once(self.res, 7 * self.tm)
        Clock.schedule_once(self.m_funk, 8 * self.tm)


def m_funk(self, text):
    m = random.randint(0, 5)
    # print(m)
    if m == 0:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.b4, 2 * self.tm)
        Clock.schedule_once(self.c4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.mm_funk, 4 * self.tm)
    elif m == 1:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.b4, 2 * self.tm)
        Clock.schedule_once(self.c4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.mm_funk, 4 * self.tm)
    elif m == 2:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.b4, 4 * self.tm)
        Clock.schedule_once(self.c4, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.mm_funk, 6 * self.tm)
    elif m == 3:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.b4, 2 * self.tm)
        Clock.schedule_once(self.c4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.mm_funk, 4 * self.tm)
    elif m == 4:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.b5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.b4, 4 * self.tm)
        Clock.schedule_once(self.c4, 4 * self.tm)
        Clock.schedule_once(self.res, 5 * self.tm)
        Clock.schedule_once(self.mm_funk, 6 * self.tm)
    elif m == 5:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.b4, 2 * self.tm)
        Clock.schedule_once(self.c4, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
        Clock.schedule_once(self.mm_funk, 4 * self.tm)


def mm_funk(self, text):
    mm = random.randint(0, 9)
    if mm == 0:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
    elif mm == 1:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.res, self.tm)
    elif mm == 2:
        Clock.schedule_once(self.a5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.a5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
    elif mm == 3:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
    elif mm == 4:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.b5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
    elif mm == 5:
        Clock.schedule_once(self.b5, 0)
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.res, self.tm)
    elif mm == 6:
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.c5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
    elif mm == 7:
        Clock.schedule_once(self.c5, 0)
        Clock.schedule_once(self.res, self.tm)
    elif mm == 8:
        Clock.schedule_once(self.d5, 0)
        Clock.schedule_once(self.res, self.tm)
        Clock.schedule_once(self.d5, 2 * self.tm)
        Clock.schedule_once(self.res, 3 * self.tm)
    elif mm == 9:
        Clock.schedule_once(self.d5, 0)
        Clock.schedule_once(self.res, self.tm)


def corr_check_num(self):
    if rn == 1:
        self.nch1()
    if rn == 2:
        self.nch2()
    if rn == 3:
        self.nch3()
    if rn == 4:
        self.nch4()
    if rn == 5:
        self.nch5()
    if rn == 6:
        self.nch6()
    if rn == 7:
        self.nch7()
    if rn == 8:
        self.nch8()
    if rn == 9:
        self.nch9()
    if rn == 10:
        self.nch10()
    if rn == 11:
        self.nch11()
    if rn == 12:
        self.nch12()
    if rn == 13:
        self.nch13()
    if rn == 14:
        self.nch14()
    if rn == 15:
        self.nch15()
    if rn == 16:
        self.nch16()
    if rn == 17:
        self.nch17()
    if rn == 18:
        self.nch18()
    if rn == 19:
        self.nch19()

def re_num(self):
    if rn == 1:
        self.ncl1()
    if rn == 2:
        self.ncl2()
    if rn == 3:
        self.ncl3()
    if rn == 4:
        self.ncl4()
    if rn == 5:
        self.ncl5()
    if rn == 6:
        self.ncl6()
    if rn == 7:
        self.ncl7()
    if rn == 8:
        self.ncl8()
    if rn == 9:
        self.ncl9()
    if rn == 10:
        self.ncl10()
    if rn == 11:
        self.ncl11()
    if rn == 12:
        self.ncl12()
    if rn == 13:
        self.ncl13()
    if rn == 14:
        self.ncl14()
    if rn == 15:
        self.ncl15()
    if rn == 16:
        self.ncl16()
    if rn == 17:
        self.ncl17()
    if rn == 18:
        self.ncl18()
    if rn == 19:
        self.ncl19()


def rand_num(self):
    global rn
    rn = random.choice(n_list)
    if rn == 1:
        self.ncl1()
    if rn == 2:
        self.ncl2()
    if rn == 3:
        self.ncl3()
    if rn == 4:
        self.ncl4()
    if rn == 5:
        self.ncl5()
    if rn == 6:
        self.ncl6()
    if rn == 7:
        self.ncl7()
    if rn == 8:
        self.ncl8()
    if rn == 9:
        self.ncl9()
    if rn == 10:
        self.ncl10()
    if rn == 11:
        self.ncl11()
    if rn == 12:
        self.ncl12()
    if rn == 13:
        self.ncl13()
    if rn == 14:
        self.ncl14()
    if rn == 15:
        self.ncl15()
    if rn == 16:
        self.ncl16()
    if rn == 17:
        self.ncl17()
    if rn == 18:
        self.ncl18()
    if rn == 19:
        self.ncl19()


def on_slider_value(self, widget):
    self.tm = int(widget.value) / - 100


def ncl1(self):  # 0
    Clock.schedule_once(self.a5, 0)
    Clock.schedule_once(self.b5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl2(self):  # 1
    Clock.schedule_once(self.a5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl3(self):  # 2
    Clock.schedule_once(self.a5, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.a5, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def ncl4(self):  # 3
    Clock.schedule_once(self.b5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl5(self):  # 4
    Clock.schedule_once(self.b5, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.b5, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def ncl6(self):  # 5
    Clock.schedule_once(self.b5, 0)
    Clock.schedule_once(self.c5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl7(self):  # 6
    Clock.schedule_once(self.c5, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.c5, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def ncl8(self):  # 7
    Clock.schedule_once(self.c5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl9(self):  # 8
    Clock.schedule_once(self.d5, 0)
    Clock.schedule_once(self.res, self.tm)
    Clock.schedule_once(self.d5, 2 * self.tm)
    Clock.schedule_once(self.res, 3 * self.tm)


def ncl10(self):  # 9
    Clock.schedule_once(self.d5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl11(self):  # 10
    Clock.schedule_once(self.c5, 0)
    Clock.schedule_once(self.d5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl12(self):  # ?
    Clock.schedule_once(self.a4, 0)
    Clock.schedule_once(self.a5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl13(self):  # !
    Clock.schedule_once(self.d4, 0)
    Clock.schedule_once(self.d5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl14(self):  # .
    Clock.schedule_once(self.a4, 0)
    Clock.schedule_once(self.b4, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl15(self):  # ,
    Clock.schedule_once(self.c4, 0)
    Clock.schedule_once(self.d4, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl16(self):  # -
    Clock.schedule_once(self.b4, 0)
    Clock.schedule_once(self.c4, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl17(self):  # :
    Clock.schedule_once(self.a4, 0)
    Clock.schedule_once(self.d4, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl18(self):  # (
    Clock.schedule_once(self.b4, 0)
    Clock.schedule_once(self.b5, 0)
    Clock.schedule_once(self.res, self.tm)


def ncl19(self):  # )
    Clock.schedule_once(self.c4, 0)
    Clock.schedule_once(self.c5, 0)
    Clock.schedule_once(self.res, self.tm)


def res(self, dt):
    self.ids['A4'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['B4'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['C4'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['D4'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['A5'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['B5'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['C5'].background_color = 0.0, 0.0, 0.3, 1.0
    self.ids['D5'].background_color = 0.0, 0.0, 0.3, 1.0


def a4(self, dt):
    self.ids['A4'].background_color = 1.0, 0.0, 0.0, 1.0


def b4(self, dt):
    self.ids['B4'].background_color = 1.0, 0.0, 0.0, 1.0


def c4(self, dt):
    self.ids['C4'].background_color = 1.0, 0.0, 0.0, 1.0


def d4(self, dt):
    self.ids['D4'].background_color = 1.0, 0.0, 0.0, 1.0


def a5(self, dt):
    self.ids['A5'].background_color = 1.0, 0.0, 0.0, 1.0


def b5(self, dt):
    self.ids['B5'].background_color = 1.0, 0.0, 0.0, 1.0


def c5(self, dt):
    self.ids['C5'].background_color = 1.0, 0.0, 0.0, 1.0


def d5(self, dt):
    self.ids['D5'].background_color = 1.0, 0.0, 0.0, 1.0


def res2(self, dt):
    self.ids['n1'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n2'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n3'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n4'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n5'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n6'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n7'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n8'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n9'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n10'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n11'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n12'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n13'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n14'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n15'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n16'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n17'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n18'].background_color = 0.5, 0.5, 0.5, 1
    self.ids['n19'].background_color = 0.5, 0.5, 0.5, 1


def n1(self, dt):
    self.ids['n1'].background_color = 0.0, 1.0, 0.0, 1.0


def n2(self, dt):
    self.ids['n2'].background_color = 0.0, 1.0, 0.0, 1.0


def n3(self, dt):
    self.ids['n3'].background_color = 0.0, 1.0, 0.0, 1.0


def n4(self, dt):
    self.ids['n4'].background_color = 0.0, 1.0, 0.0, 1.0


def n5(self, dt):
    self.ids['n5'].background_color = 0.0, 1.0, 0.0, 1.0


def n6(self, dt):
    self.ids['n6'].background_color = 0.0, 1.0, 0.0, 1.0


def n7(self, dt):
    self.ids['n7'].background_color = 0.0, 1.0, 0.0, 1.0


def n8(self, dt):
    self.ids['n8'].background_color = 0.0, 1.0, 0.0, 1.0


def n9(self, dt):
    self.ids['n9'].background_color = 0.0, 1.0, 0.0, 1.0


def n10(self, dt):
    self.ids['n10'].background_color = 0.0, 1.0, 0.0, 1.0


def n11(self, dt):
    self.ids['n11'].background_color = 0.0, 1.0, 0.0, 1.0


def n12(self, dt):
    self.ids['n12'].background_color = 0.0, 1.0, 0.0, 1.0


def n13(self, dt):
    self.ids['n13'].background_color = 0.0, 1.0, 0.0, 1.0


def n14(self, dt):
    self.ids['n14'].background_color = 0.0, 1.0, 0.0, 1.0


def n15(self, dt):
    self.ids['n15'].background_color = 0.0, 1.0, 0.0, 1.0


def n16(self, dt):
    self.ids['n16'].background_color = 0.0, 1.0, 0.0, 1.0


def n17(self, dt):
    self.ids['n17'].background_color = 0.0, 1.0, 0.0, 1.0


def n18(self, dt):
    self.ids['n18'].background_color = 0.0, 1.0, 0.0, 1.0


def n19(self, dt):
    self.ids['n19'].background_color = 0.0, 1.0, 0.0, 1.0


def nch1(self):
    Clock.schedule_once(self.n1, 0)
    Clock.schedule_once(self.res2, 1)


def nch2(self):
    Clock.schedule_once(self.n2, 0)
    Clock.schedule_once(self.res2, 1)


def nch3(self):
    Clock.schedule_once(self.n3, 0)
    Clock.schedule_once(self.res2, 1)


def nch4(self):
    Clock.schedule_once(self.n4, 0)
    Clock.schedule_once(self.res2, 1)


def nch5(self):
    Clock.schedule_once(self.n5, 0)
    Clock.schedule_once(self.res2, 1)


def nch6(self):
    Clock.schedule_once(self.n6, 0)
    Clock.schedule_once(self.res2, 1)


def nch7(self):
    Clock.schedule_once(self.n7, 0)
    Clock.schedule_once(self.res2, 1)


def nch8(self):
    Clock.schedule_once(self.n8, 0)
    Clock.schedule_once(self.res2, 1)


def nch9(self):
    Clock.schedule_once(self.n9, 0)
    Clock.schedule_once(self.res2, 1)


def nch10(self):
    Clock.schedule_once(self.n10, 0)
    Clock.schedule_once(self.res2, 1)


def nch11(self):
    Clock.schedule_once(self.n11, 0)
    Clock.schedule_once(self.res2, 1)


def nch12(self):
    Clock.schedule_once(self.n12, 0)
    Clock.schedule_once(self.res2, 1)


def nch13(self):
    Clock.schedule_once(self.n13, 0)
    Clock.schedule_once(self.res2, 1)


def nch14(self):
    Clock.schedule_once(self.n14, 0)
    Clock.schedule_once(self.res2, 1)


def nch15(self):
    Clock.schedule_once(self.n15, 0)
    Clock.schedule_once(self.res2, 1)


def nch16(self):
    Clock.schedule_once(self.n16, 0)
    Clock.schedule_once(self.res2, 1)


def nch17(self):
    Clock.schedule_once(self.n17, 0)
    Clock.schedule_once(self.res2, 1)


def nch18(self):
    Clock.schedule_once(self.n18, 0)
    Clock.schedule_once(self.res2, 1)


def nch19(self):
    Clock.schedule_once(self.n19, 0)
    Clock.schedule_once(self.res2, 1)
