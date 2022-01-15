"""
This is the Entry point for Training the Machine Learning Model.

Written By: swapnil sonawane
Version: 1.0
Revisions: None

"""
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
        except Exception as e:
            # logging the unsuccessful Training
            self.log_writer.log(self.file_object, "Unsuccessful End Of Training(trainiModel.trainModel.trainingModel)")
            self.file_object.close()
            raise Exception
