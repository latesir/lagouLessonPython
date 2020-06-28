#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/6/21
import pytest
import yaml

from test_pytest_work1.calculator import Calculator


def get_yaml_data(key):
    with open('./calculator.yaml', 'r') as f:
        datas = yaml.safe_load(f)
        return datas[key]


class TestCalculator:
    def setup_class(self):
        print('实例化计算器类')
        self.cal = Calculator()

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    @pytest.mark.parametrize(['a', 'b', 'c'], get_yaml_data('add_sub'))
    def test_add(self, a, b, c, setup_and_teardown):
        assert c == self.cal.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.parametrize(['c', 'b', 'a'], get_yaml_data('add_sub'))
    def check_sub(self, a, b, c, setup_and_teardown):
        assert c == self.cal.sub(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    @pytest.mark.parametrize(['a', 'b', 'c'], get_yaml_data('mul_div'))
    def check_mul(self, a, b, c, setup_and_teardown):
        assert c == self.cal.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.parametrize(['c', 'b', 'a'], get_yaml_data('mul_div'))
    def check_div(self, a, b, c, setup_and_teardown):
        try:
            c == self.cal.div(a, b)
        except ZeroDivisionError:
            print('被除数为0')
        else:
            assert c == self.cal.div(a, b)
