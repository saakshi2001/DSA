"""
int secondLargest(int arr[], int n)
{
    int res=-1, largest=0
    for(int i=0;i<n;i++)
    {
        if(arr[i]>arr[largest])
        {
            res=largest
            largest=i
        }
        else if(arr[i]!=arr[largest])
        {
            if(res==-1 or arr[i]>arr[res])
                res=i
        }
    }
}
"""
#Time complexity: O(n)
my_list = [8,7,12,30,6,54]
res=-1
largest=0
for i in range(len(my_list)):
    if(my_list[i]>my_list[largest]):
        res=largest
        largest=i
    elif(my_list[i]!=my_list[largest]):
        if(res==-1 or my_list[res]<my_list[i]):
            res=i
print(f"Second largest element is {my_list[res]}")