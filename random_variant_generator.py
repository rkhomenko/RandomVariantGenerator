# Copyright (C) 2018 Roman Khomenko

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import random

INT = 1
CHAR = 2
FIRST_ARG = 1
SECOND_ARG = 2


def varinat_list(arg):
    A = ord('a')
    Z = ord('z')
    A1 = ord('а')
    Z1 = ord('я')
    try:
        result = [n + 1 for n in range(int(arg))]
    except ValueError:
        c = ord(arg.lower()[0])
        if A <= c and c <= Z:
            a = A
            z = Z
        elif A1 <= c and c <= Z1:
            a = A1
            z = Z1
        else:
            print('Bad argument "{}"! Unknown charset!'.format(arg))
        result = [str(chr(a + i)) for i in range(c - a + 1)]
    return result


def generate_variant(task_number, variants, matrix):
    n = len(matrix)

    random.seed()
    for i in range(n):
        result = random.choice(variants)
        matrix[i][task_number] = result


if not len(sys.argv) >= 2:
    print('Bad command line arguments!')
    sys.exit(1)

try:
    N = int(sys.argv[FIRST_ARG])
except ValueError:
    print('Bad students count!')
    sys.exit(2)

matrix = [[0 for x in range(len(sys.argv) - SECOND_ARG)] for y in range(N)]

i = 0
for arg in sys.argv[SECOND_ARG:]:
    variants = varinat_list(arg)
    generate_variant(i, variants, matrix)
    i += 1

i = 1
for var in matrix:
    print("{:2}:".format(i), var)
    i += 1
