#############  P3

def mario_pyramid():
    print(f"--- Mario Pyramid ---")
    try:
        height = int(input("Enter a positive integer for the pyramid height: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    

    if  height <= 0:
        print("Please enter a positive integer for the pyramid height.")
        return

    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * i)




#############  P4 def mario_pyramid_string():before

def mario_list_pyramid():
    print(f"--- Mario Pyramid List ---")
    try:
        height = int(input("Enter a positive integer for the pyramid height: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    if not isinstance(height, int) or height <= 0:
        print("Error: Please enter a positive integer for the pyramid height.")
        return

    current_row_state = [" "] * height 

    print(f"\n--- Mario List Pyramid (Height {height}) ---")
    print("Showing the list's state at each step:\n")

    for i in range(1, height + 1):
        current_row_state[height - i] = "*"
        print(current_row_state)


# if __name__ == "__main__":

#     mario_pyramid()
#     mario_list_pyramid(5)