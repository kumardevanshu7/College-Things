# Python Practical 02: To write a python a program to perform Matrix Multiplication.

# take a normal example
x = [[5, 7, 8], [4, 12, 3], [7, 23, 9]]
y = [[5, 2, 8], [6, 5, 1], [12, 4, 2]]

ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            ans[i][j] += x[i][k] * y[k][j]

for r in ans:
    print(r)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")