from trees.node_tree import BinaryTree
from linear_structures.stacks import Stack
import operator

def build_parse_tree(fp_expr):
    fp_list = fp_expr.split()
    parent_stack = Stack()
    expr_tree = BinaryTree("")
    parent_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == '(':
            current_tree.insert_left("")
            parent_stack.push(current_tree)
            current_tree = current_tree.left_child
        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            parent_stack.push(current_tree)
            current_tree = current_tree.right_child
        elif i.isdigit():
            current_tree.root = int(i)
            parent = parent_stack.pop()
            current_tree = parent
        elif i == ')':
            current_tree = parent_stack.pop()
        else:
            raise ValueError(f"Unknown operator {i}")
    
    return expr_tree

def evaluate(pt):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    left_child = pt.left_child
    right_child = pt.right_child
    if left_child and right_child:
        fn = operators[pt.root]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return pt.root
    
def eval_w_post_order(pt):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    result_1 = None
    result_2 = None
    if pt:
        result_1 = eval_w_post_order(pt.left_child)
        result_2 = eval_w_post_order(pt.right_child)
        if result_1 and result_2:
            return operators[pt.key](result_1, result_2)
        return pt.key

    

if __name__ == '__main__':
    pt = build_parse_tree('( ( 10 + 5 ) * 3 )')
    print(evaluate(pt))
    print(eval_w_post_order(pt))
