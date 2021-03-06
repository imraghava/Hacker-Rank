# # ==============================================================================
# # Tree Traversals
# # class Node(object):
# #     def __init__(self, data, children):
# #         self.data = data
# #         self.children = children
#     # def find(self, data):
#     #     to_visit =[self]
#     #     while to_visit:
#     #         current = to_visit.pop()
#     #         if current.data == data:
#     #             return current
#     #         to_visit.extend(current.children)

# # Graph Traversals 

# # class PersonNode(object):
# #     def __init__(self, name, adjacent = None):
# #         if adjacent is None:
# #             adjacent = set()  
# #         self.name = name
# #         self.adjacent = adjacent

# # class FriendGraph(object):
# #     def __init__(self):
# #         self.nodes = set()

# #     def add_person(self, person):
# #         self.nodes.add(person)

# #     def set_friends(self, person1, person2):
# #         person1.adjacent.add(person2)
# #         person2.adjacent.add(person1)

# """Maze Traversal"""
# grid =  [[0, 0, 0, 0, 0, 1],
#         [1, 1, 0, 0, 0, 1],
#         [0, 0, 0, 1, 0, 0],
#         [0, 1, 1, 0, 0, 1],
#         [0, 1, 0, 0, 1, 0],
#         [0, 1, 0, 0, 0, 2]]

# def find_end(x, y):
#     if grid[x][y] == 2:
#         print "Found goal at {}, {}".format(x, y)
#         return True
#     elif grid[x][y] == 1:
#         print "Found wall at {}, {}".format(x, y)
#         return False
#     elif grid[x][y] == 3:
#         print "Visited at {}, {}".format(x, y)
#         return False

#     print "visted {} {}".format(x, y)

#     grid[x][y] = 3 # convert 0 to visited
#     if ((x < len(grid)-1 and find_end(x+1, y))
#         or (y > 0 and find_end(x, y-1))
#         or (x > 0 and find_end(x-1, y))
#         or (y < len(grid)-1 and find_end(x, y+1))):
#         return True
#     return False

# find_end(0, 0)



# # ==============================================================================
# graph = {'A': ['B', 'C'],
#              'B': ['C', 'D'],
#              'C': ['D'],
#              'D': ['C'],
#              'E': ['F'],
#              'F': ['C']}

# def find_path(graph, start, end, path=[]):
#     path += [start]
#     print "path", path
#     if start == end:
#         return path 
#     if not graph.has_key(start):
#         return None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#         if newpath:
#             return newpath
#     return None

# print find_path(graph, 'A', 'D')

# def find_shortest_length_path(graph, start, end, path=[]):
#     path += [start]
#     print "path", path
#     if start == end:
#         return path 
#     if not graph.has_key(start):
#         return None
#     shortest = None 
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_shortest_length_path(graph, node, end, path)
#             if newpath:
#                 if not shortest or len(newpath) < len(shortest):
#                     shortest = newpath
#     return shortest

# print find_shortest_length_path(graph, 'A', 'D')
# ==============================================================================
map = [
       [1, 2, 1],
       [1, 50, 50],
       [3, 4, 5]]

def find_shortest_path(map):
  rows = len(map)
  cols = len(map[0])
  copy_map = [rows]
  
  # keeps a rolling sum 
  copy_map = map[0][0]
  
  # go down the first col 1 1 3
  for y in range(1, cols-1): 
    # y-1 for index 0,0 
    copy_map[0][y] = int(map[0][y-1]) + int(map[0][y])

  # go across the first row 1 1 1     
  for x in range(1, rows-1): # 1 
    copy_map[x][0] = int(map[x-1][0]) + int(map[x][0])    

  for x in range(1, rows-1):
    for y in range(1, cols-1):
      
        copy_map[x][y] = map[x][y]  + min(copy_map[x-1][y], copy_map[x][y-1]) 
      
    return copy_map[rows - 1][cols - 1]

print find_shortest_path(map)
# //        [1, 3, 4],
# //        [2, 52, 54],
# //        [5, 9, 14]  