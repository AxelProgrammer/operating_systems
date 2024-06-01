#include <stdio.h>
#include <stdlib.h>
#include <windows.h> // Для работы с DLL
#include "math_functions.h"

int main() {
    HINSTANCE hDll = LoadLibrary("math_functions.dll"); // Загрузка DLL
    if (hDll == NULL) {
        fprintf(stderr, "Не удалось загрузить библиотеку.\n");
        return 1;
    }

    // Загрузка функции из DLL
    typedef double (*CalculateFunc)(double, double, char);
    CalculateFunc calculate = (CalculateFunc)GetProcAddress(hDll, "calculate");
    if (calculate == NULL) {
        fprintf(stderr, "Не удалось найти функцию в библиотеке.\n");
        return 1;
    }

    double num1, num2;
    char operation;
    printf("Введите два числа и операцию (+, -, *, /), через пробел, например\"5 5 +\": ");
    scanf("%lf %lf %c", &num1, &num2, &operation);

    double result = calculate(num1, num2, operation);
    printf("Результат: %lf\n", result);

    FreeLibrary(hDll);

    return 0;
}
