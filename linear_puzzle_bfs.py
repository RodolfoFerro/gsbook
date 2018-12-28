from node import Node


def left_operator(node):
    """
    Function to swap left values.
    """

    data = node.get_data()
    operated_data = [data[1], data[0]] + data[2:]
    return Node(operated_data)


def center_operator(node):
    """
    Function to swap center values.
    """

    data = node.get_data()
    operated_data = [data[0], data[2], data[1], data[3]]
    return Node(operated_data)


def right_operator(node):
    """
    Function to swap rigth values.
    """

    data = node.get_data()
    operated_data = data[:2] + [data[3], data[2]]
    return Node(operated_data)


def border_operator(node):
    """
    Function to swap border values.
    """

    data = node.get_data()
    operated_data = [data[3]] + data[1:3] + [data[0]]
    return Node(operated_data)


def search_solution_with_bfs(initial_state, solution):
    """
    Function that generates new states from the initial state (using the
    defined operators) to solve the Linear Puzzle with four elements by
    doing a Breath-First Search in a graph.
    """

    # We initialize our data structures:
    visited, border = [], []
    initial_node = Node(initial_state)
    border.append(initial_node)
    opertators = [left_operator, center_operator,
                  right_operator, border_operator]

    # While we border nodes is not empty and puzzle not solved:
    while len(border) > 0:
        # Extract a node as FIFO structure and mark it as visited:
        node = border.pop(0)
        visited.append(node)

        # Compare if we already have our solution:
        if node.get_data() == solution:
            return node
        else:
            # Generate new children with operators:
            children = []
            for operator in opertators:
                child = operator(node)
                children.append(child)

                # Add new children to border list:
                if not child.in_list(visited) and not child.in_list(border):
                    border.append(child)

            # Set new children to node:
            node.set_children(children)


if __name__ == '__main__':
    # Set initial state to the problem:
    initial_state = [1, 4, 3, 2]
    solution = [1, 2, 3, 4]

    # Compute solution:
    solution_node = search_solution_with_bfs(initial_state, solution)

    # Build steps (by getting the father nodes of the solution):
    resulting_path = []
    node = solution_node
    while node.get_father() is not None:
        resulting_path.append(node.get_data())
        node = node.get_father()

    # Format solution:
    resulting_path.append(initial_state)
    resulting_path = resulting_path[::-1]
    print(resulting_path)
