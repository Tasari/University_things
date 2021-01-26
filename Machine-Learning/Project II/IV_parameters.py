#%%
'''
Używam grid searcha aby wyszukać odpowiednie parametry dla naszego algorytmu, zmieniam opcje 
'''
from sklearn.model_selection import GridSearchCV
param_grid = [
    {'dual': [0, 1], 
     'fit_intercept':[0, 1], 
     'penalty':['l1', 'l2', 'none'], 
     'solver':['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
     },
  ]

dt = LogisticRegression(max_iter=1000, 
                        random_state=15, 
                        multi_class='ovr', 
                        n_jobs=3
                        )
'''
Używam scoringu f1 w grid searchu gdyż równanie na F1 uwzględnia precyzję i recall
F1 = 2 * (precision * recall) / (precision + recall)
'''
grid_search = GridSearchCV(dt, 
                           param_grid, 
                           cv=5,
                           scoring='f1', 
                           return_train_score=True, 
                           error_score=0.0
                           )
grid_search.fit(games_data, games_labels)

print(grid_search.best_params_)
cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(mean_score, params)
    
    
'''
Wyniki Grid searcha(usunięte wartoci 0.0), najlepszy model ostateczny jest przypisywany bez koniecznosci uruchamiania
{'dual': 0, 'fit_intercept': 1, 'penalty': 'l2', 'solver': 'liblinear'}
0.7273578949469075 {'dual': 0, 'fit_intercept': 0, 'penalty': 'l1', 'solver': 'liblinear'}
0.7248543653852264 {'dual': 0, 'fit_intercept': 0, 'penalty': 'l1', 'solver': 'saga'}
0.7280292605830871 {'dual': 0, 'fit_intercept': 0, 'penalty': 'l2', 'solver': 'newton-cg'}
0.7249227708730003 {'dual': 0, 'fit_intercept': 0, 'penalty': 'l2', 'solver': 'lbfgs'}
0.725525366448369 {'dual': 0, 'fit_intercept': 0, 'penalty': 'l2', 'solver': 'liblinear'}
0.7237547824907493 {'dual': 0, 'fit_intercept': 0, 'penalty': 'l2', 'solver': 'sag'}
0.7248543653852264 {'dual': 0, 'fit_intercept': 0, 'penalty': 'l2', 'solver': 'saga'}
0.7280239854259815 {'dual': 0, 'fit_intercept': 0, 'penalty': 'none', 'solver': 'newton-cg'}
0.7256466862404395 {'dual': 0, 'fit_intercept': 0, 'penalty': 'none', 'solver': 'lbfgs'}
0.7237547824907493 {'dual': 0, 'fit_intercept': 0, 'penalty': 'none', 'solver': 'sag'}
0.7248543653852264 {'dual': 0, 'fit_intercept': 0, 'penalty': 'none', 'solver': 'saga'}
0.727942515395613 {'dual': 0, 'fit_intercept': 1, 'penalty': 'l1', 'solver': 'liblinear'}
0.7248543653852264 {'dual': 0, 'fit_intercept': 1, 'penalty': 'l1', 'solver': 'saga'}
0.7280417617051845 {'dual': 0, 'fit_intercept': 1, 'penalty': 'l2', 'solver': 'newton-cg'}
0.7260644626831448 {'dual': 0, 'fit_intercept': 1, 'penalty': 'l2', 'solver': 'lbfgs'}
0.7288508759560649 {'dual': 0, 'fit_intercept': 1, 'penalty': 'l2', 'solver': 'liblinear'}
0.7237547824907493 {'dual': 0, 'fit_intercept': 1, 'penalty': 'l2', 'solver': 'sag'}
0.7248543653852264 {'dual': 0, 'fit_intercept': 1, 'penalty': 'l2', 'solver': 'saga'}
0.7279043086281671 {'dual': 0, 'fit_intercept': 1, 'penalty': 'none', 'solver': 'newton-cg'}
0.7255375683232342 {'dual': 0, 'fit_intercept': 1, 'penalty': 'none', 'solver': 'lbfgs'}
0.7237547824907493 {'dual': 0, 'fit_intercept': 1, 'penalty': 'none', 'solver': 'sag'}
0.7248543653852264 {'dual': 0, 'fit_intercept': 1, 'penalty': 'none', 'solver': 'saga'}
0.6736752563647026 {'dual': 1, 'fit_intercept': 0, 'penalty': 'l2', 'solver': 'liblinear'}
0.6736752563647026 {'dual': 1, 'fit_intercept': 1, 'penalty': 'l2', 'solver': 'liblinear'}

z czego wynika że powinnimy zmienić tylko solver, reszta domyslnych wartosci 
jest odpowiednia, najlepszy solver do naszego problemu to liblinear.
Solver liblinear jest stworzony stricte do problemów klasyfikacji binarnej 
więc to wyjasnia dlaczego to on jest najlepszy.
'''
#%%
'''
Uruchamiam najlepszy model dla naszych danych testowych aby zobaczyć jak model
radzi sobie z nowymi danymi.
'''

final_model = LogisticRegression(max_iter=1000, 
                                 random_state=15, 
                                 multi_class='ovr', 
                                 solver='liblinear',
                                 )
final_model.fit(games_data, games_labels)
final_predictions = final_model.predict(games_data_test)

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

confusion = confusion_matrix(final_predictions, games_labels_test)
f1 = f1_score(final_predictions, games_labels_test)
precision = precision_score(final_predictions, games_labels_test)
recall = recall_score(final_predictions, games_labels_test)
print("Wyniki najlepszego modelu")
print("Macierz błędu najlepszego rozwiązania\n", confusion)
print("F1 najlepszego rozwiązania: {:.2f}%".format(f1*100))
print("Precyzja najlepszego rozwiązania: {:.2f}%".format(precision*100))
print("Recall najlepszego rozwiązania: {:.2f}%".format(recall*100))
'''
Z otrzymanego rozwiązania możemy wywnioskować że wynik gry w znacznej częsci 
opiera sie wlasnie na jej poczatku, jednak nie jest on decydujacy, zatem druzyna
ktora przegrywa poczatek meczu, w dalszym ciągu może się odbić i wygrać mecz, 
czy to poprzez podniesienie swojego poziomu gry, czy przez spadek poziomu gry
przeciwnika, gdy ten widzi swoją dominację nad grą, przez co skupia się na niej 
mniej.
'''