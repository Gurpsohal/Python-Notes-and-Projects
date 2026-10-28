import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mt

df=pd.read_csv('Most Streamed Artists on Spotify (17_07_2026).csv')
dups = df.drop_duplicates().info()
print(df.describe())


#freq_gen = (df.value_counts(df['Primary Genre']))
freq_sing = (df.value_counts(df[' Artist Type']))
#freq_gen.to_csv('/Users/gurpartapsohal/Desktop/Desktop/Python/Data_Viz/out.csv')
freq_sing.to_csv('/Users/gurpartapsohal/Desktop/Desktop/Python/Data_Viz/out.csv')

plt.pie(df.value_counts(df['Primary Genre']), labels= df.value_counts(df['Primary Genre']), startangle=90)
plt.show()
