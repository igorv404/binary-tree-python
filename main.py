from Book import Book
from Node import Node

harry = Book("harry potter", "joanne rowling", 2002, "ababalamaga", 299)
tom = Book("tom&cat", "bob marley", 1965, "disney", 99)
charley = Book("charley and chocolate factory", "roald dahl", 1997, "ababalamaga", 199)
little = Book("little prince", "antoine exupery", 2012, "ababalamaga", 199)

root = Node(harry)
root.insert(tom)
root.insert(charley)
root.insert(little)
root.print_tree()
print("-----------")
print(root.find("ababalamaga"))
print("-----------")
root.delete("joanne rowling")
root.print_tree()
