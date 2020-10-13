# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inorderTraversal(self, root):
    nodeList = []
    self.dfs(root, nodeList)
    return nodeList
  def dfs(self, root, nodeList):
    if not root:
      return
    self.dfs(root.left, nodeList)
    nodeList.append(root.val)
    self.dfs(root.right, nodeList)