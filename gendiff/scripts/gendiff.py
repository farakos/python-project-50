#!/usr/bin/env python3

import argparse
from gendiff.gendiff import generate_nested_diff
from gendiff.data_parser import parse_data
import gendiff.stylish as stylish


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', dest='formatter', default='stylish',
                        metavar='FORMAT', help='set format of output')
    args = parser.parse_args()

    data = parse_data(args.first_file, args.second_file)
    nested_diff = generate_nested_diff(*data)
    if args.formatter == 'stylish':
        print(stylish.generate_diff(nested_diff))


if __name__ == '__main__':
    main()
