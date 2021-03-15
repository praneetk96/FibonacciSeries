#  ____  _  __
# |  _ \| |/ /	Praneet Kumar
# | |_) | ' / 	https://github.com/praneetk96
# |  __/| . \
# |_|   |_|\_\
# Fibonacci series generator for the 100th place using recursion in python3
# for i.e. enter 100 to get fibonacci series till 100th place!

nterms = int(input("Enter number's place till to print the series? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
while count < nterms:
    print(n1)
    nth = n1 + n2

    n1 = n2
    n2 = nth
    count += 1
