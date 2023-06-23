import pandas as pd 
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#fin import


data=pd.read_excel("./ressource/Sleep_health_and_lifestyle_dataset_bruit.xlsx")

def clean(data):
    data = data.drop(["Person ID"], axis=1) 
    """
    cols = ["SibSp", "Parch", "Fare", "Age"]
    for col in cols:
        data[col].fillna(data[col].median(), inplace=True)
    data.Embarked.fillna("U", inplace=True)
    """
    return data

data = clean(data)
le = preprocessing.LabelEncoder()
columns = ["Gender", "Occupation","BMI Category","Sleep Disorder"]
for col in columns:
    data[col] = le.fit_transform(data[col])
    print(le.classes_)#stocke les classes trouvées par la méthode fit()
