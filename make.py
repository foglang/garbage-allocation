#!/bin/python

import os, re, yaml as pyaml

header = """#Garbage allocation
>An outline for how html tags map to fog syntax and constructs

If you have any ideas or suggestions, please make an issue or fork this repo and make a pull request :)

"""
footer = """
##status translations
1 - will never change<br>
2 - we like this feature; unlikely to change<br>
3 - the feature works but has at least one flaw; could change<br>
4 - quick and dirty solution; likely to change<br>
5 - preposition or temporary solution

---

2015 foglang group `github.com/foglang`"""

base_url = 'https://github.com/foglang/garbage-allocation/blob/master/tags/'
table_header = 'html|fog|status\n---:|---|:----:\n'

with open('./README.md', 'w') as readme:
    readme.write(header + table_header)
    for dirname, dirnames, filenames in os.walk('./tags'):
        for filename in filenames:
            if(filename.endswith('.yaml')):
                with open(os.path.join(dirname, filename), 'r') as file:
                    yaml = pyaml.load(file)
                    tag = filename.split('.', 1)[0]
                    readme.write('`<' + tag + '>`|[' + yaml['name'] + '](' + base_url)
                    if('pointsTo' in yaml):
                        tag = yaml['pointsTo']
                    readme.write(tag + '/' + tag + '.yaml)|')
                    if('status' in yaml):
                        readme.write(str(yaml['status']))
                    readme.write('\n')
    readme.write(footer)
