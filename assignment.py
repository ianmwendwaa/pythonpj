def palindrome(x):
    return x == x[::-1]


x = "radar"
ans = palindrome(x)

if ans:
    print("True")
else:
    print("False")


def palindrome(y):
    return y == y[::-1]


y = "thigh"
ans2 = palindrome(y)

if ans2:
    print("Yes")
else:
    print("No")
