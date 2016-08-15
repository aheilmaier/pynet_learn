import yaml
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
print "\nyaml.dump(my_list)\n", yaml.dump(my_list)
print "\nyaml.dump(my_list)\n", yaml.dump(my_list, default_flow_style=True)

with open("my_list_file.yaml", "w") as fh:
    #fh.write(yaml.dump(my_list, default_flow_style=False, explicit_start=True))
    yaml.dump(my_list, fh, default_flow_style=False, explicit_start=True)
    
fh.close()

with open("my_list_file.yaml", "r") as fh:
    new_list = yaml.load(fh)

print "\nprint the read in file:\n", new_list
print "\npprint the read in file:\n", pp(new_list)
