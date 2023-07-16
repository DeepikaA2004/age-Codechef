# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input values
    X, Y, A = map(int, input().split())

    # Check if Chef is eligible to take the exam
    if X <= A < Y:
        print("YES")
    else:
        print("NO")
