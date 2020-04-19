import json

s= raw_input()

x = list(map(str,s.split(',')))

with open('Blood_grp_O_pos.json', 'w') as json_file:
    json.dump(x, json_file)
