
guest_list = []
name = input("What is your name:\r")
name = name.title()
print(name)
newlist = guest_list.insert(0,name)
print(newlist)

name = ["gabby", "andrew", "aaron", "abijah", "akinwale"]
print("Here is the original list: ")
print(name)
print("\n\t")
print("Here is the sorted list: ")
print(sorted(name))
print("\t\n")
print("Here is the original list: ")
print(name)
print(sorted(name, reverse=True))
