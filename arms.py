# def armstrong(n):
#     t = n
#     sum1 = 0
#     a = len(str(n))
#     while t > 0:
#         d = t % 10
#         sum1 += d ** a
#         t //= 10
#     if sum1 == n:
#         return "armstrong"
#     else:
#         return "not armstrong"
#
#
# while True:
#     try:
#         n = int(input("Enter an integer: "))
#     except ValueError:
#         print("Error: Input is not an integer.")
#         continue
#
#     result = armstrong(n)
#     if result == "not armstrong":
#         print("Not an Armstrong number.")
#     else:
#         print("Armstrong number.")
#         break
#
# #
#
#
# # for i in range(1,len(str(n))+1):
# #     n1 = n % 10
# #     sum = sum + n1 ** a
# #     n=n//10
# # print(sum)
#
# # if t == sum:
# #      print("amstrong")
# # else:
# #      print("not amstrong")
# a="August 2024"
# b="subha  "
# print(b.strip())
# print(a.split()[0])
# try:
#     n = int(input("Enter: "))
#     t = n
#     sum1 = 0
#     a = len(str(n))
#     while t > 0:
#         d = t % 10
#         sum1 += d ** a
#         t //= 10
#     if sum1 == n:
#         print("armstrong")
#     else:
#         print("not armstrong")
# except Exception as e:
#     print(f"Error: Input is not an integer. {e}")
#
# test_example.py

import pytest

# Define a hook implementation
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item):
    print(f"\nRunning test: {item.name}")
    yield
    print(f"\nFinished test: {item.name}")

# Test function
def test_addition():
    assert (1 + 2) == 3

def test_subtraction():
    assert (5 - 2) == 3
