# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# while x < 5:
#   print(x)
#   x = x + 1

# answer = input("should i stop?")
# while answer != "yes":
#   print(answer)
#   answer = input("should i stop?")

# define a for loop"
days = ["mon","tue","wed","thu","fri","sat","sun"]
# for d in days:
#   print(d)

# use a for loop over a collection


# use the break and continue statements
# for d in days:
#   if (d == "thu"):
#     continue
#   print(d)

# using the enumerate() function to get an index and an item
for i,d in enumerate(days):
  print(i, d)