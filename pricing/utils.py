import pickle
import pandas as pd
import numpy as np


def estimate_house_price_using_floor_area(floor_area: float):
    with open('pricing/models/simple-linear-regression-model.pkl', 'rb') as file:
        model = pickle.load(file)

        x = pd.DataFrame({'area (km^2)': [floor_area]})
        y = model.predict(x)

        return np.round(y, 2)[0][0]


def estimate_house_price_using_floor_area_and_location(floor_area: float, location: str):
    town_indices = {'accra': 0, 'kumasi': 1, 'kwabenya': 2}
    towns = pd.DataFrame({'town': ['accra', 'kumasi', 'kwabenya']})
    towns = pd.get_dummies(towns).astype(int)
    towns = towns[['town_accra', 'town_kwabenya']]
    town_index = town_indices[location]
    town = towns.iloc[[town_index]]
    town.reset_index(drop=True, inplace=True)

    x = pd.DataFrame({'area (km^2)': [floor_area]})
    x = pd.concat([x, town], axis=1)

    with open('pricing/models/multiple-linear-regression-model.pkl', 'rb') as file:
        model = pickle.load(file)
        y = model.predict(x)
        return np.round(y, 2)[0][0]
