#First Problem
'''Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.
The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

Input Format:The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.
'''
# T = int(input())
# for tc in range(T):
# 	(a, b) = map(int, input().split(' '))
# 	ans = a + b
# 	print(ans)

# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# print(a+b)

# a,b=[int(x) for x in input().split(" ")]
# print(a+b)

#second problem

a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    if d>=b and d<c:
        print("YES")
    else:
        print("NO")
    