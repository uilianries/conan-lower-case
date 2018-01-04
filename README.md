# Conan Lower Case

A simple script to remove/rename remote Conan packages.

#### Install

Before using this Python script, you need to:

1. Install all dependencies:

        pip install .

#### Usage

1. Change directory into the recipe's location (i.e. where conanfile.py is)

        cd conan-libname

2. Execute this script:


To list ALL packages

        conan-lower-case list-all -r remote
         
To list ONLY CamelCase packages

        conan-lower-case list -r remote

To remove ONLY CamelCase packages

        conan-lower-case remove -r remote


#### Testing

1. Install test requirements:

        pip install -r conan_lower_case/requirements_test.txt

2. Execute all test:

        pytest

#### LICENSE
[MIT](LICENSE)
