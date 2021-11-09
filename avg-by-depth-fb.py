class Node(object):
    def __init__(self, v):
      self.val = v
      self.left = None
      self.right = None

def _collect(node, data, depth = 0): # helper collection function (private, modularize)
  if not node:
    return None
  
  if depth not in data:
    data[depth] = []
    
  data[depth].append(node.val)
  
  _collection(node.left, data, depth + 1)
  _collection(node.right, data, depth + 1)
  
  
def avg_by_depth(root: node):
  data = {}
  _collect(node, data)
  
  result = []
  
  i = 0
  while i in data:
    nums = data[i]
    avg = sum(nums) / len(nums)
    result.append(avg)
    i += 1
    
 return result
