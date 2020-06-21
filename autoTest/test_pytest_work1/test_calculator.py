#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/6/21
import pytest

from test_pytest_work1.calculator import Calculator


class TestCalculator:
    def setup_class(self):
        print('实例化计算器类')
        self.cal = Calculator()

    @pytest.mark.parametrize(['a', 'b', 'c'], [(1, 2, 3), (-1, -2, -3), (0, 0, 0), (123, 999, 1122), (-1, 2, 1)])
    def test_add(self, a, b, c, setup_and_teardown):
        assert c == self.cal.add(a, b)

    @pytest.mark.parametrize(['c', 'b', 'a'], [(1, 2, 3), (-1, -2, -3), (0, 0, 0), (123, 999, 1122), (-1, 2, 1)])
    def test_sub(self, a, b, c, setup_and_teardown):
        assert c == self.cal.sub(a, b)

    @pytest.mark.parametrize(['a', 'b', 'c'], [(1, 2, 2), (-1, -2, 2), (0, 0, 0), (120, 120, 14400), (-1, 2, -2)])
    def test_mul(self, a, b, c, setup_and_teardown):
        assert c == self.cal.mul(a, b)

    @pytest.mark.parametrize(['a', 'b', 'c'], [(2, 1, 2), (-2, -1, 2), (0, 0, 0), (14400, 120, 120), (-2, 2, -1)])
    def test_div(self, a, b, c, setup_and_teardown):
        try:
            c == self.cal.div(a, b)
        except ZeroDivisionError:
            print('被除数为0')
        else:
            assert c == self.cal.div(a, b)
