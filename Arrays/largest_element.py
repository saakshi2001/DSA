"""
NAIVE APPROACH

int getLargest (int arr[], int n)
{
    for(int i=0;i<n;i++)
    {
        bool flag=True
        for(int j=0;j<n;j++)
        {
            if(arr[j]>arr[i])
            {
                flag=false
                break
            }
        }
        if (flag==true)
            return i
    }
    return -1
}
"""
#Time complexity:O(n^2) for above


"""Efficient approach"""
#Time Complexity: theta(n) for below
"""
int getLargest(int arr[], int n)
{
    int res=0
    for(int i=1;i<n;i++)
        if(arr[i]>arr[res])
            res=i
    return res
}
"""
my_list=[10,30,20,40,60,50]
res=0
for i in range(len(my_list)):
    if my_list[i]>my_list[res]:
        res=i
print(f"Largest number is {my_list[res]}")