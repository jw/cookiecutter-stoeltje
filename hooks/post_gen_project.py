"""Cookiecutter pre-generation hook."""

TERMINATOR = "\x1b[0m"
ERROR = "\x1b[1;31m[ERROR]"

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_REGEX, module_name):
    print(f"{ERROR}: The project slug ({module_name}) is not a valid Python module name.{TERMINATOR}")
    sys.exit(1)
    