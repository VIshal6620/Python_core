def full_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces for alignment
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for k in range(1, 2 * i):
            print("*", end="")
        # Move to the next line
        print()

# Call the function with n=5
full_pyramid(5)
