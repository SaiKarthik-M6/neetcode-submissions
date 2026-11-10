# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        maxVal = root.val

        def dfs(node, maxVal): 
            #base case 
            if node is None: 
                return 0 

            count = 0 
            if node.val >= maxVal: 
                count += 1 
                maxVal = node.val 

            count = count + dfs(node.left, maxVal) + dfs(node.right, maxVal)
            return count 


        result = dfs(root, maxVal)
        return result


            
        