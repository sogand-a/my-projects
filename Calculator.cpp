#include <iostream>
#include <limits>

using namespace std;

class Calculator {
public:
    void performOperation() {
        double num1 = getValidNumber("Enter the first number: ");
        int choice;
        
        do {
            showMenu();
            cin >> choice;

            if (choice >= 1 && choice <= 4) {
                double num2 = getValidNumber("Enter the second number: ");
                calculate(num1, num2, choice);
            } else if (choice != 5) {
                cout << "Invalid choice! Try again.\n";
            }
        } while (choice != 5);

        cout << "Exiting calculator.\n";
    }

private:
    void showMenu() const {
        cout << "\nBasic Calculator\n"
             << "Select an operation:\n"
             << "1. Addition (+)\n"
             << "2. Subtraction (-)\n"
             << "3. Multiplication (*)\n"
             << "4. Division (/)\n"
             << "5. Exit\n"
             << "Enter your choice (1-5): ";
    }

    void calculate(double num1, double num2, int operation) const {
        switch (operation) {
            case 1: 
                cout << "Result: " << num1 + num2 << endl; 
                break;
            case 2: 
                cout << "Result: " << num1 - num2 << endl; 
                break;
            case 3: 
                cout << "Result: " << num1 * num2 << endl; 
                break;
            case 4: 
                if (num2 != 0) 
                    cout << "Result: " << num1 / num2 << endl;
                else 
                    cout << "Error: Division by zero!" << endl; 
                break;
            default: 
                cout << "Invalid operation!" << endl;
        }
    }

    double getValidNumber(const string& prompt) const {
        double number;
        while (true) {
            cout << prompt;
            cin >> number;
            if (cin.fail()) {
                cout << "Invalid input! Please enter a valid number: ";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
            } else {
                return number;
            }
        }
    }
};

int main() {
    Calculator calc;
    calc.performOperation();
    return 0;
}