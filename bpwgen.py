#!/bin/env python
import argparse, random

parser = argparse.ArgumentParser(description='Generate numeric password')
parser.add_argument('len', type=int, help='Length of password')

args = parser.parse_args()

password = ''.join('%d' % random.randint(0,9) for i in xrange(args.len))

print(password)
