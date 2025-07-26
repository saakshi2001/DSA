"""
Insert x at a given position pos, in an array of capacity cap
int insert(int arr[], int n, int x, int cap, int pos)
{
    if (n==cap)
        return n
    int idx = pos-1
    for(int i=n-1, i>=idx, i--)
        arr[i+1] = arr[i]
    arr[idx] = x
    return (n+1)
}
"""
#Time complexity O(n) in general
#Insert at end: O(1)
#Insert at beginning: theta(n)
def insert(arr, n, x, cap, pos):
    if n == cap:
        print("Cannot insert: list is full")
        return n
    
    idx = pos - 1  # Convert to 0-based index

    # Shift elements to the right
    for i in range(n - 1, idx - 1, -1):
        arr[i + 1] = arr[i]

    arr[idx] = x
    return n + 1

#Most optimized
def insert_fixed(arr, n, x, cap, pos):
    if n >= cap:
        print("Insertion failed: list is full.")
        return n

    idx = pos - 1  # Convert to 0-based index

    if idx < 0 or idx > n:
        print("Invalid position.")
        return n

    arr.insert(idx, x)  # Pythonic insert

    # Trim to capacity if insert overflows
    if len(arr) > cap:
        arr.pop()

    return n + 1
