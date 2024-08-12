#binary search
arr = list(map(int, input().split()))
target = int(input())
def find_target(arr, target):
    arr.sort()
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r)// 2
        if arr[mid] == target:
            return mid
        if arr[l] < target:
            l = mid+1
        else:
            r = mid-1
    return -1

print(find_target(arr, target))