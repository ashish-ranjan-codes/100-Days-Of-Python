# let's explore some inbuilt functions to handle numbers

scores = [23, 45, 12 , 90, 98, 76, 56, 48, 100, 28, 4, 99, 91]

total_sum = sum(scores)
maximum_score = max(scores)

print(f"Total sum of scores = {total_sum}")
print(f"Maximum score in scores = {maximum_score}")

# this can also be done using loop
sum = 0
for score in scores:
    sum += score

print(f"Total score using for loop = {sum}")

max = 0
for score in scores:
    if score > max:
        max = score

print(f"Maximum score using for loop = {max}")