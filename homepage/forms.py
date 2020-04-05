from django import forms

#RADIO Btn Selectors
CHOICES = [('Customer','customer'),('Store Owner','owner')]
# Login Form Validation
class user_form(forms.Form):
    username = forms.CharField(max_length=30, required = True)
    password = forms.CharField(max_length=20, required = True, widget = forms.PasswordInput)
    
    def clean(self):
        data = super().clean()
        if len(data.get('username')) < 3:
            raise forms.ValidationError ("NAME Must Be Greater Than 3 ")
        if len(data.get('password')) < 8:
            raise forms.ValidationError ("Password Must contain At least 8 characters!!")
        
# Registeration Form Validation
class reg_form(forms.Form):
    username = forms.CharField(max_length= 30, required = True)
    password = forms.CharField(max_length= 20, required = True, widget = forms.PasswordInput)
    email = forms.EmailField(max_length = 40, required = True)
    address = forms.CharField(max_length= 30, required = True)
    category = forms.ChoiceField(choices= CHOICES, widget=forms.RadioSelect)

    def clean(self):
        valid = super().is_valid()
        print (valid)
