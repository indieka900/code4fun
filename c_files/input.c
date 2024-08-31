#include <stdio.h>

float calcNum(int c, int a, int b) {
    switch (c)
    {
    case 1:
        return a + b;
        break;
    case 2:
        return a - b;
        break;
    case 3:
        return a * b;
        break;
    case 4:
        return a / b;
        break;
    
    default:
        break;
    }
}

int main () {
    int a, b, c;
    printf("\nPlease enter the first number: ");
    scanf("%d",&a);
    printf("\nPlease enter sign to use i.e 1, 2 or 3..: ");
    printf("\n\t1. Addition\n\t2. Substraction\n\t3. Multiplication\n\t4. Division:\n");
    scanf("%d",&c);
    printf("\nPlease enter the second number: ");
    scanf("%d",&b);

    float answer = calcNum(c, a, b);
    printf("\n\n ****** The answer for (%d and %d) is %.2f ******",a, b, answer);

    return 0;
}