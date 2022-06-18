import json

with open('output.json') as f:
    data = json.load(f)

def print_leafs(data):
  for item in data['children']:
    if (len(item['children']) == 0):
      print(item['path'])
    print_leafs(item)


print_leafs(data)