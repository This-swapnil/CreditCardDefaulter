from datetime import date, datetime


class App_Logger:
    def __init__(self):
        pass

    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = datetime.date()
        self.current_time = self.now.strftime("%H:%M:%s")
        file_object.write(
            str(self.date + " /"+str(self.current_time)+"\t\t"+log_message+"\n"))
