#!/usr/bin/env python3

"""utils.py: Generic utility multi-platform functions."""

import csv
import gzip
import allel
import psutil
import pathlib


def get_cpu_count():
    """ Return physical (without hyperthreading) cpu core count """
    return psutil.cpu_count(logical=False)


def get_memory():
    return psutil.virtual_memory()
