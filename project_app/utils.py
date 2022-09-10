import pickle
import json
import config
import numpy as np

class WeightPrediction():
    def __init__(self,Length1, Length2, Length3, Height, Width, Species):
        self.Length1 = Length1
        self.Length2 = Length2
        self.Length3 = Length3
        self.Height = Height
        self.Width = Width
        self.Species = 'Species_'+ Species

    def load_model(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
            self.linear_reg_model = pickle.load(f)

        with open (config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_weight(self):
        self.load_model()
        Species_index = self.json_data['columns'].index(self.Species)

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.Length1
        test_array[1] = self.Length2
        test_array[2] = self.Length3
        test_array[3] = self.Height
        test_array[4] = self.Width
        test_array[Species_index] = 1

        print("Test Array :", test_array)

        predicted_weight = np.around(self.linear_reg_model.predict([test_array])[0],2)  # added [0] to convert to list
        return predicted_weight


if __name__ == "__main__":
    Length1 = 23.20
    Length2 = 25.40
    Length3 = 30.00
    Height = 11.52
    Width = 4.02
    Species = 'Parkki'

    wgt_pre = WeightPrediction(Length1, Length2, Length3, Height, Width, Species)
    wgt_pre.get_predicted_weight()