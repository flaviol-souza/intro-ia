import pickle

filename = 'model.pkl'
with open(filename, 'rb') as file:
    model_ml = pickle.load(file)

y = model_ml.predict([[5.8, 2.7, 5.1, 1.9]])
print(f'Y:{y}')