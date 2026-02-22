the_name = input("What is the name in camel case?: ")
for i in the_name:
    if not i.islower() and not i == the_name[0]:
        the_name = the_name.replace(i,f"_{i.lower()}")
print(F"The name in snake case is: {the_name}")