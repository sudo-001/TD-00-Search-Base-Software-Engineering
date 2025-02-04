def knapsack(items, max_weight):
    """Solves the 0/1 Knapsack problem using Dynamic Programming."""
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n+1)]

    # Fill DP table
    for i in range(1, n+1):
        value, weight = items[i-1]
        for w in range(max_weight + 1):
            if weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i-1][w-weight] + value)

    # Find selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0-1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1])
            w-=items[i-1][1]

    return dp[n][max_weight], selected_items

def manual_test():
    """Allows the user to manually input items and weight limit."""
    items=[]
    n=int(input("Enter the number of inputs : "))
    for _ in range(n):
        value, weight=map(int, input("Enter value and weight (separed by space): ").split())
        items.append((value, weight))
    max_weight = int(input("Enter the maximum weight capacity: "))

    max_value, selected_items = knapsack(items, max_weight)
    print(f"\n Maximum value: {max_value}")
    print(f"\n Selected items: {selected_items}")

def load_from_file(filename):
    """Loads knapsack test cases from a file"""
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) != 2:
                    continue
                items = [tuple(map(int, item.split(','))) for item in parts[0].split(";")]
                max_weight=int(parts[1])

                print(f"Testing case: {items}  with max weight {max_weight}")
                max_value, selected_items = knapsack(items, max_weight)
                print(f"* Maximum value: {max_value}")
                print(f"* Selected items: {selected_items}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

def main():
    """Main Menu exercise 3"""
    while True:
        print("\n\n* MAIN MENU EXERCISE 3 *")
        print("1. Enter items manually")
        print("2. Load test cases from a file")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            manual_test()
        elif choice == '2':
            filename = input("Enter the file name of the batch of tests (eg: knapsack_items.txt) : ")
            load_from_file(filename)
        elif choice == '3':
            print("Exiting...\n\n")
            break
        else:
            print("Invalid choice. Please enter a valid choice between 1 and 3.")

if __name__ == "__main__":
    main()