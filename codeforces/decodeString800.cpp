#include <iostream>
#include <string>
using namespace std;

string process(string line) {
    int position = line.length() - 1;
    string result = "";
    bool getTwo = false;
    // cout << line << endl; 
    while (position >= 0) {
        char currChar = line.at(position);
        // cout << "Curr Char is " << endl;
        // cout << currChar << endl; 
        int number = -1; 
        if ((currChar == '0') && (!getTwo)) {
            // cout << "Set getTwo to true" << endl;
            getTwo = true;
        }
        else if (getTwo) {
            // cout << "--Detected two--" << endl;
            string fullNum = line.substr(position-1, 2);
            number = stoi( fullNum);
            getTwo = false;
            position--;
        }
        else {
            string num = line.substr(position, 1);
            number = stoi ( num );
        }
        if (!getTwo) {
            char converted = "abcdefghijklmnopqrstuvwxyz"[number-1];
            result = converted + result;
        }
        // cout << result << endl;
        position--;
    }
    return result; 
}

int main() {
    // cout << "We're running!" << endl; 
    int lineCounter = 0;
    for (string line; getline(cin, line);) {
        // cout << line << endl;
        if (lineCounter == 0) {
            lineCounter++;
            continue;
        }
        if (lineCounter % 2 == 0) {
            // cout << "Calling!" << endl;
            string result = process(line);
            cout << result << endl;
        }
        lineCounter++;
    }
}
