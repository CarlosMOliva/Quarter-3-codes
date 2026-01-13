scores = [
    [85, 88, 90],
    [78, 82, 80],
    [92, 91, 94],
    [70, 75, 72],
    [88, 86, 89] 
]

for i in range(len(scores)):

    total = sum(scores[i])
    average = total / len(scores[i])
    print(
          f"Student {i + 1} - "
        f"Total Score: {total}  "
        f"Average Score: {average}"
    )