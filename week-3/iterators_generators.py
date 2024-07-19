# iterators_generators.py

class Countdown:
    def __init__(self, start):
        """Initialize the Countdown with a starting number."""
        self.current = start

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Return the next number in the countdown."""
        if self.current < 1:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

def fibonacci_generator(limit):
    """Generate Fibonacci numbers up to a specified limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

import random

def random_number_generator(start, end, count):
    """Generate a sequence of random numbers between start and end."""
    for _ in range(count):
        yield random.randint(start, end)

def main():
    # Demonstrate Countdown iterator
    print("Countdown from 5:")
    for number in Countdown(5):
        print(number, end=' ')
    print()

    # Demonstrate fibonacci_generator
    print("Fibonacci numbers up to 21:")
    for number in fibonacci_generator(21):
        print(number, end=' ')
    print()

    # Demonstrate random_number_generator
    print("Random numbers between 1 and 10:")
    for number in random_number_generator(1, 10, 5):
        print(number, end=' ')
    print()

if __name__ == "__main__":
    main()
