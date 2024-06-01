addNum(int a, int b) => a + b;

double multi({int a=12, required double c}) => a * c;

int getFirstElement(List<int> lst) => lst[0];

int stringLength(String name) => name.length;

void main() {
  print("Hello");
  var sum = addNum(12, 45);
  print(sum);
  print(multi(c: 2, a: 14));
  var ls = [12, 34, 45, 64];
  int element = getFirstElement(ls);
  print(element);
  int len = stringLength('Liz');
  print(len);
}
