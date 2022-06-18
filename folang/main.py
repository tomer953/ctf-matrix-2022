import json
import re
import matplotlib.pyplot as plt

with open('output.json') as f:
    data = json.load(f)


# postorder visit
def print_leafs(data):
  for item in data['children']:
    if is_leaf(item):
      sum = get_path_sum(item['path'])
      print(sum)
    print_leafs(item)


# return int from 'New Folder (952)' or 0 if not exist
def get_dir_num(str):
  result = re.search(r"Folder \((\d+)\)", str)
  return 0 if result is None else int(result.group(1))

def get_path_sum(str):
  sum = 0
  for name in str.split('/'):
    sum += get_dir_num(name)
  return sum


def is_leaf(item):
  return len(item['children']) == 0

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    if is_leaf(s):
      print(s['path']) 

    for neighbour in s['children']:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


# print_leafs(data)
visited = [] # List to keep track of visited nodes.
queue = [] 
bfs(visited, data, data)
