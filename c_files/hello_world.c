#include <stdio.h>
//to use booleans
#include <stdbool.h>

//function to add numbers
float addNum (float a, float b) {
    return a + b;
}

int main () {
    //declaration and initialization of variables
    int age; //( -32, 768 to +32,757)
    age = 24;
    float gpa = 3.5;
    char grade = 'C'; //(-128 to +127)
    char name[] = "Joseph AI";

    float p = 3.141592653589796; // 4 bytes
    double pi = 3.141592653589796; // 8 bytes

    bool e = true;

    unsigned char g = 255; //(0 to 255)
    unsigned int h = 65535; //(0 to + 65,535)

    /*float b = addNum(23.7, 45.5);
    printf("%f", b);*/
    //displaying variables

    printf("Hello %s \n",name);
    printf("You are %d years old\n", age);
    printf("Your average grade is %c\n", grade);
    printf("Your gpa is %f\n", gpa);

    printf("%0.15f\n", p);
    printf("%0.15lf\n", pi);

    printf("%d\n", e);

    printf("%c", age+90);


    return 0;
}