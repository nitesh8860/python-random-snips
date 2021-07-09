import os
import sys

with open('controlscript.log', 'a') as fh:
        fh.write('\nENV_VARS\n')
        for k in os.environ.keys():
                fh.write("%s: %s\n" % (k, os.environ[k]))

