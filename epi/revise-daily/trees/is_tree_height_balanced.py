import math


def is_tree_height_balanced(root):

    if not root:
        return True, 0

    is_left_tree_balanced, l_height = is_tree_height_balanced(root.left)
    is_right_tree_balanced, r_height = is_tree_height_balanced(root.right)

    if is_left_tree_balanced and is_right_tree_balanced and math.abs(l_height - r_height) <= 1:
        return True, max(l_height, r_height) + 1

    return False, max(l_height, r_height) + 1