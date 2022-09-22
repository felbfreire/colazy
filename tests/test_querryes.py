from colazy.wrappers import querry_db
from colazy.utils import exec_script

import example

import pytest


exec_script()


class TestQuerryes():

    def test_insert_name(self):
        example.insert_name()


    def test_get_names(self):
        names = example.get_names()

        assert names == [(1, "Fred", "Nit")]


    def test_update_names(self):
        example.update_name()

        names = example.get_names()

        assert names == [(1, "John", "Nit")]


    def test_delete_names(self):
        example.delete_name()

        names = example.get_names()

        assert names == []
