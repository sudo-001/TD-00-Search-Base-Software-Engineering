def kadane_algorithm(arr):
    """Finds the maximum sum of a contiguous subarray using Kadane's Algorithm."""
    if not arr:
        return 0, []

    max_sum = current_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i  # Start of new subarray
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start, end = s, i
    return max_sum, arr[start:end+1]

def manual_test():
    """Allows the user to enter an array manually."""
    arr = list(map(int, input("Enter the array (separated by space): ").split()))

    max_sum, subarray = kadane_algorithm(arr)
    print(f"\n* Maximum Sum: {max_sum}")
    print(f"* Subarray: {subarray}")

def load_from_file(filename):
    """Loads and processes arrays from a file."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                arr = list(map(int, line.strip().split(",")))
                print(f"\nTesting case: {arr}")

                max_sum, subarray = kadane_algorithm(arr)
                print(f"* Maximum Sum: {max_sum}")
                print(f"* Subarray: {subarray}")

    except FileNotFoundError:
        print(f"⚠️ File {filename} not found.")

def main():
    """Main menu Exercise 5."""
    while True:
        print("\n* MAIN MENU Exercise 5*")
        print("1. Enter an array manually")
        print("2. Load test cases from a file")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            manual_test()
        elif choice == '2':
            filename = input("Enter the filename (e.g., subarrays.txt): ")
            load_from_file(filename)
        elif choice == '3':
            print("👋 Exciting...\n\n")
            break
        else:
            print("⚠️ Invalid choice, please enter 1-3.")

if __name__ == "__main__":
    main()