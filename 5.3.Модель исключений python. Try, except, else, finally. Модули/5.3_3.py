class Tuoo:
    def __repr__(self):
        raise Exception


try:
    t = Tuoo()
    func(None, {"один": "два"}, t)
except Exception:
    print("Ура! Ошибка!")
