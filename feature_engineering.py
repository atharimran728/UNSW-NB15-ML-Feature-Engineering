import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv("UNSW_NB15_training-set.csv")

print("Columns:", df.columns)

# 2. Inspect Categorical Features -------------------------------
categorical_cols = ["proto", "service", "state"]
print("\nCategorical columns:", categorical_cols)
print(df[categorical_cols].head())

# 3. Encode Categorical Features --------------------------------
ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
cat_encoded = ohe.fit_transform(df[categorical_cols])

cat_df = pd.DataFrame(cat_encoded, columns=ohe.get_feature_names_out(categorical_cols))

# 4. Drop original categorical cols & combine -------------------
df_num = df.drop(columns=categorical_cols + ["id", "attack_cat"]) 
df_final = pd.concat([df_num.reset_index(drop=True), cat_df.reset_index(drop=True)], axis=1)

# 5. Feature Scaling --------------------------------------------
X = df_final.drop(columns=["label"])
y = df_final["label"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Feature matrix shape:", X_scaled.shape)
