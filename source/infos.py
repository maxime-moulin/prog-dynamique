class DocumentInfos:

    title = u'Programmation dynamique'
    first_name = 'Cédric'
    last_name = 'Donner'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'Juillet'
    seminary_title = u'Algorithmes et structures de données II'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/donnerc/prog-dynamique"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()