#!/usr/bin/python3

import os
import argparse
from os.path import isdir


output_header = 'tests.header.toml'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fstests_path', metavar='fstests-path',
            help='path to (x)fstests directory')
    args = parser.parse_args()

    tests_dir = args.fstests_path + '/tests'

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
