# randomly bill payment by friends
import random
friends = ["ankit", "balvir", "aman", "kishu"]
num = random.randint(0,len(friends)-1)

print(f"{num+1}th friend will pay bill i.e {friends[num]}")