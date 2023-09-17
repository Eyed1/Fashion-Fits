import pickle
from sklearn.ensemble import RandomForestRegressor

f = open("regressor_size2.pkl", "rb")
regress = pickle.load(f)

print(regress.predict([[11, 27]]))
