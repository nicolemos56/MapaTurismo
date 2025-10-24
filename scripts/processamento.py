from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd


data = {
    'provincia': ['Luanda', 'Benguela', 'Huíla', 'Namibe'],
    'densidade_pontos_turisticos': [12.4, 8.1, 5.7, 7.3],
    'distancia_aeroporto': [4.3, 12.0, 8.9, 14.1],
    'densidade_populacional': [1023, 800, 650, 420],
    'indice_acessibilidade': [0.91, 0.83, 0.76, 0.79],
    'potencial_real': [1, 1, 0, 0]  # variável alvo (turismo alto = 1)
}

df=pd.DataFrame(data)
#salvando o dataframe em um arquivo CSV
df.to_csv('dados_turisticos.csv', index=False)
print("Dataframe criado e salvo como 'dados_turisticos.csv'")


df = pd.read_csv("data/model_inputs_mock.csv")

X = df.drop(columns=["provincia", "potencial_real"])
y = df["potencial_real"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

print("Acurácia:", accuracy_score(y_test, y_pred))
