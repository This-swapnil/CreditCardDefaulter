from DataTransform_Training.DataTransformation import dataTransform
from Training_Raw_data_validation.rawValidation import Raw_Data_validation


class train_validation():
    def __init__(self):
        self.raw_data = Raw_Data_validation()
        self.dataTransform = dataTransform()
