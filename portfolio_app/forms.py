from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=100, required=True)
    email = forms.EmailField(label='Mail', required=True)
    phone = forms.CharField(label='Номер телефона', max_length=20, required=True)
    subject = forms.CharField(label='Тип услуги', max_length=100, required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)
