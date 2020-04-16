string = "this is a variable"

# find method error nhi deta, index method error deta hai or script terminate hojati hai
# index method error deta hai
# print(string.find("z"))
# print(string.index("z"))

user_input = input("What to find? ")

# print(bool(string.find(user_input)))
# exit()

# print(bool(3))
# print(bool(-1))
# != matlab hai 'not equals to'

if string.find(user_input) != -1: # user_input mila ya nhi
    print(user_input, "was found")
    print(user_input, "found at", string.find(user_input))
else:
    print(user_input, "was not found")
exit()
# abhi meion bol nhi sakta kuch, cuz bara bhai barabar mein ;v, nhi to fuck kar deta
#print(bool(False))


# 1 = True
# 0 = False

# TRUE: kuch bhi ho, is true
# FALSE: kuch bhi nahi ho, is false






exit()
# 1 = true
# -1 = true
# 0 = false
input = input('What to find? ')

if string.find(input) != -1:
    print(input, "was found")
else:
    print(input, "was not found")


xyz in string
abs()
round()
len()

str.replace()
operators : /, +, -, *, **, //, %
augmented assignment :  +=, -=
