
#############   d1P4 Multiplication Combinations Generator

def generate_multiplication_combinations():
    try:
        number = int(input("Enter a positive integer for the multiplication table's upper limit: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
        
    if number <= 0:
        print("Please enter a positive integer.")
        return

    print(f"\n--- Multiplication Combinations Up to {number} ---")
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(f"{i} x {j} = {j*i}") # Adjust padding as needed


#############   d2P2 Multiplication Table List Generator
def generate_multiplication_table_list():
    while True:
        try:
            number = int(input("Enter the upper limit for the multiplication table: "))
            if number <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    table_rows = []
    for i in range(1, number + 1):
        current_row = []
        for j in range(1, i + 1):
            current_row.append(i * j)
        table_rows.append(current_row)
    
    print("\n--- Generated Multiplication Table List ---")
    for row in table_rows:
        print(row)
        
    return table_rows





# if __name__ == "main":
#     generate_multiplication_combinations()
#     generate_multiplication_table_list()