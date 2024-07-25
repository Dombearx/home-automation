from datetime import datetime


class Date:
    @staticmethod
    def get_current_date():
        return datetime.now().strftime("%Y-%m-%d")
