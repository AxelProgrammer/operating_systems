#include "math_functions.h"

double calculate(double num1, double num2, char operation) {
    double result;
    switch(operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
        default:
            result = 0.0; // По умолчанию возвращаем 0
            break;
    }
    return result;
}
