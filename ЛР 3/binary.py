def gen_bin_tree(height: int, root: int) -> dict:
    if height < 1:
        return {}
    if height == 1:
        return {str(root): {}}  # Лист без детей
    return {
        str(root): {
            "left leaf": gen_bin_tree(height - 1, root * 3),
            "right leaf": gen_bin_tree(height - 1, root - 4)
        }
    }

# tree = (gen_bin_tree(4, 7))
# import pprint
# pprint.pprint(tree)

print(gen_bin_tree(4, 7))

