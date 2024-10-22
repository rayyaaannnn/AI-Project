note_denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

note_count = {}

amount = int(input("Enter the amount: "))

for note in note_denominations:
    count = amount // note
    amount %= note
    note_count[note] = count

print("Note Denomination\tCount")
for note, count in note_count.items():
    if count > 0:
        print(f"{note}\t\t{count}")

total_notes = sum(note_count.values())
print(f"\nTotal Number of Notes: {total_notes}")