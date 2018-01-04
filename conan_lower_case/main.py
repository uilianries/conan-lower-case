#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Read user arguments and run the app
'''
import sys
from conan_lower_case.remote_handler import RemoteHandler
from conan_lower_case.arguments_parser import ArgumentsParser


def run():
    try:
        arguments = ArgumentsParser()
        remote_handler = RemoteHandler()
        remote_handler.run(arguments.command, arguments.remote)
    except Exception as e:
        print("An error has occured! %s" % e)
        sys.exit(1)


if __name__ == "__main__":
    run()
