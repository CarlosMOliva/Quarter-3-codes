steppers = ["Jim", "Jack", "John"]
steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

totals = []

for i in range(len(steps)):
    total_steps = sum(steps[i])
    totals.append(total_steps)
    print(f"{steppers[i]} - Steps: {steps[i]} Total steps: {total_steps}")

max_steps = max(totals)
max_stepper = totals.index(max_steps)
print(f"Highest total steps: {steppers[max_stepper]} ")

min_steps = min(totals)

difference = max_steps - min_steps
print(f"Difference between highest and lowest total steps: {difference}")