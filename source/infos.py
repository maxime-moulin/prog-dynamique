class DocumentInfos:

    title = u'Programmation dynamique'
    first_name = 'Maxime'
    last_name = 'Moulin'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Janvier'
    seminary_title = u'Algorithmes et structures de données II'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/donnerc/prog-dynamique"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()