from django import forms

CONTESTS = (
    ('','Select'),
    ('abc','AtCoder Begginer Contest'),
    ('arc','AtCoder Regular Contest'),
    ('agc','AtCoder Grand Contest'),
)

NUMBERS = [[0 for i in range(2)] for j in range(101)]
NUMBERS[0] = {'',"Select"}
for i in range(100):
    for j in range(2):
        if j == 0:
            if i+1 / 10 < 1:
                NUMBERS[i+1][j] = "00" + str(i+1)
            elif i+1 / 10 >= 1 or i+1 / 10 < 10:
                NUMBERS[i+1][j] = "0" + str(i+1)
            else:
                NUMBERS[i+1][j] = str(i+1)
        if j == 1:
            NUMBERS[i+1][j] = str(i+1)
            

QUESTIONS = (
    ('','Select'),
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
    ('e','E'),
    ('f','F'),
)

class ViewContests(forms.Form):
    contests = forms.ChoiceField(
        label='Contests',
        required=True,
        disabled=False,
        choices=CONTESTS,
        widget=forms.Select,
    )
    numbers = forms.ChoiceField(
        label='Numbers',
        required=True,
        disabled=False,
        choices=NUMBERS,
        widget=forms.Select,
    )
    questions = forms.ChoiceField(
        label='Questions',
        required=True,
        disabled=False,
        choices=QUESTIONS,
        widget=forms.Select,
    )

    