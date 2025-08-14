"""
void reverse(int arr[], int n)
{
    int low=0
    int high = n-1
    for (int i=0; i<n; i++)
    {
        if(low<high):
        {
            int temp = arr[low]
            arr[low]=arr[high]
            arr[high]=temp
            low++
            high--
        }
    }
}
"""
arr = [30, 7, 6, 5, 10]
low = 0
high = len(arr)-1
for i in range(len(arr)):
    if low<high:
        temp =arr[low]
        arr[low]=arr[high]
        arr[high]=temp
        low+=1
        high-=1
for i in range(len(arr)):
    print(arr[i], end=" ")
