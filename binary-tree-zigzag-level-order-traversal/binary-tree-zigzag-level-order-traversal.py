from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        
        leftToRight = True              # flag is out here so it doesn't get reset in while loop
        while queue:
            level_size = len(queue)
            current_level = deque()     #zigzag order (append left or right accourding to bool)
            
            for _ in range(level_size):
                current_node = queue.popleft()
                
                if leftToRight:
                    current_level.append(current_node.val)
                else:
                    current_level.appendleft(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                    
                if current_node.right:
                    queue.append(current_node.right)
            
            result.append(list(current_level))
            leftToRight = not leftToRight
        
        return result
            
            