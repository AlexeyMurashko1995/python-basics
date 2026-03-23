# --- GEOMETRIC PATTERNS PROJECT ---

# Set the size for all shapes (Try changing this to 10 or 15!)
size = 8 

# --- TASK 1: THE X-PATTERN ---
# Combines both main and anti-diagonals
print("--- Task 1: Letter X ---")
for block in range(size):
    for section in range(size):
        # Universal formula for an X-shape
        if block == section or block + section == size - 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print("")

# --- TASK 2: THE HOLLOW SQUARE (Frame) ---
# Highlights only the borders of the grid
print("\n--- Task 2: Hollow Square ---")
for block in range(size):
    for section in range(size):
        # Check if we are on any of the four edges
        if block == 0 or block == size - 1 or section == 0 or section == size - 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print("")

# --- TASK 3: THE RIGHT TRIANGLE ---
# A wall that grows row by row
print("\n--- Task 3: Right Triangle ---")
for block in range(size):
    for section in range(block + 1):
        print("#", end=" ")
    print("")