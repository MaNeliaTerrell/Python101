# x = 1
# y = 2

# z = x + y

# print(z) // 3

# --------------------------------------------------
# x = input("What's x?")
# y = input("What's y?")

# z = x + y

# print(z)  //  1 + 2 = 12 (concatenate - 1 and 2 are being read as strings)

#--------------------------------------------------------
# x = input("What's x?")
# y = input("What's y?")

# z = int(x) + int(y)

# print(z) // will return a 3 (as an integer)

#-----------------------------------------

# # Nesting function
# x = int(input("What's x?"))
# y = int(input("What's y?"))

# print(x + y)

# -------------------------------------
# Prone to syntax errors
#print(int(input("What's x?")) + int(input("What's y?"))) 


# ++++++++++++++ FLOAT ++++++++++++++ (numbers with decimals)

# x = float(input("What's x?"))
# y = float(input("What's y?"))

# print(x + y)

# ----------ROUNDING------------
# documentation  round(number[, ndigits])

# x = float(input("What's x?"))
# y = float(input("What's y?"))

# z = round(x + y)

# print(f"{z:,}")   ///  1,000 (with a comma)


#----------------------------------------

# x = float(input("What's x?"))
# y = float(input("What's y?"))

# z = round(x / y, 2)

# print(z) //  0.67

# ----------------------------------------
# x = float(input("What's x?"))
# y = float(input("What's y?"))

# z = x / y

# print(f"{z:.2f}")  /// 0.67 -- this is a f string way

#----------------------------------------------

# x = float(input("What's x?"))
# y = float(input("What's y?"))

# z = x / y

# print(f"{z:.2f}")

#---------------------------------------------

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

# OR n ** 2  OR pow(n, 2) // power of 2 / exponent of 2

main()



