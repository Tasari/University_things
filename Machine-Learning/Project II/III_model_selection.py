import numpy as np

from sklearn.metrics import mean_squared_error


from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

from sklearn.model_selection import cross_val_score
'''
Dobieranie modelu oparte o stronę
https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
oraz informacje z zajęć
'''
sgd=SGDClassifier(max_iter=5, tol=-np.infty, random_state=15, 
                  loss="log", penalty="l2")
sgd.fit(games_data, games_labels)

gnb = GaussianNB()
gnb.fit(games_data, games_labels)

svc = SVC(random_state=15)
svc.fit(games_data, games_labels)

log = LogisticRegression(max_iter=1000, random_state=15)
log.fit(games_data, games_labels)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(games_data, games_labels)

dt = DecisionTreeClassifier(random_state=15)
dt.fit(games_data, games_labels)

rf = RandomForestClassifier(n_estimators=10, random_state=15)
rf.fit(games_data, games_labels)

abc = AdaBoostClassifier(random_state=15)
abc.fit(games_data, games_labels)

'''
Tworzę dwie listy, jedną z klasyfikatorami a drugą z odpowiadającymi im nazwami
tak żeby móc iterować wspólnie po nazwach z klasyfikatorami
'''
classifiers = [gnb, svc, log, neigh, dt, rf, abc, sgd]
names = ["GaussianNB", "SVC", "LogisticRegression", "KNeighbors", 
         "DecisionTree", "RandomForest", "AdaBoost", "SGD"]

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_curve
from sklearn.model_selection import cross_val_predict

plt.figure(figsize=(8, 6))

'''
Iteruje po każdym klasyfikatorze, przewidując dane treningowe, tak żeby dobrać
najlepszy klasyfikator, oraz wykreslić krzywą ROC (skrypt z zajęć)
Iteracja zajmuje chwilę, ze względu na długie działanie SVC
'''

for ident, classifier in zip(names, classifiers):
    label_train_predict = cross_val_predict(classifier, games_data, 
                                            games_labels, cv=10)
    confusion = confusion_matrix(games_labels, label_train_predict)
    print(ident)
    print(confusion)
    print("F1: ", f1_score(games_labels, label_train_predict))
    print("Precision: ", precision_score(games_labels, label_train_predict))
    print("Recall: ", recall_score(games_labels, label_train_predict))
    print()
    fpr, tpr, t = roc_curve(games_labels, label_train_predict)
    plt.plot(fpr, tpr, label=ident)
    
plt.legend(loc="lower right", fontsize=16)
plt.plot([0, 1], [0, 1], 'k--')
plt.axis([0, 1, 0, 1])
plt.xlabel('False Positive Rate', fontsize=16)
plt.ylabel('True Positive Rate (recall)', fontsize=16)
plt.savefig(os.path.join(KATALOG_WYKRESOW, "roc_curve_comparison_plot"))
plt.show()

'''
LogisticClassifier ma najwyższy F1_score
(F1 = 2 * (precision * recall) / (precision + recall)) 
zatem będę do niego dobierać parametry w kolejnym kroku.
'''