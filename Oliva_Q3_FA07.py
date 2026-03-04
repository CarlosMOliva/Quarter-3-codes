scores = [
    [85, 88, 90],
    [78, 82, 80],
    [92, 91, 94],
    [70, 75, 72], 
    [88, 86, 89]  
]

for i in range(len(scores)):
    print("Student", i + 1, "scores:", scores[i])
    
    total = sum(scores[i])
    average = total / len(scores[i])
    
    print("Total:", total)
    print("Average:", round(average, 2))

all_scores = []
for row in scores:
    for score in row:
        all_scores.append(score)

print("Highest score:", max(all_scores))
print("Lowest score:", min(all_scores))