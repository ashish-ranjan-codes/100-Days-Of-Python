# learn about list

states = ["bihar", "goa", "kerala", "delhi"]
print(f"First state is {states[0]}")
print(f"Last state is {states[-1]}")

states[2] = "assam"
print(f"3rd state is changed to {states[2]}")

states.append("tamil nadu") # appends at the end
print(f"Last newly added state is {states[-1]}")

print("Full list of states is: ")
for i in range(len(states)):
    print(states[i])