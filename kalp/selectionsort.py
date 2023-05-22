def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Take array input from the user
input_str = input("Enter the elements of the array separated by space: ")
arr = [int(num) for num in input_str.split()]

# Sort the array using selection sort
sorted_arr = selection_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)
