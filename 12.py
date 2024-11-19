import pandas as pd
import numpy as np

# Create a DataFrame with 10 rows and 4 columns filled with random values
np.random.seed(42)  # For reproducibility
data = np.random.randn(10, 4)

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=["A", "B", "C", "D"])

# Define a function to style the entire DataFrame
def style_black_yellow(_):
    return "background-color: black; color: yellow"

# Apply the style to the DataFrame
styled_df = df.style.map(style_black_yellow)

# Save the styled DataFrame to an HTML file
styled_df.to_html("styled_dataframe_black_yellow.html")
