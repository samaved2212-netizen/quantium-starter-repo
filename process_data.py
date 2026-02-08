import pandas as pd
from pathlib import Path

data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

all_data = []

for file in csv_files:
    df = pd.read_csv(file)
    df = df[df["product"] == "Pink Morsels"]
    df["sales"] = df["quantity"] * df["price"]
    df = df[["sales", "date", "region"]]
    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)
final_df.to_csv("pink_morsels_sales.csv", index=False)

print("done")
