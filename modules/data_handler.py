import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataHandler:

    def load_data(self, file):
        df = pd.read_csv(file)
        return df

    def preprocess_data(self, df, selected_features):

        data = df[selected_features]

        # remove missing values
        data = data.dropna()

        # scale features
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)

        return scaled_data, data