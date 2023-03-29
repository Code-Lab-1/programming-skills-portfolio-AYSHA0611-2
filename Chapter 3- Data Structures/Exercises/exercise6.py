Guest=["Sharvari","Abiya","Rachita"]
print(Guest[0],"Your invited to dinner,please be present")
print(Guest[1],"Your invited to dinner,please be present")
print(Guest[2],"Your invited to dinner,please be present")
print("Sorry", Guest[2], "can't make it to dinner")
Guest.pop(2)
print(Guest[0],"Your still invited, please be present")
print(Guest[1],"Your still invited, please be present")
del Guest[0]
del Guest[0]
print(Guest)
