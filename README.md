# Print Binary Tree

Print binary tree in Python

## Usage

```python
# Create Binary Tree
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

# print tree
print_binary_tree(root)

# Output:
          0
     ↙︎         ↘︎
    1           2
  ↙︎   ↘︎       ↙︎   ↘︎
 3     4     5     6
```

## Auto calculate the suitable width

```python
# Create Binary Tree
root = TreeNode("00000")
root.left = TreeNode("00001")
root.right = TreeNode("00002")
root.left.left = TreeNode("00003")
root.left.right = TreeNode("00004")
root.right.left = TreeNode("00005")
root.right.right = TreeNode("00006")

# print tree
print_binary_tree(root)

# Output:
               00000
         ↙︎               ↘︎
     00001               00002
    ↙︎     ↘︎             ↙︎     ↘︎
00003     00004     00005     00006
```

## Customize the node width (`node_width`)

```python
# Create Binary Tree
root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.left.right = TreeNode("e")
root.right.left = TreeNode("f")
root.right.right = TreeNode("g")

# print tree
print_binary_tree(root, node_width=5)

# Output:
                 a
         ↙︎               ↘︎
       b                   c
    ↙︎     ↘︎             ↙︎     ↘︎
  d         e         f         g
```

## Show the tree level number (`show_level_num`)

```python
# Create Binary Tree
root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.left.right = TreeNode("e")
root.right.left = TreeNode("f")
root.right.right = TreeNode("g")

# print tree
print_binary_tree(root, show_level_num=True)

# Output:
1:           a
        ↙︎         ↘︎
2:     b           c
     ↙︎   ↘︎       ↙︎   ↘︎
3:  d     e     f     g
```
