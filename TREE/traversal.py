"""LEFT -> ROOT -> RIGHT"""


def in_order(root):
    output = []
    if root is not None:
        output = in_order(root.left)
        output.append(root.data)
        output += in_order(root.right)
    return output


"""ROOT -> LEFT -> RIGHT"""


def pre_order(root):
    output = []
    if root is not None:
        output.append(root.data)
        output += pre_order(root.left)
        output += pre_order(root.right)
    return output


"""LEFT -> RIGHT -> ROOT"""


def post_order(root):
    output = []
    if root is not None:
        output = post_order(root.left)
        output += post_order(root.right)
        output.append(root.data)
    return output
