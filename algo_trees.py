class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # BST: ADD
    def add(self, value):
        if (self.root):
            runner = self.root
            while (runner):
                if (value > runner.value):
                    if (runner.right):
                        runner = runner.right
                    else:
                        runner.right = Node(value)
                        return self
                else:
                    if (runner.left):
                        runner = runner.left
                    else:
                        runner.left = Node(value)
                        return self
        self.root = Node(value)
        return self

    def contains(self, value):
        runner = self.root
        while runner:
            if value == runner.value:
                return True

            if value < runner.value:
                if (not runner.left):
                    return False
                runner = runner.left
            else:
                if (not runner.right):
                    return False
                runner = runner.right
        return False

    def min(self):
        runner = self.root
        min = self.root.value
        while runner.left:
            if runner.left.value < min:
                min = runner.left.value
            runner = runner.left

        return min

    def max(self):
        runner = self.root
        max = self.root.value
        while (runner.right):
            if (runner.right.value > max):
                max = runner.right.value

            runner = runner.right

        return max

    def size(self):
        if self.root == None:
            return 0

        def sizeHelp(runner):
            if (not runner):
                return 0
            return 1 + sizeHelp(runner.left) + sizeHelp(runner.right)

        return sizeHelp(self.root)

    def isEmpty(self):
        if self.root:
            return False
        return True