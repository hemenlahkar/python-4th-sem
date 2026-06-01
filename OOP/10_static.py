"""
Write a class-based program to implement static members
"""


class Test:
    count = 0  # Static variable

    def __init__(sefl):
        Test.count += 1

    @staticmethod
    def add(a, b):  # Static function
        return a + b


def main():
    t1 = Test()
    t2 = Test()

    print("Current value of counter:", Test.count)
    print("Calling static add function with 4, 5 gives:", Test.add(4, 5))

if __name__ == '__main__':
    main()