#!/usr/bin/env python
#-- coding:utf-8 --
# Author: latesir
# Date: 2020/6/21
import pytest


@pytest.fixture(scope='session')
def setup_and_teardown():
    yield print('开始计算')
    print('计算结束')