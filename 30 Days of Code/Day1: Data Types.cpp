#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    // Declare second integer, double, and String variables.
    int k; double e; string t;
    // Read and save an integer, double, and String to your variables.
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    cin >> k; cin >> e; getline(cin >> ws, t);
    // Print the sum of both integer variables on a new line.
    k += i;
    cout << k <<endl;
    // Print the sum of the double variables on a new line.
    e += d;
    cout << fixed << setprecision(1) << e << endl;
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s << t << endl;
    return 0;
}