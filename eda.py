import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("churn.csv")

sns.countplot(x="Churn", data=df)
plt.show()

sns.histplot(df["MonthlyCharges"])
plt.show()

sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.show()

sns.scatterplot(
    x="tenure",
    y="MonthlyCharges",
    hue="Churn",
    data=df
)
plt.show()

sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")
plt.show()
