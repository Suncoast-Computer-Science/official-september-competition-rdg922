def diamond(width):
  len_first_half = int(width/2)
  for i in range(len_first_half+1):
    output = ""
    for j in range(len_first_half-i+1):
      output+=' '
    for j in range(i+1):
      output+='*'
    for j in range(i):
      output +='*'
    print(output)
  for i in reversed(range(len_first_half)):
    output = ""
    for j in range(len_first_half-i+1):
      output+=' '
    for j in range(i+1):
      output+='*'
    for j in range(i):
      output +='*'
    print(output)
    
#     # for j in range()
#     print(output)
a = int(input())
for i in range(1, 2*int(a)+1, 2):
  diamond(i)
  print('')
# for i in range(2*int(a),1, -2):
#   diamond(i)
for i in range(a, 1, -2):
  diamond(i)
  print('')
print('*')
