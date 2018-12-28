from node import Node


def solution_with_bfs(connections, initial_state, solution):
    """
    Function that generates traverses connections from the initial state
    to solve compute the minimum number of airport transfers in the flights
    problem doing a Breath-First Search in a graph.
    """

    # We initialize our data structures:
    visited, border = [], []
    initial_node = Node(initial_state)
    border.append(initial_node)

    # While we border nodes is not empty and puzzle not solved:
    while len(border) > 0:
        # Extract a node as FIFO structure and mark it as visited:
        node = border.pop(0)
        visited.append(node)

        # Compare if we already have our solution:
        if node.get_data() == solution:
            return node
        else:
            # Visit each connection (child):
            node_data = node.get_data()
            children = []
            for connection in connections[node_data]:
                child = Node(connection)
                children.append(child)

                # Add new children to border list:
                if not child.in_list(visited) and not child.in_list(border):
                    border.append(child)

            # Set new children to node:
            node.set_children(children)


if __name__ == '__main__':
    # Create connections map:
    connections = {
        "Malaga": ["Salamanca", "Madrid", "Barcelona"],
        "Sevilla": ["Santiago", "Madrid"],
        "Granada": ["Valencia"],
        "Valencia": ["Barcelona"],
        "Madrid": ["Salamanca", "Sevilla", "Malaga", "Barcelona", "Santander"],
        "Salamanca": ["Malaga", "Madrid"],
        "Santiago": ["Sevilla", "Santander", "Barcelona"],
        "Santander": ["Santiago", "Madrid"],
        "Zaragoza": ["Barcelona"],
        "Barcelona": ["Zaragoza", "Santiago", "Madrid", "Malaga", "Valencia"]
    }

    # Set initial state to the problem:
    initial_state = "Malaga"
    solution = "Santiago"

    # Compute solution:
    solution_node = solution_with_bfs(connections, initial_state, solution)

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
