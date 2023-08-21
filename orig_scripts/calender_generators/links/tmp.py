# Open the file for reading
with open('tac-monst.txt', 'r') as f:
    # Read the contents of the file
    lines = f.readlines()

# Modify each line
lines = ['    "' + line.strip() + '",\n' for line in lines]

# Print the modified lines
for line in lines:
    print(line, end='')
