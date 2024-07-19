# file_handling.py

def read_file(file_path):
    """Function to read data from a file, print its contents, and count the number of words."""
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print("File Contents:")
            print(data)
            word_count = len(data.split())
            print(f"Word Count: {word_count}")
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error: An error occurred while reading the file. {e}")

def write_to_file(file_path, content):
    """Function to write user input to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to '{file_path}'.")
    except Exception as e:
        print(f"Error: An error occurred while writing to the file. {e}")

def main():
    # Read data from data.txt and print its contents
    file_path = 'data.txt'
    data = read_file(file_path)

    # Write user input to output.txt
    user_input = input("Enter some text to write to output.txt: ")
    output_file_path = 'output.txt'
    write_to_file(output_file_path, user_input)

if __name__ == "__main__":
    main()
