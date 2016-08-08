import yaml

my_list = range(8)
my_list.append('elem9')
my_list.append('elem10')
my_list.append({})
my_list[-1]['ip_addr'] = '10.1.1.1'
my_list[-1]['mask'] = '255.255.255.0'
my_list[-1]['attribs'] = range(5)

print my_list
# ugly print
print yaml.dump(my_list)
print yaml.dump(my_list, default_flow_style=True)

with open("my_list_file.yaml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))
