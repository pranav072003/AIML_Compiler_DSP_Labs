# bayesian network

class Node:
    def __init__(self, name, parents=None):
        self.name = name
        self.parents = parents if parents else []
        self.probabilities = {}

    def add_probability(self, values, probability):
        self.probabilities[tuple(values)] = probability

    def get_probability(self, values):
        return self.probabilities[tuple(values)]


class BayesianNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def get_node(self, name):
        return self.nodes[name]

    def calculate_probability(self, node_name, node_value, evidence):
        node = self.get_node(node_name)
        parents = node.parents
        parent_node = []
        parent_of_parent = []
        for parent_name in parents:
          i = self.get_node(parent_name)
          parent_node.append(i) 
          parent_of_parent.append(i.parents)
        parent_of_parent_values = [evidence[parent] for parent in parent_of_parent[0]]
        parent_node = self.get_node(parents[0])
        probability = node.get_probability([node_value]) * parent_node.get_probability(parent_of_parent_values)
        for parent in parent_of_parent[0]:
            parent_of_parent_node = self.get_node(parent)
            # print(parent_of_parent_node.get_probability([evidence[parent]]))
            if evidence[parent]==False:
                probability *= (1-parent_of_parent_node.get_probability(tuple([True])))
                continue
            probability *= parent_of_parent_node.get_probability([evidence[parent]])
        return probability

# Create nodes
burglary = Node('Burglary')
earthquake = Node('Earthquake')
alarm = Node('Alarm', parents=['Burglary', 'Earthquake'])
john_calls = Node('JohnCalls', parents=['Alarm'])
mary_calls = Node('MaryCalls', parents=['Alarm'])

# Add probabilities
burglary.add_probability([True], 0.001)
earthquake.add_probability([True], 0.002)
alarm.add_probability([True, True], 0.95)
alarm.add_probability([True, False], 0.05)
alarm.add_probability([False, True], 0.94)
alarm.add_probability([False, False], 0.06)
john_calls.add_probability([True], 0.90)
john_calls.add_probability([False], 0.10)
mary_calls.add_probability([True], 0.70)
mary_calls.add_probability([False], 0.30)

# Create Bayesian network
network = BayesianNetwork()
network.add_node(burglary)
network.add_node(earthquake)
network.add_node(alarm)
network.add_node(john_calls)
network.add_node(mary_calls)

# Calculate probability
evidence = {'Burglary': True, 'Earthquake': False, 'Alarm': True}
probability = network.calculate_probability('JohnCalls', False, evidence)
print(f"The probability of John calling given the evidence is: {probability}")