import pytest
from practice.caculator import Caculator


def div_zero():
    raise ZeroDivisionError('除数为0的异常')

class TestCalculatorAdd:

    def setup_class(self):
        print('开始加法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('加法计算结束')

    @pytest.mark.parametrize('a,b,expect',
                             [(6, 2, 8), (10, 6, 16), (8, 0, 8)],
                             ids=["one_case1", "two_case1", "three_case1"]
                             )
    def test_add(self, a, b, expect):
        assert expect == a + b


class TestCalculatorSub:

    def setup_class(self):
        print('开始减法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('减法计算结束')

    @pytest.mark.parametrize('a,b,expect',
                             [(5, 2, 3), (10, 6, 4), (0, 4, -4)],
                             ids=["one_case2", "two_case2", "three_case2"]
                             )
    def test_sub(self, a, b, expect):
        assert expect == a - b


class TestCalculatorMul:

    def setup_class(self):
        print('开始乘法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('乘法计算结束')

    @pytest.mark.parametrize('a,b,expect',
                             [(2, 3, 6), (5, 6, 30), (8, 0, 0)],
                             ids=["one_case3", "two_case3", "three_case3"]
                             )
    def test_mul(self, a, b, expect):
        assert expect == a * b


class TestCalculatorDiv:

    def setup_class(self):
        print('开始除法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('除法计算结束')

    @pytest.mark.parametrize('a,b,expect',
                             [(8, 2, 4), (9, 0, 0), (18, 6, 3)],
                             ids=["one_case4", "two_case4", "three_case4"]
                             )
    def test_div(self, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                div_zero()
        assert expect == a / b
