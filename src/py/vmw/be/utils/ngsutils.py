#!/usr/bin/env python3

"""ngsutils.py: NGS-specific functions to read csv or vcf files."""

import io
import os
import csv
import gzip
import allel
import psutil
import pathlib


def get_common_headers(files, filter_list=[]):
    """ Return a list of intersecting headers found in files """
    intersecting_headers = []
    for fp in files:
        try:
            headers = get_file_headers(fp, filter_list)
        except RuntimeError:
            raise

        # if intersect list is empty, concat lists otherwise take intersecting elements
        if (len(intersecting_headers) == 0):
            intersecting_headers += headers
        else:
            intersecting_headers = list(set(intersecting_headers).intersection(headers))

    return intersecting_headers


def get_file_headers(file, filter_list=[]):
    """ Return headers in csv or vcf files """
    headers = []
    try:
        if str.lower(pathlib.Path(file).suffix) == '.csv':
            with open(file, 'r') as f:
                reader = csv.reader(f)
                headers = next(reader)
        elif str.lower(pathlib.Path(file).suffix) in ['.vcf', '.gz']:
            try:
                df = allel.vcf_to_dataframe(file, fields='*', alt_number=1)
                headers = list(df.columns.values)
            except RuntimeError:
                try:
                    with gzip.open(file, 'rt') as f:
                        reader = csv.reader(f)
                        headers = next(reader)
                except Exception:
                    print('>>> {0} <<<'.format(file))
                    raise RuntimeError('File format wasn\'t recognised')
        else:
            print('>>> {0} <<<'.format(file))
            raise RuntimeError('Incorrect file format')
    except FileNotFoundError:
        print('>>> {0} <<<'.format(file))
        raise RuntimeError("File not found!")

    # filter list from unwanted characters
    file_headers = [x for x in headers if str.strip(x) not in filter_list]

    return file_headers
