from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class AnchorLayout(AnchorLayout):
    pass


class MainWindow(Screen):
    pass


class TrainingRuTest(Screen):
    from training import cl1, res, a1, a2, b1, b2, c1, c2, d1, d2, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cl11, \
        cl12, cl13, cl14, cl15, cl16, cl17, cl18, cl19, cl20, cl21, cl22, cl23, cl24, cl25, cl26, cl27, cl28, cl29, \
        cl30, cl31, cl32, on_slider_value, rand_letter, re_letter, res2, ch1, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, \
        l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, l31, l32, \
        ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20, \
        ch21, ch22, ch23, ch24, ch25, ch26, ch27, ch28, ch29, ch30, ch31, ch32, corr_check

    def __init__(self, tm=0.5, **kw):
        super().__init__(**kw)
        self.tm = tm


class TrainingWindow(Screen):
    from training import cl1, res, a1, a2, b1, b2, c1, c2, d1, d2, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cl11, \
        cl12, cl13, cl14, cl15, cl16, cl17, cl18, cl19, cl20, cl21, cl22, cl23, cl24, cl25, cl26, cl27, cl28, cl29, \
        cl30, cl31, cl32, on_slider_value

    def __init__(self, tm=0.5, **kw):
        super().__init__(**kw)
        self.tm = tm


class TrNumWindow(Screen):
    from numwin import on_slider_value, ncl1, res, a4, a5, b4, b5, c4, c5, d4, d5, ncl2, ncl3, ncl4, ncl5, ncl6, ncl7, \
        ncl8, ncl9, ncl10, ncl11, ncl12, ncl13, ncl14, ncl15, ncl16, ncl17, ncl18, ncl19

    def __init__(self, tm=0.5, **kw):
        super().__init__(**kw)
        self.tm = tm


class TrNumTest(Screen):
    from numwin import on_slider_value, ncl1, res, a4, a5, b4, b5, c4, c5, d4, d5, ncl2, ncl3, ncl4, ncl5, ncl6, ncl7, \
        ncl8, ncl9, ncl10, ncl11, ncl12, ncl13, ncl14, ncl15, ncl16, ncl17, ncl18, ncl19, rand_num, re_num, \
        corr_check_num, res2, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, \
        nch1, nch2, nch3, nch4, nch5, nch6, nch7, nch8, nch9, nch10, nch11, nch12, nch13, nch14, nch15, nch16, nch17, \
        nch18, nch19, rand_time, m_funk, mm_funk

    def __init__(self, tm=0.5, **kw):
        super().__init__(**kw)
        self.tm = tm


class TrWords(Screen):
    from trwords import on_slider_value, short_list, cl31, cl30, cl29, cl28, cl27, cl26, cl25, cl24, cl23, cl22, cl21, \
        cl20, cl19, cl18, cl17, cl16, cl15, cl14, cl13, cl12, cl11, cl10, cl9, cl8, cl7, cl6, cl5, cl4, cl3, cl2, cl1, \
        normal_list, long_list, repeat_list, combination_list, cl32, cl33

    def __init__(self, tm=0.5, **kw):
        super().__init__(**kw)
        self.tm = tm


class Setup(Screen):
    pass


class BTConnect(Screen):
    from btconnect import connect_bt, on, con_bt, disconnect


class WindowManager(ScreenManager):
    pass


class MainWidget(Widget):
    pass


class SenseHandApp(App):
    pass


SenseHandApp().run()
