//add two numbers
addNum(int a, int b) => a + b;

//divide two numbers and return a double
double multi({int a=12, required double c}) => a * c;

//get first element in the list of integers
int getFirstElement(List<int> lst) => lst[0];

//returns the lenth of the string parsed
int stringLength(String name) => name.length;

//checks if the number is even or not
bool checkeven(int num) => num % 2 == 0 ? true : false;

void main() {
  var sum = addNum(12, 45);
  print(sum);
  print(multi(c: 2, a: 14));
  var ls = [12, 34, 45, 64];
  int element = getFirstElement(ls);
  print(element);
  int len = stringLength('Liz');
  print(len);
  print(checkeven(22));
}
