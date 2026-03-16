# Two Room Vacuum Cleaner Agent

# Initial room states
roomA = input("Enter state of Room A (clean/dirty): ")
roomB = input("Enter state of Room B (clean/dirty): ")

location = "A"

while True:
    if location == "A":
        print("\nAgent in Room A")

        if roomA == "dirty":
            print("Cleaning Room A")
            roomA = "clean"
        else:
            print("Room A already clean")

        location = "B"

    else:
        print("\nAgent in Room B")

        if roomB == "dirty":
            print("Cleaning Room B")
            roomB = "clean"
        else:
            print("Room B already clean")

        location = "A"

    # Check if both rooms are clean
    if roomA == "clean" and roomB == "clean":
        print("\nBoth rooms are clean. Task completed.")
        break
