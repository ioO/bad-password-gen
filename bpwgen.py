#!/bin/env python
import argparse, random

parser = argparse.ArgumentParser(description='Generate numeric password')
parser.add_argument('len', type=int, help='Length of password')

args = parser.parse_args()

password = str()
while len(password) < args.len:
    password = password + str(random.randint(0, 9))

print(password)
