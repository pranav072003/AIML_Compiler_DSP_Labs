#include <iostream>
#include <vector>
using namespace std;

class Node {
public:
    string value;
    vector<Node*> children;

    Node(string val) {
        value = val;
    }
};

void generate_sdt(Node* node) {
    if (node->value == "A") {
        // Action for rule A -> B C
        generate_sdt(node->children[0]);
        generate_sdt(node->children[1]);
    }
    else if (node->value == "B") {
        // Action for rule B -> D
        generate_sdt(node->children[0]);
    }
    else if (node->value == "C") {
        // Action for rule C -> E
        generate_sdt(node->children[0]);
    }
    else if (node->value == "D") {
        // Action for rule D -> "Hello"
        cout << "Hello ";
    }
    else if (node->value == "E") {
        // Action for rule E -> "World"
        cout << "World";
    }
}

int main() {
    // Example graph
    // A -> B C
    // B -> D
    // C -> E
    // D -> "Hello"
    // E -> "World"

    // Create the graph
    Node* root = new Node("A");
    root->children.push_back(new Node("B"));
    root->children.push_back(new Node("C"));
    root->children[0]->children.push_back(new Node("D"));
    root->children[1]->children.push_back(new Node("E"));

    // Generate SDT
    generate_sdt(root);

    return 0;
}