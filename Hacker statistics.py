# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(3)

# Generate and print random float
print(np.random.rand())

# Use randint() to simulate a dice
#print(np.random.randint(1,7))

# Try again to use randint() again, to see if these two are same
#print(np.random.randint(1,7))

# Initialize random_walk
random_walk = [0]

# Complete the 100 dice toss
for x in range(1000) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = max(step - 1,0)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
        # Implement clumsiness
    if np.random.rand() == 0.001 :
        step = 0
    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
