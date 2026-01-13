students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"]
scores = [
    [85, 88, 90],
    [78, 82, 80],
    [92, 91, 94],
    [70, 75, 72],
    [88, 86, 89]
]

totals = []

for i in range(len(scores)):
    total_score = sum(scores[i])
    totals.append(total_score)
    print(f"{students[i]} - Scores: {scores[i]} Total Score: {total_score}")

max_score = max(totals)
max_student = totals.index(max_score)
print(f"Highest total score: {students[max_student]} ")

min_score = min(totals)

difference = max_score - min_score
print(f"Difference between highest and lowest total scores: {difference}")