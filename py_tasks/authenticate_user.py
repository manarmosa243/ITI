def authenticate_user(users_data, max_attempts=3):

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}:")
        
        entered_name = input("Enter your name: ").strip() 
        try:
            entered_password = int(input("Enter your password: "))
        except ValueError:
            print("Invalid password input. Please enter a whole number.")
            continue # Go to the next attempt if password is not a valid number

        found_match = False
        for user_record in users_data:
            if entered_name == user_record["name"] and entered_password == user_record["password"]:
                found_match = True
                break # Found a match, no need to check further records
        
        if found_match:
            print("\nWelcome! Authentication successful.")
            return True # Indicate successful login
        else:
            print("Invalid credentials. Name or password is incorrect.")
            if attempt == max_attempts:
                print("Maximum login attempts reached. Access denied.")
                return False # Indicate failed login after max attempts

    return False


if __name__ == "__main__":
    user_accounts = [
        {"name": "ahmed", "password": 20},
        {"name": "fatma", "password": 25},
        {"name": "ali", "password": 30}
    ]

    if authenticate_user(user_accounts, max_attempts=2):
        print("User logged in.")
    else:
        print("Failed to log in.")
