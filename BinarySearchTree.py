class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        # Traverse left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Traverse root node
        elements.append(self.data)

        # Traverse right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self,value):  # Delete a particular Node with the passed value
        if value < self.data:   # Go to left subtree and recursively call this function
            if self.data:   # IMPORTANT : Check this condition to see if tree exists or not
                self.left = self.left.delete(value)  # IMPORTANT : Make sure to assign it as the new left subtree
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value) # Go to right subtree and recursively call this function
        else:  # Which means we found our node to be deleted. 3 cases exists here
            if self.left is None:  # Which means only one child exists which is right node
                return self.right  # The child node occupies the position of the deleted node
            elif self.right is None:
                return self.left
            elif self.left is None and self.right is None:  # Which means no child nodes, just set the node to None
                return None
               # Case where 2 nodes also exists. Can take two approaches here
            min_value = self.right.find_min()   # Minimum from right subtree
            self.data = min_value    # Set current node to minimum value
            self.right = self.right.delete(min_value)   # Delete duplicate node from right subtree and assign the returned subtree as the new right subtree

        return self

    def delete_alternate_approach(self,value):  # By taking maximum from left subtree
        if value < self.data:   
            if self.data:   
                self.left = self.left.delete(value)  
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value) 
        else:  
            if self.left is None:  
                return self.right  
            elif self.right is None:
                return self.left
            elif self.left is None and self.right is None:  
                return None
               
            max_value = self.left.find_max()   # The following 3 lines are changed to get this approach
            self.data = max_value    
            self.left = self.left.delete(max_value)   

        return self


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root



if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

    numbers_tree.delete(4)
    print("Delete Node 4 from list: ",numbers_tree.in_order_traversal())

    numbers_tree.delete_alternate_approach(1)
    print("Delete Node 4 from list: ",numbers_tree.in_order_traversal())