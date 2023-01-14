# ++++++ STR (STRINGS) ++++++++++++++

# Ask user for their name
# name = input("What's your name? ").strip().title()

# name = input().strip().title()   

# Split user's name into first name and last name
# first, last = name.split(' ')

# # Remove whitespace from  str
# name = name.strip() 

# Combine methods (strip and capitalize for shorter codes)
# name = name.strip().title()

# # Capitalize name (first letter only)
# name = name.capitalize()

# #Capitalize all
# name = name.title()

#Say hello to user
# print(f"hello, {first}")

## +++++++++++++def for define ++++++++++++++++++

# def hello():
#     print("hello")

# name = input("What's your name?")
# hello()
# print(name)

# ----------------------------------

# def hello(to):
#     print("hello,", to)

# name = input("What's your name?")
# hello(name)   ////  hello, Nelia

#-----------------------------------

# def hello(to="world"):
#     print("hello,", to)
# hello()
# name = input("What's your name?")
# hello(name)   // hello, world (from the first arg)    hello, Nelia (from the name arg)

#-----------------------------
def main():
    name = input("What's your name?")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()






