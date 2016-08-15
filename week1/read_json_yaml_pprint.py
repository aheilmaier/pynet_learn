import json
import yaml
from pprint import pprint as pp

with open("my_list_file.json", "r") as fh:
    new_list = json.load(fh)

print "\npp(new_list) my_list_file.json:\n", pp(new_list)
fh.close()

print 'real pretty pring of json with json.dumps...'
print json.dumps(new_list, sort_keys=True, indent=4, separators=(',', ':'))

with open("my_list_file.yaml", "r") as fh:
    new_list = yaml.load(fh)

print "\npp(new_list) my_list_file.yaml\n", pp(new_list)
fh.close()
