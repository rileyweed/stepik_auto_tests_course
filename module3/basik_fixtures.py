# file basic_fixtures.py
import pytest


def setup():
    print("\t\t\t3 basic setup into module")


def teardown():
    print("\t\t\t3 basic teardown into module")


def setup_module(module):
    print("\n\t1 module setup")


def teardown_module(module):
    print("\t1 module teardown")


def setup_function(function):
    print("\t\t2 function setup")


def teardown_function(function):
    print("\t\t2 function teardown")


def test_numbers_3_4():
    print("\t\t\ttest 3*4")
    assert 3 * 4 == 12


def test_strings_a_3():
    print("\t\t\ttest a*3")
    assert 'a' * 3 == 'aaa'


class TestUM:
    def setup(self):
        print("\t\t\t\t2.2 basic setup into class")

    def teardown(self):
        print("\t\t\t\t2.2 basic teardown into class")

    def setup_class(cls):
        print("\t\t2.0 class setup")

    def teardown_class(cls):
        print("\t\t2.0 class teardown")

    def setup_method(self, method):
        print("\t\t\t2.1 method setup")

    def teardown_method(self, method):
        print("\t\t\t2.1 method teardown")

    def test_numbers_5_6(self):
        print("\t\t\t\ttest 5*6")
        assert 5 * 6 == 30

    def test_strings_b_2(self):
        print("\t\t\t\ttest b*2")
        assert 'b' * 2 == 'bb'