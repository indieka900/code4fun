#include <stdio.h>

//function to add numbers
float addNum (float a, float b) {
    return a + b;
}

int main () {
    //declaration and initialization of variables
    int age;
    age = 24;
    float gpa = 3.5;
    char grade = 'C';
    char name[] = "Joseph AI";
    /*float b = addNum(23.7, 45.5);
    printf("%f", b);*/
    //displaying variables
    printf("Hello %s \n",name);
    printf("You are %d years old\n", age);
    printf("Your average grade is %c\n", grade);
    printf("Your gpa is %f\n", gpa);
    return 0;
}