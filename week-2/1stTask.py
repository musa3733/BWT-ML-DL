musaimport re

def get_user_input():
    user_data = {}

    # Prompt user for input
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    user_data['email'] = input("Enter your email: ")
    user_data['favorite_number'] = input("Enter your favorite number: ")

    return user_data

def validate_email(email):
    # Basic email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def display_user_info(user_data):
    # Display the user information
    print(f"Hello {user_data['name']}, you are {user_data['age']} years old, your email is {user_data['email']}, and your favorite number is {user_data['favorite_number']}.")

def main():
    user_data = get_user_input()

    if validate_email(user_data['email']):
        display_user_info(user_data)
    else:
        print("Invalid email format. Please enter a valid email address.")

if __name__ == "__main__":
    main()
