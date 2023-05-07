import seaborn as sns
import matplotlib.pyplot as plt

# Read data from data.txt
with open('data.txt', 'r') as f:
    data = []
    for line in f:
        line = line.strip().split(':')
        if len(line) == 2:
            _, affinity = line
            try:
                data.append(float(affinity))
            except ValueError:
                continue

# Plot density plot using seaborn
sns.kdeplot(data, shade=True)
plt.xlabel('Binding Affinity')
plt.show()