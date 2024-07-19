def find_max_min(numbers_list):
    # Find the maximum and minimum numbers in the list
    max_number = max(numbers_list)
    min_number = min(numbers_list)

    return max_number, min_number


def main():
    # Prompt the user to enter 5 numbers
    numbers_list = []
    for i in range(5):
        number = float(input(f"Enter number {i + 1}: "))
        numbers_list.append(number)

    # Use the find_max_min function to find the maximum and minimum numbers
    max_number, min_number = find_max_min(numbers_list)

    # Display the maximum and minimum numbers
    print(f"The maximum number is: {max_number}")
    print(f"The minimum number is: {min_number}")


# Run the main function
if __name__ == "__main__":
    main()
