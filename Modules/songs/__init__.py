# __all__=["nepali","english","chinese"]

from os.path import dirname,  basename, isfile, join
import glob

all_files=glob.glob(join(dirname(__file__),"*.py"))

for name in all_files:
    a=basename(name)[:-3]
print(a)


