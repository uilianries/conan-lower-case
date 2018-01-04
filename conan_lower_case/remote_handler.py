#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from conans.client.conan_api import ConanAPIV1
from conan_lower_case.arguments_parser import Command


class RemoteHandler(object):

    def __init__(self):
        self._conan_api, _, _ = ConanAPIV1.factory()

    def run(self, command, remote):
        if command == Command.LIST:
            recipes = self._list_camel_case(remote)
            RemoteHandler._print_recipes(recipes)
        elif command == Command.LIST_ALL:
            recipes = self._list_all(remote)
            RemoteHandler._print_recipes(recipes)
        elif command == Command.REMOVE:
            self._remove_camel_case(remote)
        else:
            raise Exception("Invalid command! %s" % command)

    def _list_all(self, remote):
        print("GETTING DATA FROM REMOTE...")
        return self._conan_api.search_recipes(pattern="*", remote=remote)

    def _list_camel_case(self, remote):
        recipes = self._list_all(remote)
        filtered_recipes = []
        for recipe in recipes:
            if RemoteHandler._is_camel_case(recipe.name):
                filtered_recipes.append(recipe)
        return filtered_recipes

    def _remove_camel_case(self, remote):
        recipes = self._list_camel_case(remote)
        print("WARNING!")
        print("THE FOLLOW RECIPES/PACKAGES WILL BE REMOVED!!!")
        RemoteHandler._print_recipes(recipes)
        text = input("DO YOU WANT TO CONTINUE [Y]? ")
        if text.lower() == "y" or text.lower() == "yes":
            print("REMOVING ALL PACKAGES!")
            for recipe in recipes:
                self._conan_api.remove(str(recipe), force=True, remote=remote)
        else:
            print("COMMAND CANCELED.")

    @staticmethod
    def _is_camel_case(package_ref):
        return re.match(r'[A-Z]+', package_ref)

    @staticmethod
    def _print_recipes(recipes):
        print("=== REMOTE RECIPES: ===")
        for recipe in recipes:
            print(str(recipe))
