from common.r3 import R3
from shadow.polyedr import Polyedr


class TestMod:

    # =====================================
    # Тесты на проверку решения модификации
    # =====================================

    # Проверка точек на пример "хорошести"

    def test_mod01(self):
        a = R3(0.0, 0.0, 0.0)
        assert a.is_good() == 1

    def test_mod02(self):
        a = R3(2.0, 3.0, -4.1)
        assert a.is_good() == 0

    def test_mod03(self):
        a = R3(0.5, -0.2, 0.8)
        assert a.is_good() == 1

    # Корректная работа вычисления площади

    # Для куба с точками с координатами = |0.5|
    def test_mod10(self):
        pol = Polyedr("data/cube1.geom")
        assert pol.ret_sqr() == 6.0

    # Для куба с точками с координатами = |1|
    def test_mod20(self):
        pol = Polyedr("data/cube2.geom")
        assert pol.ret_sqr() == 0.0


'''
a = TestMod()
a.test_mod10()
'''
