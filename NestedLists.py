records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    scores = [name, score]
    records.append(scores)

records.sort(key=lambda x: x[1])

# Find the second lowest score
lowest_score = records[0][1]
second_lowest_score = None
for record in records:
    if record[1] > lowest_score:
        second_lowest_score = record[1]
        break

# Find the names of students with the second lowest score
second_lowest_names = [record[0] for record in records if record[1] == second_lowest_score]
sorted_names = sorted(second_lowest_names)

for name in sorted_names:
    print(name)
