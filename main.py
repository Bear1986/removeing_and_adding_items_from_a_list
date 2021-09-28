#removeing and adding items from a list

#list
x = [
  231, 435, 777, 9874, 666
  ]

#removeing

y = int(input("what number do you want to remove?: "))

new_x =[x for x in x if x != y ]

print(new_x)

#adding

j = int(input("what number would you like to add?: "))

#remember that you have to specify a posision that the new item will take in the list - in this case its at posision 0 - or the start of the list

new_x.insert(0,j)    

print(new_x)
#Or

k = int(input("what number would you like to add?: "))
new_x.append(k)

print(new_x)

#This just adds it to the end of the list
