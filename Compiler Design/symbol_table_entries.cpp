#include <iostream>
#include <unordered_map>
using namespace std;

class SymbolTable {
public:
    unordered_map<string, string> symbolTable;

    void addEntry(string identifier, string value) {
        symbolTable[identifier] = value;
    }

    void showEntries() {
        cout << "Symbol Table Entries:" << endl;
        for (auto& entry : symbolTable) {
            cout << entry.first << " : " << entry.second << endl;
        }
    }
};

int main() {
    SymbolTable symbolTable;

    // Add symbol table entries
    symbolTable.addEntry("x", "10");
    symbolTable.addEntry("y", "20");
    symbolTable.addEntry("z", "30");

    // Show symbol table entries
    symbolTable.showEntries();

    return 0;
}