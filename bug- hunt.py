# BUG: The loop condition is wrong, so the loop never runs.
count = 1

while count < 0:
    print(count)
    count += 1


# BUG: The total is reset inside the loop.
scores = [10, 20, 30]
total = 0

for score in scores:
    total = 0
    total += score

print("Total:", total)


# BUG: A score of exactly 50 is incorrectly treated as failing.
score = 50

if score > 50:
    print("Pass")
else:
    print("Fail")
