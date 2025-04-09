def binary_search(arr, target):
    # Define the search boundaries
    left, right = 0, len(arr) - 1

    # Continue searching while the boundaries are valid
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found in the array


# 🧪 Example usage
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    target = int(input("please enter a number :"))

    index = binary_search(nums, target)

    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in the list.")
