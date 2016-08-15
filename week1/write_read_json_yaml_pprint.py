import json
import yaml
from pprint import pprint as pp

my_list = range(8)
my_list.append('elem9')
my_list.append('elem10')
my_list.append({})
my_list[-1]['ip_addr'] = '10.1.1.1'
my_list[-1]['mask'] = '255.255.255.0'
my_list[-1]['attribs'] = range(5)

with open("my_list_file.json", "w") as fh:
    json.dump(my_list, fh)

fh.close()

with open("my_list_file.yaml", "w") as fh:
    #fh.write(yaml.dump(my_list, default_flow_style=False, explicit_start=True))
    yaml.dump(my_list, fh, default_flow_style=False, explicit_start=True)

fh.close()

# read yson file and print it "pretty"
with open("my_list_file.json", "r") as fh:
    new_list = json.load(fh)

print "\npp(new_list) my_list_file.json:\n", pp(new_list)
fh.close()
print 'real pretty pring of json with json.dumps...'
print json.dumps(new_list, sort_keys=True, indent=4, separators=(',', ':'))

# read yaml file and print it "pretty"
with open("my_list_file.yaml", "r") as fh:
    new_list = yaml.load(fh)

print "\npp(new_list) my_list_file.yaml\n", pp(new_list)
fh.close()

print 'real pretty pring of json with yaml.dumps...'
print yaml.dump(new_list, explicit_start=True, default_flow_style=False)
