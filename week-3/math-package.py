# main.py

from mymath.addition import add
from mymath.subtraction import subtract
from mymath.multiplication import multiply
from mymath.division import divide
from mymath.modulus import modulus
from mymath.exponentiation import power
from mymath.square_root import sqrt

def main():
    a = 10
    b = 5

    print(f"Addition of {a} and {b}: {add(a, b)}")
    print(f"Subtraction of {a} and {b}: {subtract(a, b)}")
    print(f"Multiplication of {a} and {b}: {multiply(a, b)}")
    print(f"Division of {a} and {b}: {divide(a, b)}")
    print(f"Modulus of {a} and {b}: {modulus(a, b)}")
    print(f"{a} raised to the power of {b}: {power(a, b)}")
    print(f"Square root of {a}: {sqrt(a)}")

if __name__ == "__main__":
    main()
