# def aa(i):
#     for i in range(10):
        

#         print("*")
# aa(i)
# for i in range(1,9):
#     # for j in range(6):  
#         print((9-i)*" "+ i*"*")

def triangle(n):
   for i in range(1, n+1):
      print(' ' * n, end='')
      print('* '*(i))
      n -= 1
n = int(input())
triangle(n)