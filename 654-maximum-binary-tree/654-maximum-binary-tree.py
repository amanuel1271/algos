# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        index_map = {nums[i]:i for i in range(len(nums))}
        
        ## to avoid unnecessary copying
        def maxIndex(i,j):
            maxi = i
            for k in range(i+1,j+1):
                if nums[k] > nums[maxi]:
                    maxi = k
                    
            return maxi
            
        
        def helper(i,j):
            if i > j:
                return None
            
            max_index = maxIndex(i,j)
            root = TreeNode(nums[max_index])
            root.left = helper(i,max_index-1)
            root.right = helper(max_index + 1,j)
            return root
            
        
        return helper(0,len(nums)-1)