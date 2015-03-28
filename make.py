#!/bin/python

import os, re

header = '#Garbage allocation\nAn outline for how html tags map to fog syntax and constructs\n\n'
footer = '\n2015 foglang group `github.com/foglang`'
base_url = 'https://github.com/foglang/garbage-allocation/blob/master/'
table_header = 'html|fog\n---:|---\n'

with open('./README.md', 'w') as readme:
    readme.write(header + table_header)
    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if(filename.endswith('.yml')):
                with open(os.path.join(dirname, filename), 'r') as source:
                    yaml = source.read()
                    tag = filename.split('.', 1)[0]
                    firstValueI = yaml.index('"') + 1
                    name = yaml[firstValueI:yaml.index('"', firstValueI)]
                    readme.write('`<' + tag + '>`|[' + name + '](' + base_url + tag + '/' + tag + '.yml)\n');
    readme.write(footer)
