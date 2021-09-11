output = []

with open("output/output.txt", 'r') as f:
    for line in f:
        if 'NEW' in line.split() and 'AD:' in line.split():
            output.append(line)

with open("output/output.txt", 'w') as f:
    f.write("")

if len(output) < 1:
    print("No new ads detected.")
else:
    print("NEW ADS:")
    for item in output:
        print(item.split(' ')[-1])
