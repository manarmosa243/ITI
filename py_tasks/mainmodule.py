import mario_pyramid as mp
import multiplication_combinations as mul# pyright: ignore[reportMissingImports]
import py_proplem_solving as ps
import email_validation as eval

# #############d1
ps.check_vowels("Hello World") 
print("i will get a charecter index in your string")
char=input("enter the charecter you are looking for")
ps.find_first_char_index(char) 
#############d2

print("i will make a list and sort it according to your inputs ")
ps.sort_user_numbers()

#
print("i will create mario pyramid according to your inputs ")
mp.mario_pyramid()
mp.mario_list_pyramid()
#
print("i will make multiplication table according to your inputs ")
mul.generate_multiplication_combinations()
mul.generate_multiplication_table_list()
#
print('lets validate your email \n')
for _ in range(5):
    email = input("Enter your email: ")
    if eval.email_valid(email):
        break
else:
    raise ValueError("Too many invalid attempts.")
