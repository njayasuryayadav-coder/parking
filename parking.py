def display_parking(parking_lot):
    print("\nParking Area:")
    for row in parking_lot:
        for slot in row:
            print(slot, end="\t")
        print()

def create_parking_area(rows, cols):
    return [["[ ]" for _ in range(cols)] for _ in range(rows)]

def main():
    print("Welcome to the Car Parking System")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    parking_lot = create_parking_area(rows, cols)
    parked_vehicles = {}

    while True:
        print("\nMenu:")
        print("1. Park a Vehicle")
        print("2. Remove a Parked Vehicle")
        print("3. Show Parking Area")
        print("4. Search Vehicle")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nVehicle types:")
            print("1. Car")
            print("2. Bike")
            print("3. Truck")

            v_type = input("Enter vehicle type (1/2/3): ")
            plate = input("Enter vehicle license plate: ")
            display_parking(parking_lot)
            row = int(input(f"Enter the row where you want to park the vehicle (0-{rows-1}): "))
            col = int(input(f"Enter the column where you want to park the vehicle (0-{cols-1}): "))

            if 0 <= row < rows and 0 <= col < cols and parking_lot[row][col] == "[ ]":
                symbol = "[C]" if v_type == "1" else "[B]" if v_type == "2" else "[T]"
                parking_lot[row][col] = symbol
                parked_vehicles[plate] = (row, col)
                print(f"Vehicle {plate} parked at row {row}, column {col}")
            else:
                print("Invalid location or already occupied!")

        elif choice == '2':
            plate = input("Enter vehicle license plate to remove: ")
            if plate in parked_vehicles:
                row, col = parked_vehicles[plate]
                parking_lot[row][col] = "[ ]"
                del parked_vehicles[plate]
                print(f"Vehicle {plate} removed.")
            else:
                print("Vehicle not found!")

        elif choice == '3':
            display_parking(parking_lot)

        elif choice == '4':
            plate = input("Enter vehicle license plate to search: ")
            if plate in parked_vehicles:
                row, col = parked_vehicles[plate]
                print(f"Vehicle {plate} is parked at row {row}, column {col}.")
            else:
                print("Vehicle not found!")

        elif choice == '5':
            print("Thank you for using the parking system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


