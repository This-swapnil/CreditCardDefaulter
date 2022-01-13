from application_logging.logger import App_Logger


class dBOperation:
    """
          This class shall be used for handling all the SQL operations.

          Written By: swapnil sonawane
          Version: 1.0
          Revisions: None

          """

    def __init__(self):
        self.path = "Traninig_Database/"
        self.badFilePath = "Traning_Raw_files_validated/Bad_Raw"
        self.goodFilePath = "Training_Raw_files_validated/Good_Raw"
        self.logger = App_Logger()

    def DataBaseConnection(self, DatabaseName):
        """
                        Method Name: dataBaseConnection
                        Description: This method creates the database with the given name and if Database already exists then opens the connection to the DB.
                        Output: Connection to the DB
                        On Failure: Raise ConnectionError

                         Written By: swapnil sonawane
                        Version: 1.0
                        Revisions: None

                        """
        pass
