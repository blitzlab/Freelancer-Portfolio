from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = 'Name', required=True, widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Name', 'id':'name', 'data-validation-required-message':'Please enter your name.', 'aria-invalid':'false'}))
    email = forms.EmailField(label = 'Email', required=True, widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Email', 'id':'email', 'data-validation-required-message':'Please enter your email.', 'aria-invalid':'false'}))
    phone = forms.IntegerField(label = 'Phone', required=True, widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Phone', 'id':'phone', 'data-validation-required-message':'Please enter your phone number.', 'aria-invalid':'false'}))
    message = forms.CharField(label = 'Message', required=True, widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Message', 'id':'message', 'data-validation-required-message':'Please enter your message.', 'aria-invalid':'false'}))

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(ContactForm, self).__init__(*args, **kwargs)
