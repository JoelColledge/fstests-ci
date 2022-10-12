#!/usr/bin/python3

import os
import argparse
from os.path import isdir


tests_dir = 'xfstests/tests'
output_header = 'tests.header.toml'

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    # Read test files
    test_names = []
    for dir_name in os.listdir(tests_dir):
        if not isdir(tests_dir + '/' + dir_name):
            continue
        for name in os.listdir(tests_dir + '/' + dir_name):
            if len(name) != 3:
                continue
            test_names.append(dir_name + '/' + name)

    # Write header
    with open(output_header) as f:
        print(f.read().rstrip())

    # Write tests
    for name in sorted(test_names):
        print('[tests.{}]'.format(name.replace('/', '_')))
        print('vms = [1]')
        print()


if __name__ == '__main__':
    main()
