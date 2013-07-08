#!/bin/env python

# This program generates a numeric password from the length you pass.
# This is a bad idea to use numeric password but sometimes some website doesn't
# allow you another solution.
# So I dedicated this licence to this kind of website :

#               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                       Version 2, December 2004

# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

#               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#       TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

# 0. You just DO WHAT THE FUCK YOU WANT TO.

import argparse, random

parser = argparse.ArgumentParser(description='Generate numeric password')
parser.add_argument('len', type=int, help='Length of password')

args = parser.parse_args()

password = str()
while len(password) < args.len:
    password = password + str(random.randint(0, 9))

print(password)
