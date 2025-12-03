# Read inputs
file_name = input().strip()
lower = input().strip()
upper = input().strip()

# Read all words from file
with open(file_name, 'r') as f:
    words = f.readlines()

for w in words:
    word = w.strip()
    if lower <= word <= upper:
        print(f"{word} - in range")
    else:
        print(f"{word} - not in range")
