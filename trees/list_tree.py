"""
my_tree = [
    "a",  # root
        ["b",  # left subtree
            ["d", [], []],
            ["e", [], []]
        ],
        ["c",  # right subtree
            ["f", [], []],
            []
        ],
    ]

root = my_tree[0]
left_subtree = my_tree[1]
right_subtree = my_tree[2]    
"""

def make_binary_tree(root):
    return [root, [], []]

def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root

def insert_right(root, new_child):
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def build_tree():
    tree = make_binary_tree("a")
    insert_left(tree, "b")
    insert_right(get_left_child(tree), "d")
    insert_right(tree, "c")
    insert_left(get_right_child(tree), "e")
    insert_right(get_right_child(tree), "f")
    return tree

if __name__ == '__main__':
    tree = make_binary_tree(3)
    insert_left(tree, 4)
    insert_left(tree, 6)
    insert_right(tree, 7)
    insert_right(tree, 8)
    print(tree)

    left = get_left_child(tree)
    set_root_val(tree, 10)
    print(tree)
    print(build_tree())