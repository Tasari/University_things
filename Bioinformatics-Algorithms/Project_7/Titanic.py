import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Wczytanie tablicy 
data = pd.read_csv('titanic.csv')
df_data = pd.DataFrame(data)

#Symbolizacja wartosci kategorycznych
df_data['Sex_clean'] = np.where(df_data['Sex'] == 'male', 0, 1)
df_data['Embarked_clean'] = np.where(df_data['Embarked']== 'S',2, np.where(df_data['Embarked']=='C', 1, 0))

#Usuniecie kolumny zawierajacej wiele NaN
del df_data['Cabin']

#Usuniecie wierszy zawierajacych NaN
data_poprawne=data[[
"Survived",
"Pclass",
"Sex_clean",
"Age",
"SibSp",
"Parch",
"Fare",
"Embarked_clean"
]].dropna(axis=0, how='any')

#Podzielenie ludzi ze na zywych i martwych
surv = data_poprawne.loc[df_data['Survived'] == 1]
dead = data_poprawne.loc[df_data['Survived'] == 0]

#Dodanie tabeli i histogramow z wiekami zywych i martwych
surv_age = surv['Age']
dead_age = dead['Age']
figure = plt.figure(figsize=(20, 20))#tworze figure o stalym rozmiarze na ekranie
ax1 = figure.add_subplot(3,2,1)#dodaje subplot do figury
ax1.hist(surv_age, bins=np.arange(0, 100 ,5), label=["Zywi"], color='g')
ax1.legend()#dodanie legendy
ax2 = figure.add_subplot(3,2,2)
ax2.hist(dead_age, bins=np.arange(0, 100 ,5), label=["Martwi"], color='r')
ax2.legend()

#Tworzenie tabeli zywych i martwych w zaleznosci od plci
surv_male = surv.loc[data_poprawne['Sex_clean'] == 0]
surv_female = surv.loc[data_poprawne['Sex_clean'] == 1]
dead_male = dead.loc[data_poprawne['Sex_clean'] == 0]
dead_female = dead.loc[data_poprawne['Sex_clean'] == 1]

#Tworzenie histogramów zywych i martwych ze wzgledu na plec i wiek
ax3 = figure.add_subplot(3,2,3)
ax3.hist([surv_male['Age'], surv_female['Age']], bins=np.arange(0,100,5), label=["Zywi mezczyzni","Zywe kobiety"], color=['b', 'm']) 
ax3.legend()
ax4 = figure.add_subplot(3,2,4)
ax4.hist([dead_male["Age"], dead_female['Age']],bins=np.arange(0,100,5), label= ["Martwi mezczyzni", "Martwe kobiety"])
ax4.legend()

#tworzenie tabel z cenami biletow zywych i martwych
surv_fare = surv['Fare']
dead_fare = dead['Fare']

#tworzenie histogramow zywych i martwych w zaleznisci od ceny biletu
ax5 = figure.add_subplot(3,2,5)
ax5.hist(surv_fare, bins=np.arange(0,200, 10), label=['Koszt biletu zywych'], color='y')
ax5.legend()
ax6 = figure.add_subplot(3,2,6)
ax6.hist(dead_fare, bins=np.arange(0,200, 10), label=['Koszt biletu martwych'], color='k')
ax6.legend()
plt.show()