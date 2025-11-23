# Ask data from users

# Name input
name = input("Enter your name: ")

# age input
age = int(input(f"Welcome {name}!!! How old are you "))
if age < 18:
    print(f"heloo {name} your access has been denied")
else:
# Vip confirm
    vip_pass =input(f""" heloo {name}!! Do you have VIP pass
1) Yes
2) No
choice: """)

    vip_pass_is_true = vip_pass.lower()=="yes" or int(vip_pass)=="1"
    if not vip_pass_is_true:
        print(f"Heloo {name} your entry is allowed with no backstage")
    else:
        print(f"Heloo {name} your entry and backstage is allowed")

# ----------------------corrected code------------------------------- 
        # Ask data from users

# Name input
name = input("Enter your name: ")

# age input
age = int(input(f"Welcome {name}!!! How old are you? "))

if age < 18:
    print(f"Hello {name}, your access has been denied.")
else:
    # VIP confirm
    vip_pass = input(f"""
Hello {name}!!
Do you have a VIP pass?
1) Yes
2) No
choice: """)

    vip_pass_is_true = vip_pass.lower() == "yes" or vip_pass == "1"

    # Require AND (as instructed)
    if vip_pass_is_true and age >= 18:
        print(f"Hello {name}, your entry and backstage access is allowed.")
    else:
        print(f"Hello {name}, your entry is allowed with no backstage.")

    