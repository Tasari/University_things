'''
Jako iÅ¼ nie brakuje mi danych oraz wszystkie wartosci w datasecie sa liczbowe
to od razu przechodze do dzielenia danych na treningowe i testujace, robie 
to poprzez splicing danych gdyż metoda sklearn wybiera dane losowo, 
co daje różne wyniki za każdym razem, a nie chciałem żeby konieczne
było uruchamianie długiego grid searcha
'''

train_amount = int(9879*0.8)
train_set, test_set = games[:7903], games[7903:]

games_data = train_set.drop("Wins", axis=1)
games_labels = train_set["Wins"].copy()

games_data_test = test_set.drop("Wins", axis=1)
games_labels_test = test_set["Wins"].copy()