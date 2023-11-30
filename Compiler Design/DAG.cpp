#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class DAG {
public:
    unordered_map<string, vector<string>> adjList;

    void addEdge(string from, string to) {
        adjList[from].push_back(to);
    }

    void draw_dag() {
        for (auto& entry : adjList) {
            cout << entry.first << " -> ";
            for (string dep : entry.second) {
                cout << dep << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    DAG dag;

    // Add edges
    dag.addEdge("A", "B");
    dag.addEdge("A", "C");
    dag.addEdge("B", "D");
    dag.addEdge("C", "D");
    dag.addEdge("C", "E");

    // Draw the DAG
    dag.draw_dag();

    return 0;
}