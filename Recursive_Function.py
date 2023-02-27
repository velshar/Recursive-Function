# Sharon Robinson
# CIS 261, Week 8, Lab 2


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    for i in range(16):
        print(fib(i), end=", ")
    print("...")
print("The Fibonacci series for 16")

if __name__ == "__main__":
    main()
