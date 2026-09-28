scores = [85, 72, 68, 45, 91, 56, 39, 78]

passed = 0
failed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score} - Grade: {grade}")

    if score >= 50:
        passed += 1
    else:
        failed += 1

    total += score

average = total / len(scores)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {round(average, 1)}")
