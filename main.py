import pandas as pd 
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#fin import


data=pd.read_excel("./ressource/Sleep_health_and_lifestyle_dataset_bruit.xlsx")
df = pd.DataFrame(data)
def clean(data):
    data = data.drop(["Person ID"], axis=1) 
    """
    for col in cols:
        data[col].fillna(data[col].median(), inplace=True)
    """
    return data

data = clean(data)
le = preprocessing.LabelEncoder()
columns = ["Gender", "Occupation","BMI Category","Sleep Disorder"]
for col in columns:
    data[col] = le.fit_transform(data[col])
    print(le.classes_)#stocke les classes trouvées par la méthode fit()

# Utiliser la méthode value_counts() pour compter le nombre d'occurrences de chaque valeur
# Calculer le pourcentage de chaque valeur en divisant le compte par le nombre total d'éléments
percentages = df["BMI Category"].value_counts() / len(df) * 100
# Afficher les pourcentages
print(percentages)
