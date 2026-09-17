class TreeNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if self.root is None:
            self.root = new_node
            return
        
        curr_node = self.root
        while True:
            if key < curr_node.key:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return
                curr_node = curr_node.left
            elif key > curr_node.key:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return
                curr_node = curr_node.right
            else:
                curr_node.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr is not None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.val if curr else -1

    def findMax(self, node: TreeNode) -> TreeNode:
        while node and node.right:
            node = node.right
        return node

    def getMax(self) -> int:
        curr = self.findMax(self.root)
        return curr.val if curr else -1

    def removeHelper(self, node: TreeNode, key: int) -> TreeNode:
        if node is None:
            return None

        if key > node.key:
            node.right = self.removeHelper(node.right, key)
        elif key < node.key:
            node.left = self.removeHelper(node.left, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self.findMin(node.right)
                node.key = min_node.key
                node.val = min_node.val
                node.right = self.removeHelper(node.right, min_node.key)
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def inorderTraversal(self, root: TreeNode, res: List[int]) -> None:
        if root is not None:
            self.inorderTraversal(root.left, res)
            res.append(root.key)
            self.inorderTraversal(root.right, res)

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderTraversal(self.root, res)
        return res

