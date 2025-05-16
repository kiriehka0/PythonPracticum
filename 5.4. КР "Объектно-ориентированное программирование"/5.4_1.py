class Comment:
    def __init__(self, username, birth_date, info):
        self.username = username
        self.birth_date = birth_date
        self.info = info

    def get_author(self):
        return self.username

    def get_date(self):
        date = self.birth_date.split()[0]
        return date

    def get_time(self):
        time = self.birth_date.split()[1]
        return time

    def get_text(self):
        return self.info
