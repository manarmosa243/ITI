# day1.py
#############  P1  check_vowels
def check_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u'] # Added 'e' for completeness
    count = 0
    # Convert the input string to lowercase to handle both 'A' and 'a'
    text_lower = text.lower()
    for char in text_lower:
        if char in vowels:
            count += 1
            print(char) # print each vowel as it's found
    print(f"Total vowels found: {count}") 
    return count # Return the count of vowels found


#############   P2  find_first_char_index

def find_first_char_index(target_char):
    string = input("Enter the string: ")
    string_lower = string.lower()
    target_char_lower = target_char.lower()
    
    for index, char in enumerate(string_lower):
        if char == target_char_lower:
            print(f"The first '{target_char}' is at index: {index}")
            return index # Return the index
    
    print(f"'{target_char}' not found in the string.")
    return -1 # Return -1 if not found



# day2.py
#############  p1

def sort_user_numbers():
    arr = []
    while True:
        try:
            num_elements = int(input("How many numbers do you want to sort? "))
            if num_elements <= 0:
                print("Please enter a positive number of elements.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(num_elements):
        while True:
            try:
                elem = int(input(f"Enter element number {i+1}: "))
                arr.append(elem)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
    ascending_arr = sorted(arr)
    descending_arr = sorted(arr, reverse=True)
    
    print("\n--- Sorted Results ---")
    print(f"Ascending sort: {ascending_arr}")
    print(f"Descending sort: {descending_arr}")
    
    return ascending_arr, descending_arr







# if __name__ == "__main__":

#     #############d1
#     check_vowels("Hello World") 
#     find_first_char_index("i") 
#     #############d2
#     sort_user_numbers()