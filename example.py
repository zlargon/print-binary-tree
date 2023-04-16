#!/usr/bin/env python
from print_binary_tree import TreeNode, print_binary_tree


# create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


print("1. Print binary tree")
print_binary_tree(root)
"""
          1
     ↙︎         ↘︎
    2           3
  ↙︎   ↘︎       ↙︎   ↘︎
 4     5     6     7
"""


print("\n\n2. Print binary tree with customized node width")
print_binary_tree(root, node_width=5)
"""
                 1
         ↙︎               ↘︎
       2                   3
    ↙︎     ↘︎             ↙︎     ↘︎
  4         5         6         7
"""


print("\n\n3. Print binary tree with the level numbers")
print_binary_tree(root, show_level_num=True)
"""
1:           1
        ↙︎         ↘︎
2:     2           3
     ↙︎   ↘︎       ↙︎   ↘︎
3:  4     5     6     7
"""
