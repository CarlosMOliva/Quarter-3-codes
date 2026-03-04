steppers = ["Jim", "Jack", "John"]
steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

daily_totals = []

for day_index in range(len(steps[0])):
    total_for_day = 0
    for person in steps:
        total_for_day += person[day_index]
    daily_totals.append(total_for_day)

for i in range(len(days)):
    print(f"{days[i]} total steps: {daily_totals[i]}")

max_steps = max(daily_totals)
most_active_day = days[daily_totals.index(max_steps)]

print(f"Most active day: {most_active_day}")