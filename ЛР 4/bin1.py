from collections import deque


def gen_bin_tree(
        height: int,
        root: int,
        left_branch=lambda x: x * 3,
        right_branch=lambda x: x - 4
) -> dict:

    if height < 1:
        return {}
    if height == 1:
        return {str(root): {}}

    tree = {str(root): {}} #корень дерева

    #Очередь: (родительский словарь, значение узла, текущая глубина)
    queue = deque()
    queue.append((tree, root, 1))

    while queue:
        parent_dict, value, depth = queue.popleft()

        if depth < height:
            #Вычисляем потомков с помощью переданных лямбда-функций
            left_val = left_branch(value)
            right_val = right_branch(value)

            #Создаём узел с детьми
            node = {
                "left leaf": {str(left_val): {}},
                "right leaf": {str(right_val): {}}
            }
            parent_dict[str(value)] = node

            queue.append((node["left leaf"], left_val, depth + 1))
            queue.append((node["right leaf"], right_val, depth + 1))
        else:
            parent_dict[str(value)] = {}

    return tree

print(gen_bin_tree(4,7))