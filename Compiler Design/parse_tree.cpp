#include <iostream>
#include <vector>
#include <string>

struct Node {
    std::string symbol;
    std::vector<Node> children;
};

Node generateParseTree(std::string input, std::vector<std::pair<std::string, std::vector<std::string>>> productions, std::string currentSymbol) {
    Node currentNode;
    currentNode.symbol = currentSymbol;

    for (auto production : productions) {
        if (production.first == currentSymbol) {
            Node childNode;
            childNode.symbol = production.first;

            for (std::string symbol : production.second) {
                Node grandchildNode = generateParseTree(input, productions, symbol);
                childNode.children.push_back(grandchildNode);
            }

            currentNode.children.push_back(childNode);
        }
    }

    return currentNode;
}

void printParseTree(Node node, int depth = 0) {
    for (int i = 0; i < depth; i++) {
        std::cout << "  ";
    }
    std::cout << node.symbol << std::endl;

    for (Node child : node.children) {
        printParseTree(child, depth + 1);
    }
}

int main() {
    std::vector<std::pair<std::string, std::vector<std::string>>> productions = {
        {"S", {"aSb", "ab"}},
        {"A", {"c"}},
        {"B", {"d"}}
    };

    std::string input = "aaab";

    Node parseTree = generateParseTree(input, productions, "S");
    printParseTree(parseTree);

    return 0;
}