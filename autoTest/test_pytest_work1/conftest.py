#!/usr/bin/env python
#-- coding:utf-8 --
# Author: latesir
# Date: 2020/6/21
import pytest


@pytest.fixture(scope='session')
def setup_and_teardown():
    yield print('开始计算')
    print('计算结束')

def pytest_addoption(parser):
    mygroup = parser.getgroup("douhui")
    mygroup.addoption("--env",default='test',dest='env',help='douhui add option test')

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default='test')
    if myenv == 'test':
        print('获取测试环境配置信息')
    elif myenv == 'dev':
        print('获取开发环境配置信息')
    elif myenv == 'st':
        print('获取st环境配置信息')