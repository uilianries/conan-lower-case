#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import ArgumentError
from enum import Enum


class Command(Enum):
    LIST = 1
    LIST_ALL = 2
    REMOVE = 3


class ArgumentsParser(object):

    def __init__(self, *args):
        parser = argparse.ArgumentParser(description="A simple script to remove/rename remote Conan packages.")

        group = parser.add_mutually_exclusive_group()
        group.add_argument('--list-all', action='store_const', dest='command', const=Command.LIST_ALL, help='List all remote packages')
        group.add_argument('--list', action='store_const', dest='command', const=Command.LIST, help='List only camel case packages from remote')
        group.add_argument('--remove', action='store_const', dest='command', const=Command.REMOVE, help='Remove only camel case packages from remote')

        parser.add_argument("-r", "--remote",
                            default="bincrafters",
                            help='Remote alias to Conan server')

        self._arguments = parser.parse_args(*args)

        if self.command is None:
            raise ArgumentError(None, "Command must be valid.")

    @property
    def command(self):
        return self._arguments.command

    @property
    def remote(self):
        return self._arguments.remote
