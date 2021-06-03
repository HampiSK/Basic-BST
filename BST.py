""" Basic BST code for inserting and printing a tree
"""

import math

""" Node class
"""
class Node:
    ''' CONSTRUCTOR 
        Optional:
        @param [data] - value of node, None otherwise
    '''
    def __init__(self, data = None): 
        self.data = data             # Assign node value
        self.left = None             # Point to node on the left
        self.right = None            # Point to node on the right

""" BST class with insert and display methods. display pretty prints the tree
"""
class BinaryTree:
    ''' CONSTRUCTOR
    Construct class
    '''
    def __init__(self):
        self.root = None    # Init empty tree
    ''' INSERT
    Insert node into tree
    @param [data] - Value to be inserted into tree
    '''
    def insert(self, data):
        if self.root is None:             # When tree is empty first value will be inserted in top
            self.root = Node(data)
        else:
            self._insert(data, self.root) # Insert value in tree in correct position
    ''' INTERNAL INSERT
    Recursively insert value into correct position in tree
    @param [data]     - Value to be inserted into tree
    @param [cur_node] - Current root of the tree
    '''
    def _insert(self, data, cur_node):
        if data < cur_node.data:                 # Move under smaller root
            if cur_node.left is None:            # When next root doesnt exist
                cur_node.left = Node(data)       # Assign as next left root
            else:
                self._insert(data,cur_node.left) # Move on to next root on the left
        elif data > cur_node.data:               # Move under bigger root
            if cur_node.right is None:           # When next root doesnt exist
                cur_node.right = Node(data)      # Assign as next right root
            else:
                self._insert(data,cur_node.right)# Move on to next root on the right
        else:
            print("Value already present in tree")

    ''' DISPLAY TREE 
    @param [cur_node] - Display tree from this node
    '''
    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node) # Get tree in normalized shape
        for line in lines:                       # Print tree
            print(line)
    '''BST SEARCH ITERATION
    Basic BTS search using iteration
    @param [target]   - Search number in tree
    @return {boolian} - True if value is in tree, otherwise False   
    '''
    def find_i(self, target):               
        cur_node = self.root                # Assign Tree into variable
        while cur_node is not None:         # Loop until cur_node is None
            if cur_node.data is target:     # Compare if Node value is same as target value
                return True                 # Return true
            elif cur_node.data > target:    # Compare if Node value is higher then target value
                cur_node = cur_node.left    # Assign Node on left connected to Node value into cur_node
            else:                           
                cur_node = cur_node.right   # Assign Node on right connected to Node value into cur_node
        return False                        # Retrun false when value was not found in tree                          
    '''RECONSTRUCT TREE
    Reconstruct tree around deleted node
    @param [node]     - Node to delete
    '''
    def _left_right(self,node):
        delNodeParent = node                # Assign node as parent
        delNode = node.right                # Node on right 

        while delNode.left:                 # Until node on the left is not None, gets lowest value
            delNodeParent = delNode         # Get parent of last left node
            delNode = delNode.left          # Will be last left node
        
        node.data = delNode.data            # Assign node bellow to current node

        if delNode.right:                             # When node on the right exists
            if delNodeParent.data > delNode.data:     # When parent is bigger then  node
                delNodeParent.left = delNode.right    # Set parents left node to right node
            else:
                delNodeParent.right = delNode.right   # Set parents right node to right node 
        
        else:
            if delNode.data < delNodeParent.data:     # When node is lower then parent
                delNodeParent.left = None             # Remove parents left node
            else: 
                delNodeParent.right = None            # Remove parents right node
    '''REMOVE TARGET ON TOP
    Remove target on top of the tree
    @param [target]     - Node to delete
    @return [bolean or None] - false when tree is empy, true when target is on top, None otherwise
    '''
    def _is_target(self,target):
        if self.root is None:                                      # When tree is empty
            return False    
        elif self.root.data is target:                             # Check if top value is target
            if self.root.left is None and self.root.right is None: # When adjanced roots doesnt exists
                self.root = None                                   # Remove top value in tree
            elif self.root.left and self.root.right is None:       # When left root is valid and right doesnt exists
                self.root = self.root.left                         # Set top value to connected left root
            elif self.root.left is None and self.root.right:       # When right root is valid and left doesnt exists 
                self.root = self.root.right                        # Set top value to connected right root
            elif self.root.left and self.root.right:               # When right and left roots exists
                self._left_right(self.root)                        # Rebuild tree around node
            return True
        return None                                       

    '''INTERNAL REMOVE NODE
    Remove node from tree
    @param [target]     - Node to delete
    '''               
    def _remove(self,target,parent,node):
        if node.left is None and node.right is None:               # When adjacent left nodes dont exists for current node
            if target < parent.data:                               # When target is lower then parent root
                parent.left = None                                 # Remove connection with target on left
            else:
                parent.right = None                                # Remove connection with target on right
        
        elif node.left and node.right is None:                     # When adjacent node exists and right is not for current node 
            if target < parent.data:                               # When target is lower then parent
                parent.left = node.left                            # Set node on left to parents left
            else:
                parent.right = node.left                           # Set node on right to parents left
        
        elif node.right and node.left is None:                     # When adjacent right node exists and left is not for current node 
            if target > parent.data:                               # When target is lower then parent
                parent.right = node.right                          # Set node on right to parents right
            else:
                parent.left = node.right                           # Set node on left to parents right
        
        else:
            self._left_right(node)                                 # Rebuild tree around node
    '''REMOVE NODE
    Remove node from tree
    @param [target]     - Node to delete
    @return [boolean]   - Node removed = True or not found = False
    '''
    def remove(self,target):
        flag = self._is_target(target)                              # Check if same as target
        if flag is not None:                                       # When it is None, target is not on top
            return flag
                
        parent = None                                              # Keeping track of previous node
        node = self.root                                           # Current node
 
        while node and node.data is not target:                    # Until target is not found or None
            parent = node                                          # Set current node as parent
            if target < node.data:                                 # When target is lower than current node
                node = node.left                                   # Set node on left into current node 
            elif target > node.data:                               # When target is higher than current node
                node = node.right                                  # Set node on right into current node 
        
        if node is None or node.data != target:                    # Exit when target was not found
            return False

        self._remove(target,parent,node)                           # Remove target from tree
        return True                                                # Target was found
    '''INTERNAL DISPLAY
    @param [cur_node]     - Node to display from
    @return [line]      - Line of the tree
    '''            
    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

bst = BinaryTree() # Init  

# Find value while tree is empty
print(bst.find_i(0))

# Insert values
bst.insert(40)
bst.insert(20)
bst.insert(60)
bst.insert(10)
bst.insert(30)
bst.insert(50)
bst.insert(70)
bst.insert(68)
bst.insert(66)
bst.insert(63)
bst.insert(69)
bst.insert(67)
bst.insert(61)

# Display tree
bst.display(bst.root)

# Find value
print(bst.find_i(60))

# Remove
print(bst.remove(60))
bst.display(bst.root)

# Find value
print(bst.find_i(60))
