#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/13


from work_webAutoTest.work2.pages.main_page import MainPage


class TestMemberMng():
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.driver.quit()

    def teardown(self):
        self.main.return_mainPage()

    def test_add_member(self):
        assert "bob" in self.main.goto_add_member().add_member('bob').get_members()

    def test_del_member(self):
        assert "bob" not in self.main.goto_contact().del_member().get_members()

    def test_import_contact(self):
        assert "aaa" in self.main.goto_import_contact().import_contact().get_members()
