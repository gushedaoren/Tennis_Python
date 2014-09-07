#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    sys.path.append('/Volumes/D/webserver/Tennis_Python/Tennis_Python')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tennis_Python.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
