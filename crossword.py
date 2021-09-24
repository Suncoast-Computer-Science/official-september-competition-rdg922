a = input()
b = input()
num = int(input())

a, b = sorted([a, b], key=len)

if len(a + b) >= num:
  print("False");
else:
  print(a + b);
