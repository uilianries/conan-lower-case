#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import argparse
from conan_lower_case.arguments_parser import ArgumentsParser, Command


def test_valid_remote():
    expected_remote = "foobar"
    command_line = ["-r", expected_remote, "--list"]
    argument_parser = ArgumentsParser(command_line)
    assert expected_remote == argument_parser.remote


def test_default_remote():
    expected_remote = "bincrafters"
    command_line = ["--list"]
    argument_parser = ArgumentsParser(command_line)
    assert expected_remote == argument_parser.remote


def test_empty_command():
    with pytest.raises(argparse.ArgumentError):
        ArgumentsParser([])


def test_supported_commands():
    command_line = ["--list"]
    argument_parser = ArgumentsParser(command_line)
    assert Command.LIST == argument_parser.command
    command_line = ["--list-all"]
    argument_parser = ArgumentsParser(command_line)
    assert Command.LIST_ALL == argument_parser.command
    command_line = ["--remove"]
    argument_parser = ArgumentsParser(command_line)
    assert Command.REMOVE == argument_parser.command
