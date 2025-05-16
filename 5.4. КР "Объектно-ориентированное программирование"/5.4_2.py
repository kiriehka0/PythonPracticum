class Comment:
    def __init__(self, username, birth_date, info):
        self.username = username
        self.birth_date = birth_date
        self.info = info
        self._approved = False
        self._edited = False

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

    def approve(self):
        self._approved = True

    def is_approved(self):
        return self._approved

    def set_text(self, text):
        self.info = text
        self._approved = False
        self._edited = True

    def is_edited(self):
        return self._edited

    def __str__(self):
        if not self.info:
            return " "
        return f"{self.info}\n[{self.username} ({self.birth_date})]\n"
