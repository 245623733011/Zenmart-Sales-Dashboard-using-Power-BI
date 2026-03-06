import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.countplot(x=df['City'])
plt.title("Sales Count by City")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x=df['PaymentMethod'])
plt.title("Payment Method Distribution")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x=df['ProductCategory'])
plt.title("Sales by Product Category")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['UnitPrice'], kde=True)
plt.title("Unit Price Distribution")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df['Month'].value_counts().index, df['Month'].value_counts().values)
plt.title("Monthly Purchase Frequency")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df['DayName'].value_counts().index, df['DayName'].value_counts().values)
plt.title("Sales by Day of Week")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df['Quantity'], df['Revenue'])
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.show()

corr = df.corr(numeric_only=True)
plt.figure(figsize=(8,5))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()