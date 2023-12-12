import pandas as pd
#reads the CSV file
df = pd.read_csv("NYPD_Arrest_Data__Year_to_Date_.csv")

#changes the letter representing a borough to the actual borough name
df['ARREST_BORO'] = df['ARREST_BORO'].replace({'K': 'Brooklyn'})
df['ARREST_BORO'] = df['ARREST_BORO'].replace({'M': 'Manhattan'})
df['ARREST_BORO'] = df['ARREST_BORO'].replace({'B': 'Bronx'})
df['ARREST_BORO'] = df['ARREST_BORO'].replace({'Q': 'Queens'})
df['ARREST_BORO'] = df['ARREST_BORO'].replace({'S': 'Staten Island'})


# writing into the file
df.to_csv("AllDetails2.csv", index=False)

print(df)
