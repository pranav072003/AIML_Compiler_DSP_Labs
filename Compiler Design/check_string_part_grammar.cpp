#include <iostream>
#include <vector>

using namespace std;

bool belongsToGrammar(string input, vector<pair<char, string>> productions) {
    char startSymbol = productions[0].first;
    char currentSymbol = startSymbol;

    for (char c : input) {
        bool found = false;
        for (auto production : productions) {
            if (production.first == currentSymbol && production.second.find(c) != string::npos) {
                currentSymbol = production.second[0];
                found = true;
                break;
            }
        }
        if (!found) {
            return false;
        }
    }

    return currentSymbol == startSymbol;
}

int main() {
    vector<pair<char, string>> productions = {
        {'S', "aSb"},
        {'S', "ab"}
    };

    string input1 = "aab";
    string input2 = "aabb";

    if (belongsToGrammar(input1, productions)) {
        cout << input1 << " belongs to the grammar." << endl;
    } else {
        cout << input1 << " does not belong to the grammar." << endl;
    }

    if (belongsToGrammar(input2, productions)) {
        cout << input2 << " belongs to the grammar." << endl;
    } else {
        cout << input2 << " does not belong to the grammar." << endl;
    }

    return 0;
}