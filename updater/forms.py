from django import forms

class EmailUpdateForm(forms.Form):
    poiid = forms.CharField(label="POI ID", max_length=50)
    email_nuova = forms.EmailField(label="Nuova Email")
