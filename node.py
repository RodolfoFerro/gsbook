class Node:
    """
    Node class based on the book "Inteligencia Artificial. Fundamentos,
    práctica y apliaciones", 2nd. Edition, by Alberto García Serrano.
    """

    def __init__(self, data, children=None):
        self.data = data
        self.children = None
        self.father = None
        self.cost = None
        self.set_children(children)

    def set_children(self, children):
        self.children = children
        if self.children is not None:
            for child in self.children:
                child.father = self
        return

    def get_children(self):
        return self.children

    def set_father(self, father):
        self.father = father
        return

    def get_father(self):
        return self.father

    def set_data(self, data):
        self.data = data
        return

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost
        return

    def get_cost(self):
        return self.cost

    def equal(self, node):
        if self.get_data() == node.get_data():
            return True
        return False

    def in_list(self, node_list):
        is_contained = False
        for node in node_list:
            if self.equal(node):
                is_contained = True
                break
        return is_contained

    def __str__(self):
        return str(self.get_data())
