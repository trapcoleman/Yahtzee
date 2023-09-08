from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import YahtzeeScorecard, Player

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# Create add scorecard form
class AddScorecard(forms.ModelForm):
    username = forms.ModelChoiceField(queryset=Player.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label="Username")
    ones = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Ones")
    twos = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Twos")
    threes = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Threes")
    fours = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Fours")
    fives = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Fives")
    sixes = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Sixes")
    upper_bonus = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Upper Bonus")
    upper_total = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Upper Total")
    three_of_a_kind = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="3 of a Kind")
    four_of_a_kind = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="4 of a Kind")
    full_house = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Full House")
    small_straight = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Small Straight")
    large_straight = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Large Straight")
    yahtzee = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Yahtzee")
    yahtzee_bonus = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Yahtzee Bonus")
    chance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Chance")
    lower_total = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Lower Total")
    grand_total = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), label="Grand Total")

    class Meta:
        model = YahtzeeScorecard
        exclude = ("user",)
