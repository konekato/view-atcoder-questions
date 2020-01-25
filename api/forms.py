from django import forms

CONTESTS = (
    {'','Select'},
    ('ABC','AtCoder Begginer Contest'),
    ('ARC','AtCoder Regular Contest'),
    ('AGC','AtCoder Grand Contest'),
)

class ViewContests(forms.Form):
    contests = forms.ChoiceField(
        label='Contests',
        required=True,
        disabled=False,
        choices=CONTESTS,
        widget=forms.Select,
    )