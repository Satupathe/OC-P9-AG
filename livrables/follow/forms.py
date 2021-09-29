from django import forms


class FollowForm(forms.Form):
    name = forms.CharField(max_length=50)
