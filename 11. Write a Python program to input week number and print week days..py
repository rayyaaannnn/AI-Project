weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

week_number = int(input("Enter the week number: "))
start_day = input("Enter the starting day of the week (e.g., Sunday, Monday): ")

if start_day in weekdays:
    start_index = weekdays.index(start_day)
else:
    print("Invalid starting day. Defaulting to Sunday.")
    start_index = 0

print(f"Week {week_number}:")
for i in range(7):
    print(f"Day {i + 1}: {weekdays[(start_index + (week_number - 1) * 7 + i) % 7]}")