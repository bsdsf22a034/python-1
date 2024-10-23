class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert_element_root(self, element):
        self.root = Node(element)
    def insert_left_child(self, parent, child):
        parent.left = Node(child)
    def insert_right_child(self, parent, child):
        parent.right = Node(child)
    def delete_element(self, element):
        pass
    def display_pre_order(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.display_pre_order(node.left)
            self.display_pre_order(node.right)
    def display_in_order(self, node):
        if node is not None:
            self.display_in_order(node.left)
            print(node.value, end=" ")
            self.display_in_order(node.right)
    def display_post_order(self, node):
        if node is not None:
            self.display_post_order(node.left)
            self.display_post_order(node.right)
            print(node.value, end=" ")
    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    def min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value
    def count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)

    def non_rec_pre_order(self):
        stack = []
        current = self.root
        while stack or current:
            if current:
                print(current.value, end=" ")
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
    def non_rec_post_order(self):
        stack = []
        current = self.root
        last_visited = None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right is not None and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    print(peek_node.value, end=" ")
                    last_visited = stack.pop()
    def non_rec_in_order(self):
        stack = []
        current = self.root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.value, end=" ")
                current = current.right
    def find_balance_factor(self, node):
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        return height(node.left) - height(node.right)
    def display_ancestors(self, node_data):
        def find_ancestors(root, target):
            if root is None:
                return False
            if root.value == target:
                return True
            if (find_ancestors(root.left, target) or find_ancestors(root.right, target)):
                print(root.value, end=" ")
                return True
            return False
        find_ancestors(self.root, node_data)
    def display_descendants(self, node_data):
        def find_descendants(node, target):
            if node is None:
                return
            if node.value == target:
                print(node.value, end=" ")
            find_descendants(node.left, target)
            find_descendants(node.right, target)
        find_descendants(self.root, node_data)

    def height_of_tree(self):
        def calculate_height(node):
            if node is None:
                return 0
            left = calculate_height(node.left)
            right = calculate_height(node.right)
            return 1 + max(left, right)
        return calculate_height(self.root)
tree = BinaryTree()
tree.insert_element_root(5)
tree.insert_left_child(tree.root, 3)
tree.insert_right_child(tree.root, 8)
tree.insert_left_child(tree.root.left, 2)
tree.insert_right_child(tree.root.left, 4)
tree.insert_left_child(tree.root.right, 7)
print("Pre-order traversal:")
tree.display_pre_order(tree.root)
print("\nIn-order traversal:")
tree.display_in_order(tree.root)
print("\nPost-order traversal:")
tree.display_post_order(tree.root)
print("Number of nodes:", tree.count_nodes())
print("Minimum value:", tree.min_value(tree.root))
print("Number of leaf nodes:", tree.count_leaf_nodes(tree.root))
print("Height of the tree:", tree.height_of_tree())
