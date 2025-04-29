'''

Tag: Easy, Stack, Tree ,Depth-First Search, Binary Tree

-------------------------------------------------------------------------------------------

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

    
Ultimate Goal: Recursive solution is trivial, could you do it iteratively?

'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")

    # Start printing at the Root -> then the Left subtree -> finaly the Right subtree
    def preorder_print(self, start, traversal):

        if start: 
            traversal += (str(start.val) + " - ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    #Start printing at the left most, then root, the right most
    def inorder_print(self, start, traversal):

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.val) + " - ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    #Start printing at the left most, then the right most, then the root
    def postorder_print(self, start, traversal):

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.val) + " - ")
        return traversal



if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.left.right.left = TreeNode(6)
    tree.root.left.right.right = TreeNode(7)
    tree.root.right.right = TreeNode(8)
    tree.root.right.right.left = TreeNode(9)

    print(tree.print_tree("preorder"))
    print(tree.print_tree("inorder"))
    print(tree.print_tree("postorder"))

