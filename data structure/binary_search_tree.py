from __future__ import annotations
from typing import Any, Type

class Node:
    # node
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        # constructor
        self.key = key # key
        self.value = value # value
        self.left = left # left pointer
        self.right = right # right pointer

class BinarySearchTree:
    # tree
    def __init__(self):
        
        self.root = None # root

    def search(self, key: Any) -> Any:
        # find a node with key
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        # add node with key and value

        def add_node(node: Node, key: Any, value: Any) -> None:
            # inner function that appends node into its subtree
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True

        # search for node with key
        while True:
            if p is None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:
            # right child become root if node is root
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else: # two child nodes
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self) -> None:
        # inorder
        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)
        
        print_subtree(self.root)

    def min_key(self) -> Any:
        
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key
    
    def max_key(self) -> Any:
        
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key