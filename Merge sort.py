# merge sort will of course sort data and it does this by taking the initial array of
# unsorted data and then breaks it down
# into many arrays that are one element long and combines them back together in order
# also it works in logarithmic time (n log n)

items = [6,2,4,6,8,1,3,457,2,456,23,123,543,765,567,345,2,432,2,7,53]


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        # break down the arrays using recursion
        merge_sort(left)
        merge_sort(right)

        # merge them back together
        i = 0  # index for left
        j = 0  # index for right
        k = 0  # index for the new one

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


print(items)
merge_sort(items)
print(items)

