
NIVEL_CHOICES = (
    (1, 'Iniciação Científica'),
    (2, 'Mestrado'),
    (3, 'Doutorado'),
    (4, 'Pós-Doc.'),
)

ROLE_CHOICES = (
    (1, 'Aluno'),
    (2, 'Orientador'),
)
DOC_TYPES = (
    (1, '.docx'),
    (2, '.xlsx'),
    (3, '.ppx'),

)


def pro_ch(username):
    all_pro = UserProjects.objects.all().filter(user=username)
    proj = []
    for i in all_pro:
        proj.append(i.projeto)


def conc(choice):
    for i in range(0, len(st)):
        tp = ()
        tp +=(i,)
        print(tp)

        tp += (st[i], )
        print(tp)

        choice += (tp, )
        print(choice)
