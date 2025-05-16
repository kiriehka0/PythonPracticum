class Comment:
    def __init__(self, username, birth_date, info):
        self.username = username
        self.birth_date = birth_date
        self.info = info
        self._approved = False
        self._edited = False
        self._sub_comments = []

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

    def get_sub_comments(self):
        return self._sub_comments.copy()

    def __iadd__(self, sub_comment):
        if not isinstance(sub_comment, SubComment):
            raise TypeError("Can only add SubComment instances")
        sub_comment.set_parent(self)
        return self

    def __lt__(self, other):
        if not isinstance(other, SubComment):
            return False
        current = other.get_parent()
        while current is not None:
            if current == self:
                return True
            if isinstance(current, SubComment):
                current = current.get_parent()
            else:
                current = None
        return False

    def __gt__(self, other):
        if isinstance(other, Comment):
            if isinstance(self, SubComment):
                current = self.get_parent()
                while current is not None:
                    if current == other:
                        return True
                    if isinstance(current, SubComment):
                        current = current.get_parent()
                    else:
                        current = None
        return False

    def __str__(self):
        if not self.info:
            return " "
        return f"{self.info}\n[{self.username} ({self.birth_date})]\n"

    def __repr__(self):
        return f"Comment({self.username}, {self.get_date()}, {self.get_time()})"


class SubComment(Comment):
    def __init__(self, username, birth_date, info, parent=None):
        super().__init__(username, birth_date, info)
        self._parent = parent
        if parent is not None and isinstance(parent, Comment):
            parent._sub_comments.append(self)

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        if self._parent is not None and isinstance(self._parent, Comment):
            try:
                self._parent._sub_comments.remove(self)
            except ValueError:
                pass
        self._parent = parent
        if parent is not None and isinstance(parent, Comment):
            parent._sub_comments.append(self)

    def __repr__(self):
        return f"SubComment({self.username}, {self.get_date()}, {self.get_time()}, {repr(self._parent)})"



