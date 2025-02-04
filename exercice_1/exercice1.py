def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid # Found the target
        elif arr[mid] < target:
            left = mid + 1 # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half

    return -1 # Target is not in the array

def manual_test():
    """enables the user to manually test the binary_search function by providing a sorted table and the target to seach for"""
    try:
        arr = list(map(int, input("Enter the sorted array(separed by space): ").split()))
        target = int(input("Enter the target : "))
        result = binary_search(arr, target)
        print(f"Result : Index {result}" if result != -1 else "Target not found")
    except ValueError:
        print("Please enter a valid integer")

def batch_test(filename):
    """enables the user to test the binary_search function on a batch of tests from a file"""
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("->")
                sorted_list = list(map(int, parts[0].strip().split()))
                target = int(parts[1].strip())

                result = binary_search(sorted_list, target)
                print(f"Sorted Table: {sorted_list}, Target: {target} -> Result: Index {result}" if result != -1 else "Target not found")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except ValueError:
        print("Invalid file format. Make sur the file is in the right format : '1 2 3 4 5 -> 5'.")

def main():
    """Main function"""
    while True:
        print("\n\n* MAIN MENU OF EXERCISE 1 *")
        print("1. Manual Test")
        print("2. Run a batch of tests")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3) : ")

        if choice == "1":
            manual_test()
        elif choice == "2":
            filename = input("Enter the file name of the batch of tests (eg: test_cases.txt) : ")
            batch_test(filename)
        elif choice == "3":
            print("Exiting...\n\n")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()