import pandas as pd

df = pd.read_csv("assets/cisti_podaci.csv")

df_kandidati = df[
    (df["Metan_Senzor"] == "Pozitivno") &
    (df["Organske_Molekule"] == "Da")
]

prosjek_temp = df_kandidati["Temp_Tla_C"].mean()

print(f"Prosječna temperatura kandidata: {prosjek_temp:.2f} °C")
