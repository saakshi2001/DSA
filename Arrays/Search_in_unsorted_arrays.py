"""
int search (int arr[], int n, int x)
{
    for(int i=0,i<n,i++)
        (if arr[i]==x)
            return i
    return -1
}
"""
#TIME COMPLEXITY O(n)
my_list = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

x = int(input("Enter number to be searched for: "))

flag = False
for i in range(n):
    if my_list[i]==x:
        print(f"Element at array position {i}")
        flag = True
        break
if flag == False:
    print(f"{x} not found in list")

#OPTIMIZED IN TERMS OF LINES
my_list = [int(input(f"Enter element {i+1}: ")) for i in range(int(input("Enter the number of elements: ")))]

x = int(input("Enter number to be searched for: "))

if x in my_list:
    print(f"Element found at array position {my_list.index(x)}")
else:
    print(f"{x} not found in list")