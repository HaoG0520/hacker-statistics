# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(3)

# Generate and print random float
#print(np.random.rand())

# Use randint() to simulate a dice
#print(np.random.randint(1,7))

# Try again to use randint() again, to see if these two are same
#print(np.random.randint(1,7))

# Initialize all_walks
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)
