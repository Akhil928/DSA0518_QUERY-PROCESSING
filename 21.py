import pandas as pd

data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "BOB", "ChArLiE"],
    "City": ["New York", "LOS ANGELES", "cHiCaGo"]
}
df = pd.DataFrame(data)

def swap_case(df, column_name):
    df[column_name] = df[column_name].apply(lambda x: x.swapcase() if isinstance(x, str) else x)
    return df

swapped_df = swap_case(df, "Name")

print("Original DataFrame:")
print(df)
print("\nDataFrame after swapping cases in 'Name' column:")
print(swapped_df)
