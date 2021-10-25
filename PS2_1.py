import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problem 1

Sig_Eqs = pd.read_csv('./earthquakes-2021-10-13_20-48-54_+0800.tsv', header=0, sep='\t')

Year_list = list(set(Sig_Eqs['Year'].values.tolist()))
Year_list.remove(Year_list[0])
Year_list.sort()

Country_list = Sig_Eqs['Country'].values.tolist()
Country_list = list(set(Country_list))
Country_list.remove(np.nan)
Country_list.sort()
death_list_country = []
for C in Country_list:
    Country_death = Sig_Eqs[Sig_Eqs['Country'] == C]
    death = np.nansum(Country_death['Deaths'].values)
    death_list_country.append(death)

country_death = dict(zip(Country_list, death_list_country))
order = sorted(country_death.items(), key=lambda x: x[1], reverse=True)

Mag_list_year = []
for C in Year_list:
    Year_Mag = Sig_Eqs[Sig_Eqs['Year'] == C]
    Mag = Year_Mag['Mag'].values.tolist()
    Mag_6 = list(filter(lambda x: x > 6, Mag))
    Mag_list_year.append(len(Mag_6))


# plt.plot(Year_list, Mag_list_year)
# plt.show()


def CountEq_LargestEq(Country_name):
    Country_df = Sig_Eqs[Sig_Eqs['Country'] == Country_name]
    number = Country_df.shape[0]
    Max_ = Country_death.max()
    Max_mag = Max_.Mag
    Max_df = Country_df[Country_df['Mag'] == Max_mag]
    Max_mag_date = Max_df[['Year', 'Mo', 'Dy', 'Mag']]
    return Max_mag_date, number


a, b = CountEq_LargestEq('GREECE')
for i in range(10):
    a, b = CountEq_LargestEq(order[i][0])
    print(order[i][0], ':', b, '\n', a)

# plt.plot(Year_list,Mag_list_year)
# plt.show()
