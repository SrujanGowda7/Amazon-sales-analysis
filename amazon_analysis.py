import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet"],
    "Sales": [50000, 30000, 20000]
}

df = pd.DataFrame(data)

print("Sales Data:\n")
print(df)

print("\nTotal Sales:", df["Sales"].sum())