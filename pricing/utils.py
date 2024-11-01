import pickle
import pandas as pd
import numpy as np


def estimate_house_price_using_floor_area(floor_area: float):
    with open('pricing/models/simple-linear-regression-model.pkl', 'rb') as file:
        model = pickle.load(file)

        x = pd.DataFrame({'area (km^2)': [floor_area]})
        y = model.predict(x)

        return np.round(y, 2)[0][0]

