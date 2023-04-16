from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.role: int = None


def print_binary_tree(
    root: TreeNode, node_width: Optional[int] = None, show_level_num=False
) -> None:
    # tree node roles
    ROOT = 0
    LEFT = 1
    RIGHT = 2

    # -------------------------------------------
    # Get inorder list (DFS)
    # -------------------------------------------
    inorder_list: list[TreeNode] = []
    stack: list[TreeNode] = []
    max_val_len = -1

    root.role = ROOT
    node = root
    while True:
        if node:
            stack.append(node)

            node = node.left
            if node:
                node.role = LEFT
            continue

        if len(stack) > 0:
            node = stack.pop()
            inorder_list.append(node)
            max_val_len = max(max_val_len, len(str(node.val)))

            node = node.right
            if node:
                node.role = RIGHT
            continue

        break

    # -------------------------------------------
    # Get node width. Default is 3
    # -------------------------------------------
    node_width = node_width or max(max_val_len, 3)
    BLANK = " " * node_width
    arrow_of = {
        ROOT: BLANK,
        LEFT: BLANK[1:] + "↙︎",
        RIGHT: "↘︎" + BLANK[1:],
    }

    # -------------------------------------------
    # Print binary tree (BFS)
    # -------------------------------------------
    level = 1
    queue = deque([root])
    next_queue = deque()
    while len(queue) > 0:
        # Find the position of the node in a line
        node_set = set(queue)
        line: list[Optional(TreeNode, None)] = list(
            map(lambda n: n if n in node_set else None, inorder_list)
        )

        # Print first line with arrows
        if show_level_num:
            print("   ", end="")
        for node in line:
            print(arrow_of[node.role] if node else BLANK, end="")
        print()

        # Print second line with values
        if show_level_num:
            text = str(level) + ":"
            print(f"{text:<3}", end="")
        for node in line:
            print(f"{node.val:^{node_width}}" if node else BLANK, end="")
        print()

        # Add node's children to the next queue
        while len(queue) > 0:
            node = queue.popleft()

            if node.left:
                next_queue.append(node.left)

            if node.right:
                next_queue.append(node.right)

        # Swap queue and next_queue for next loop
        queue, next_queue = next_queue, queue
        level += 1
    print()
