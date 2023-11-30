#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Graph {
public:
    unordered_map<string, vector<string>> adjList;

    void addEdge(string from, string to) {
        adjList[from].push_back(to);
    }

    void generate_dependency_graph(string node, unordered_map<string, bool>& visited, vector<string>& dependency_order) {
        visited[node] = true;

        for (string dep : adjList[node]) {
            if (!visited[dep]) {
                generate_dependency_graph(dep, visited, dependency_order);
            }
        }

        dependency_order.push_back(node);
    }

    vector<string> get_dependency_order() {
        unordered_map<string, bool> visited;
        vector<string> dependency_order;

        for (auto& entry : adjList) {
            visited[entry.first] = false;
        }

        for (auto& entry : adjList) {
            if (!visited[entry.first]) {
                generate_dependency_graph(entry.first, visited, dependency_order);
            }
        }

        reverse(dependency_order.begin(), dependency_order.end());

        return dependency_order;
    }
};

int main() {
    Graph dependencyGraph;

    // Add dependencies
    dependencyGraph.addEdge("A", "B");
    dependencyGraph.addEdge("A", "C");
    dependencyGraph.addEdge("B", "D");
    dependencyGraph.addEdge("C", "E");

    // Generate dependency order
    vector<string> dependencyOrder = dependencyGraph.get_dependency_order();

    // Print the dependency order
    cout << "Dependency Order: ";
    for (string node : dependencyOrder) {
        cout << node << " ";
    }
    cout << endl;

    return 0;
}