#Delete first occurence
my_list = [10, 20, 30, 40]
my_list.remove(30)  # removes the first 30

#Delete by index
my_list = [10, 20, 30, 40]
del my_list[2]  # removes the element at index 2 (i.e., 30)
#OR
my_list.pop(2)
# pop() returns the removed element.
# Without arguments: my_list.pop() removes the last element.

#Delete All Occurrences of a Value
my_list = [10, 20, 30, 20, 40]
my_list = [x for x in my_list if x != 20]

#Clear the Entire List
my_list.clear()
