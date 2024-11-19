import pandas as pd
import numpy as np

np.random.seed(42) 
data = np.random.randn(10, 4)

df = pd.DataFrame(data, columns=["A", "B", "C", "D"])

def style_black_yellow(_):
    return "background-color: black; color: yellow"

styled_df = df.style.map(style_black_yellow)

styled_df.to_html("styled_dataframe_black_yellow.html")
