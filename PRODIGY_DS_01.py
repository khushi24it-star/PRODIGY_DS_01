import matplotlib.pyplot as plt
import seaborn as sns

# Built-in Titanic Dataset load kar rahe hain
df = sns.load_dataset("titanic")

# Canvas layout set kar rahe hain (2 plots ek saath)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 1. Histogram: Age Distribution (Continuous Variable)
sns.histplot(
    data=df,
    x="age",
    bins=20,
    kde=True,
    color="skyblue",
    ax=axes[0],
)
axes[0].set_title("Age Distribution of Passengers")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Count")

# 2. Bar Chart: Gender Distribution (Categorical Variable)
sns.countplot(data=df, x="sex", palette="pastel", ax=axes[1])
axes[1].set_title("Gender Distribution")
axes[1].set_xlabel("Gender")
axes[1].set_ylabel("Count")

# Clean Layout
plt.tight_layout()
plt.show()
