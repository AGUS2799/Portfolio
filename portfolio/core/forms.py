from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', min_length=3, max_length=100, required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', min_length=3, max_length=100, required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject', min_length=3, max_length=100, required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(label='Message', min_length=10, max_length=1000, required=True,
        widget=forms.Textarea(attrs={'reows':10, 'class':'form-control'}))