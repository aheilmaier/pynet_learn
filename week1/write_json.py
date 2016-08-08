import json

my_list = range(8)
my_list.append('elem9')
my_list.append('elem10')
my_list.append({})
my_list[-1]['ip_addr'] = '10.1.1.1'
my_list[-1]['mask'] = '255.255.255.0'
my_list[-1]['attribs'] = range(5)

print my_list
# ugly print
print json.dumps(my_list)
print json.dumps(my_list, sort_keys=True, indent=4, separators=(',',':'))

with open("my_list_file.json", "w") as f:
    json.dump(my_list, f)
