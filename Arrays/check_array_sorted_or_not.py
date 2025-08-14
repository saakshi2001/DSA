"""
bool is Sorted(int arr[], int n)
{
    for (int i=1; i<n; i++)
        if arr[i]<arr[i-1]:
            return false
    return true
}
"""
def isSorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

arr = [5, 12, 20, 70, 3]
res = isSorted(arr)
print(res)
