# def email_valid(email):

#     try:
#         if "@" not in email or "." not in email:
#             raise ValueError("Missing '@' or '.'")

#         if email.index("@") > email.index("."):
#             raise ValueError("'@' must come before '.'")

#         local, domain = email.split("@")
#         if not local or local.isdigit() or " " in local:
#             raise ValueError("Invalid local part of email")

#         domain_parts = domain.split(".")
#         if len(domain_parts) < 2 or not all(part for part in domain_parts[:2]):
#             raise ValueError("Invalid domain format")

#         print("Thanks!")
#         return True

#     except ValueError as ve:
#         print(f"Invalid email: {ve}")
#         return False

def email_valid(email):
    try:
        
        if "@" not in email or "." not in email:
            return False
        else :
            parts=email.split('@')
            if len(parts) != 2 :
                return False
            else :
                domain=parts[1]
                if '.'not in domain :
                    return False
                    
                else :
                    print("email is valid")
                    return True
    except ValueError:
        print(" email should contin '@'and '.'")
        return False



