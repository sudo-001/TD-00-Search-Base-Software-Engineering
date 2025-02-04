def merge_intervals(intervals):
    """Merges overlapping intervals."""
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping case
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def manual_test():
    """Allows the user to enter intervals manually."""
    n = int(input("Enter the number of intervals: "))
    intervals = []
    for _ in range(n):
        start, end = map(int, input("Enter start and end time (separated by space): ").split())
        intervals.append((start, end))
    merged = merge_intervals(intervals)
    print(f"\n* Merged Intervals: {merged}")

def load_from_file(filename):
    """Loads and processes intervals from a file."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                intervals = [tuple(map(int, item.split(','))) for item in line.strip().split(";")]
                print(f"\nTesting case: {intervals}")

                merged = merge_intervals(intervals)
                print(f"* Merged Intervals: {merged}")

    except FileNotFoundError:
        print(f"File {filename} not found.")

def main():
    """Main menu."""
    while True:
        print("\n\n* MAIN MENU EXERCISE 4*")
        print("1. Enter intervals manually")
        print("2. Load test cases from a file")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            manual_test()
        elif choice == '2':
            filename = input("Enter the filename (e.g., intervals.txt): ")
            load_from_file(filename)
        elif choice == '3':
            print("Exciting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()