"""
This is the Entry point for Training the Machine Learning Model.

Written By: swapnil sonawane
Version: 1.0
Revisions: None

"""
from sklearn.model_selection import train_test_split

from application_logging import logger
from data_ingestion import data_loder
from data_preprocessing import preprocessing


class trainModel:
    def __init__(self):
        self.log_writer = logger.App_Logger()
        self.file_object = open("Training_Logs/ModelTrainingLog.txt", 'a+')

    def trainingModel(self):
        # Logging the start of Training
        self.log_writer.log(self.file_object, "Start of Training(trainiModel.trainModel.trainingModel)")
        try:
            # Getting the data from the source
            data_getter = data_loder.Data_Getter(self.file_object, self.log_writer)
            data = data_getter.get_data()
            """ doing the data preprocessing"""
            preprocessor = preprocessing.Preprocessor(self.file_object, self.log_writer)

            # crete separate features and labels
            X, Y = preprocessor.separate_label_features(data, label_column_name='default.payment.next.month')

            # Check if missing values are present in the dataset
            is_null_present, cols_with_missing_values = preprocessor.is_null_present(X)

            # if missing values are there, replace them appropriatly
            if (is_null_present):
                X = preprocessor.impute_missing_values(X, cols_with_missing_values)  # missing value imputation

            # train_test_split
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20,
                                                                random_state=100)
            print(x_train)
            print("x_test\n", x_test)
            # x_train_scaled,y_train_scaled
            train_x = preprocessor.scale_numerical_columns(x_train)
            test_x = preprocessor.scale_numerical_columns(x_test)
            return train_x, test_x
        except Exception as e:
            # logging the unsuccessful Training
            self.log_writer.log(self.file_object, "Unsuccessful End Of Training(trainiModel.trainModel.trainingModel)")
            self.file_object.close()
            raise Exception
