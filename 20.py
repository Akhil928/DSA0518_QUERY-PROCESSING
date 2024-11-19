import pandas as pd
data = {
    "Country": [
        "Viet Nam", "Uruguay", "Cte d'Ivoire",
        "Colombia", "Saint Kitts and Nevis"
    ]
}
df = pd.DataFrame(data)
substring = "Viet"
indices = df[df['Country'].str.contains(substring, na=False)].index.tolist()
print("Indices of rows with the substring:", indices)
