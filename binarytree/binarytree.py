#!/usr/bin/env python3
from collections import deque

class BinaryTree(object):
    '''
    A binary tree.
    '''
    def __init__(self):
        self.root = None


    def __repr__(self):
        return repr(self.root)

    top = 0
    p = 0
    def set(self, key, value):
        '''
        Adds the given key=value pair to the tree.
        '''
        #TODO
        if self.root == None:
            self.root = Node(None,key,value)
            if self.top != 0:
                self.root = self.top
            if self.p != 0:
                self.root.parent = self.p
            

        else:
            if self.root.parent == None:
                self.top = self.root
            n = self.root
            if key < n.key:
                if n.left is None:
                    n.left = Node(n,key,value)
                    self.root = self.top
                    self.p = 0
                    return
                else:
                    self.p = n
                    self.root = n.left
                    return self.set(key,value)
            else:   
                if n.right is None:
                    n.right = Node(n,key,value)
                    self.root = self.top
                    self.p = 0
                    return
                else:
                    self.p = n
                    self.root = n.right
                    return self.set(key,value)
            


    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        #TODO
        out = self._find(key)
        if out == None:
            return None
        else:
            return out.value


    def remove(self, key):
        '''
        Removes the given key from the tree.
        Returns silently if the key does not exist.
        '''
        #TODO
        re = self._find(key)
        p = re.parent
        if re.left is None and re.right is None:
            if re.key < p.key:
                p.left = None
            else:
                p.right = None
            return
        if re.left is None and re.right is not None:
            if re.key < p.key:
                p.left = re.right
            else:
                p.right = re.right
            return
        if re.left is not None and re.right is None:
            if re.key < p.key:
                p.left = re.left
            else:
                p.right = re.left
            return
        if re.left is not None and re.right is not None:
            mini = self.fm(re)
            re.key = mini.key
            mini.parent.left = None
            return

    def walk_dfs_inorder(self, node=None):
        '''
        An iterator that walks the tree in DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        
        return self.inorder(self.root)

    def inorder(self, node):
        if not node:
            return []

        yield from self.inorder(node.left)
        yield (node.key,node.value)
        yield from self.inorder(node.right)

    def walk_dfs_preorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in preorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        return self.preorder(self.root)
    
    def postorder(self, node):
        if not node:
            return []

        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield (node.key,node.value)
        


    def walk_dfs_postorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in inorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        return self.postorder(self.root)

    def preorder(self, node):
        if not node:
            return []

        yield (node.key,node.value)
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)


    def walk_bfs(self):
        '''
        An iterator that walks the tree in BFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            yield (queue[0].key,queue[0].value)
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return []





    ##################################################
    ###   Helper methods


    def fm(self, n):
        '''
        Internal method to remove a node from its parent
        '''
        #TODO: feel free to use or remove this method
        if n.right is not None:
            n = n.right
        else:
            return n
        if n.left is not None:
            return self.fm(n.left)
        else:
            return n


    def _find(self, key):
        '''
        Internal method to find a node by key.
        Returns (parent, node).
        '''
        #TODO: feel free to use or remove this method
        if self.root.parent == None:
            self.top = self.root
        if self.root.key == key:
            reval = self.root
            self.root = self.top
            self.top = 0
            return reval
        elif key < self.root.key and self.root.left is not None:
            self.root = self.root.left
            return self._find(key)
        elif key >= self.root.key and self.root.right is not None:
            self.root = self.root.right
            return self._find(key)
        else:
            return None



class Node(object):
    '''
    A node in a binary tree.
    '''
    def __init__(self, parent, key, value):
        '''Creates a linked list.'''
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        result = []
        def recurse(node, prefix1, side, prefix2):
            if node is None:
                return
            result.append(prefix1 + node.key + side)
            if node.right is not None:
                recurse(node.left, prefix2 + '\u251c\u2500\u2500 ', ' \u2c96', prefix2 + '\u2502   ')
            else:
                recurse(node.left, prefix2 + '\u2514\u2500\u2500 ', ' \u2c96', prefix2 + '    ')
            recurse(node.right, prefix2 + '\u2514\u2500\u2500 ', ' \u1fe5', prefix2 + '    ')
        recurse(self, '', '', '')
        return '\n'.join(result)
