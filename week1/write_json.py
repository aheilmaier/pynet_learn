import json
from pprint import pprint as pp

my_list = range(8)
my_list.append('elem9')
my_list.append('elem10')
my_list.append({})
my_list[-1]['ip_addr'] = '10.1.1.1'
my_list[-1]['mask'] = '255.255.255.0'
my_list[-1]['attribs'] = range(5)

print "\nraw input:\n", my_list
# ugly print
print "\njson.dumps(my_list):\n", json.dumps(my_list)
print "\njson.dumps(my_list, sort_keys=True, indent=4, separators=(',',':')):\n", json.dumps(my_list, sort_keys=True, indent=4, separators=(',',':'))

with open("my_list_file.json", "w") as fh:
    json.dump(my_list, fh)

fh.close()

with open("my_list_file.json", "r") as fh:
    new_list = json.load(fh)

print "\nprint the read in file:\n", new_list
print "\npprint the read in file:\n", pp(new_list)
