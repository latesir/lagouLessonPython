#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
import pytest
import yaml
from work_appium.work2.pages.app import App
with open('./testData.yaml', 'r', encoding='utf-8') as f:
    testData = yaml.safe_load(f)
    addMemberList = testData['addMember']
    delMemberList = testData['delMember']


class TestWechat:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    def teardown_class(self):
        self.app.close()

    def teardown(self):
        self.main.back_to_main()

    @pytest.mark.parametrize('name,phone,sex', addMemberList)
    def test_addMember(self, name, phone, sex):
        assert '添加成功' == self.main.goto_contact().goto_inviteMember().goto_addMember().enter_name(name).enter_phoneNum(
            phone).choose_sex(sex).click_save()

    @pytest.mark.parametrize('name', delMemberList)
    def test_delMember(self, name):
        assert self.main.goto_contact().goto_memberInfo(name).goto_memberSetting().goto_MemberEdit().\
            click_delMember().click_confirmButton().check_no_member(name) is True
