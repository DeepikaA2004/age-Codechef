# age-Codechef
## PROBLEM STATEMENT
Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

The minimum age limit is 
X (i.e. Age should be greater than or equal to 
X).
Age should be strictly less than 
Y.
Chef's current Age is 
A. Find whether he is currently eligible to take the exam or not.

## Input Format
First line will contain 
T, number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing three integers
X,Y, and 
A as mentioned in the statement.
## Output Format
For each test case, output YES if Chef is eligible to give the exam, NO otherwise.
You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

## Constraints

## Sample 1:
## Input                      Output
  21 34 30                    YES 
  25 31 31                    NO
  22 29 25                    YES
  20 40 15                    NO
  28 29 28                    YES

## Explanation:
Test case 
1
1: The age of Chef is 
30
30. His age satisfies the minimum age limit as 
30
≥
21
30≥21. Also, it is less than the upper limit as 
30
<
34
30<34. Thus, Chef is eligible to take the exam.

Test case 
2
2: The age of Chef is 
31
31. His age satisfies the minimum age limit as 
31
≥
25
31≥25. But, it is not less than the upper limit as 
31
≮
31
31≮31. Thus, Chef is not eligible to take the exam.

Test case 
3
3: The age of Chef is 
25
25. His age satisfies the minimum age limit as 
25
≥
22
25≥22. Also, it is less than the upper limit as 
25
<
29
25<29. Thus, Chef is eligible to take the exam.

Test case 
4
4: The age of Chef is 
15
15. His age does not satisfy the minimum age limit as 
15
<
20
15<20. Thus, Chef is not eligible to take the exam.
