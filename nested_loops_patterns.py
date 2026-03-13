# --- GEOMETRIC PATTERNS: ADVANCED ---
size = 7  # You can change this to any odd number for best results

# --- TASK 1: THE X-PATTERN (Diagonals) ---
print("--- Task 1: Letter X ---")
for block in range(size):
    for section in range(size):
        if block == section or block + section == size - 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print("")

# --- TASK 2: THE HOLLOW SQUARE (Frame) ---
print("\n--- Task 2: Hollow Square ---")
for block in range(size):
    for section in range(size):
        if block == 0 or block == size - 1 or section == 0 or section == size - 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print("")

# --- TASK 3: THE CHESSBOARD (Alternating) ---
print("\n--- Task 3: Chessboard ---")
for block in range(size):
    for section in range(size):
        # Using modulo to alternate symbols
        if (block + section) % 2 == 0:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print("")

# --- TASK 4: THE HOURGLASS (Combined Logic) ---
print("\n--- Task 4: Hourglass ---")
for block in range(size):
    for section in range(size):
        # Top/Bottom rows + both diagonals
        if block == 0 or block == size - 1 or block == section or block + section == size - 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print("")
