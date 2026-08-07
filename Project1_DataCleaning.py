import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
excel_path = base_dir / "Dataset for Data Analytics.xlsx"
output_path = base_dir / "Cleaned_Dataset.xlsx"

df = pd.read_excel(excel_path)
df.columns = [col.strip() for col in df.columns]

if "Date" in df.columns and "date" not in df.columns:
    df = df.rename(columns={"Date": "date"})
elif "date" not in df.columns:
    raise KeyError("Expected a date column named 'Date' or 'date' in the dataset.")

df.head()
df.info()
print(df.isnull().sum())
print(df.duplicated().sum())

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["Product"] = df["Product"].astype(str).str.strip().str.title()
df["OrderStatus"] = df["OrderStatus"].astype(str).str.strip().str.title()
df["UnitPrice"] = df["UnitPrice"].round(2)
df["TotalPrice"] = df["TotalPrice"].round(2)
print("Duplicate OrderIDs:", df["OrderID"].duplicated().sum())

df.to_excel(output_path, index=False)
print(f"Cleaned data saved to {output_path}")