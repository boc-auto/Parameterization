import pytest,yaml
from practice.caculator import Caculator


# print(yaml.safe_load(open('./data_test.yaml'))['add'])

def div_zero():
    raise ZeroDivisionError('除数为0的异常')

class TestCalculatorAdd:

    def setup_class(self):
        print('开始加法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('加法计算结束')

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data_test.yaml'))['add'])
    def test_add(self, a, b, expect):
        assert expect == a + b


class TestCalculatorSub:

    def setup_class(self):
        print('开始减法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('减法计算结束')

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data_test.yaml'))['sub'])
    def test_sub(self, a, b, expect):
        assert expect == a - b


class TestCalculatorMul:

    def setup_class(self):
        print('开始乘法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('乘法计算结束')

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data_test.yaml'))['mul'])
    def test_mul(self, a, b, expect):
        assert expect == a * b


class TestCalculatorDiv:

    def setup_class(self):
        print('开始除法计算')
        self.calc = Caculator()

    def teardown_class(self):
        print('除法计算结束')

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./data_test.yaml'))['div'])
    def test_div(self, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                div_zero()
        assert expect == a / b
