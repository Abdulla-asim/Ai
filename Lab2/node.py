class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = 0 if parent is None else parent.depth + 1

    def getPath(self):
        node, actions = self, []
        while node.parent is not None:
            actions.append(node.action)
            node = node.parent
        actions.reverse()
        return actions

    def getCost(self):
        return self.cost

    def getState(self):
        return self.state
    
    def getDepth(self):
        return self.depth
    