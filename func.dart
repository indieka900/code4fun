addNum(int a, int b) => a + b;

int getFirstElement(List<int> lst) => lst[0];

int stringLength(String name) => name.length;

void main() {
  print("Hello");
  var sum = addNum(12, 45);
  print(sum);
  var ls = [12, 34, 45, 64];
  int element = getFirstElement(ls);
  print(element);
  int len = stringLength('Liz');
  print(len);
}
