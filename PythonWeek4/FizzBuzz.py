"""KKKK"""

def fizzbuzz(target):
    """if num mod 3 = 0 print fizz
    if num mod 5 = 0 print buzz"""
    for i in range(1, target+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
            continue
        elif i%3 == 0:
            print("Fizz")
            continue
        elif i%5 == 0:
            print("Buzz")
            continue
        print(i)
fizzbuzz(int(input()))
