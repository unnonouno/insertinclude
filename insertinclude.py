#!/usr/bin/env python

import os
import sys

def usage():
    print "insertinclude.py PROJECT FILE"

if len(sys.argv) != 3:
    usage()
    sys.exit(1)

project = sys.argv[1]
file = sys.argv[2]

path = os.path.abspath(file)
dirs = path.split('/')

if 'src' in dirs:
    begin = dirs.index('src') + 1
else:
    begin = 0
var = (project + '_' + '_'.join(dirs[begin:])).upper().replace('.', '_') + '_'

lines = []
with open(file) as f:
    for line in f:
        lines.append(line)

inserted = False
with open(file, 'w') as f:
    for l in lines:
        if "#pragma once" in l:
            f.write('#ifndef %s\n' % var)
            f.write('#define %s\n' % var)
            f.write('\n')
            inserted = True
        else:
            f.write(l)

    if inserted:
        f.write('\n')
        f.write('#endif  // %s\n' % var)

