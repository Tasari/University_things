#%%
import numpy as np1
import matplotlib.pyplot as plt
import pandas as pd
import os

KATALOG_PROJEKTU = os.path.join(os.getcwd(), "league_games_stats")
KATALOG_DANYCH = os.path.join(KATALOG_PROJEKTU,"dane")
KATALOG_WYKRESOW = os.path.join(KATALOG_PROJEKTU, "wykresy")
os.makedirs(KATALOG_WYKRESOW, exist_ok=True)
os.makedirs(KATALOG_DANYCH, exist_ok=True)

def load_data(filename="lol_games.csv"):
    return pd.read_csv(os.path.join(KATALOG_DANYCH, filename))

"""
Link do danych(https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min)
Informacje o danych:
Plik "lol_games.csv" zawiera dane z prawie 10 000 rankingowych meczy(5 vs 5) z gry 
"League of Legends",są one pobierane z gier osób o najwyższych wynikach
(Ranga: Diament I oraz wyższe), z 10 minuty meczu (Koniec fazy początkowej, 
w której w dużej częsci wypadków wynik meczu jest przesądzony, jednak drużyna 
przeciwna może jeszcze się odbić gdyż cały mecz trwa około 30 minut)
Sam plik zawiera dane o wyniku meczu czyli zniszczeniu wrogiej bazy, 
oraz o statystykach każdej z dwóch drużyn (Zarobione pieniądze, śmierci, zabicia, 
pokonane stwory i inne dane mające wpływ na wynik końcowy)
"""
games = load_data()
'''
Usuwam wszystkie dane drużyny czerwonej gdyż chce nauczyć 
mój model przewidywania tylko na podstawie wyników drużyny niebieskiej, 
usuwam również przedrostek blue, gdyż teraz mamy dane tylko niebieskiej 
drużyny więc przedrostek jest zbędny
'''
for column in games.columns:
    if column.startswith("red"):
        del games[column]
    elif column.startswith("blue"):
        games = games.rename(columns = {column:column[4:]})
'''
Usuwam również gameId, gdyż nie przyda się nam do niczego, 
oraz statystyki blueTotalMinionsKilled oraz blueTotalGold, 
gdyż są to statystyki równoznaczne ze swoimi odpowiednikami "PerMin"
'''
del games["gameId"]
del games["TotalGold"]
del games["TotalMinionsKilled"]
stats = games.describe()

'''
Robie histogram danych które nie są binarne przed 10 minutą meczu. 
'''

games[['WardsPlaced', 'WardsDestroyed', 'Kills', 'Deaths', 'Assists', 'EliteMonsters',
       'TowersDestroyed', 'AvgLevel', 'TotalExperience', 'TotalJungleMinionsKilled', 
       'GoldDiff', 'ExperienceDiff','CSPerMin', 'GoldPerMin']
    ].hist(bins=15, figsize=(12, 8))
plt.tight_layout()
plt.savefig(os.path.join(KATALOG_WYKRESOW,'histogramy.jpg')) 
plt.show()

'''
Tworzę nowy atrybut, KDA który pokazuje ile jest Kills+Assists/Death 
oraz tworze nowy dataframe w ktorym zmieniam wartosci Death na 1, 
który jest używany do obliczen żeby nie dzielić przez 0
'''
games_notnull_deaths = games.copy()
games_notnull_deaths.loc[games_notnull_deaths["Deaths"]<1, "Deaths"] = 1
games["KDA"] = games["Kills"]+games["Assists"]/games_notnull_deaths["Deaths"]
del games_notnull_deaths

'''
Następnie tworzę macierz korelacji sprawdzając jaka zmienna najbardziej koreluje ze zwycięstwem drużyny
'''
corr_matrix = games.corr()
print(corr_matrix["Wins"].sort_values(ascending=False))

'''
Widząc dużą korelację wielu zmiennych, uznałem że uwzględnie w macierzy 
tylko zmienne powyżej 40% korelacji, widząc również że 2 razy widzimy 
korelację zawierającą Gold, możemy stwierdzić że zdobyte złoto gra znaczącą 
rolę w zwycięstwie drużyny, co przekłada się na wiedzę z gry, że większe 
zarobki pozwalają na zakup lepszych przedmiotów które następnie pozwalają na 
dominacje nad przeciwnikiem, co tym bardziej potwierdza najwyższa korelacja 
zmiennej GoldDiff, będącej różnicą złota miedzy drużyną niebieską a czerwoną.
'''
pd.plotting.scatter_matrix(games[["Wins", "GoldDiff", 'ExperienceDiff', "GoldPerMin"]])
plt.savefig(os.path.join(KATALOG_WYKRESOW,'korelacje.jpg'), dpi=300 ) 
plt.show()

