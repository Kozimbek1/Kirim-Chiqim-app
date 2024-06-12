from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction


class CustomUserCreationForm(UserCreationForm):
    """
      Form for user registration with custom fields.

      Extends UserCreationForm to include additional fields for first name, last name, and customized labels and placeholders.

      Attributes:
      username (str): Username of the user.
      first_name (str): First name of the user.
      last_name (str): Last name of the user.
      password1 (str): Password of the user.
      password2 (str): Password confirmation.
      """
    username = forms.CharField(
        label="Foydalanuvchi nomi",
        max_length=150,
        help_text=None,
        widget=forms.TextInput(attrs={'placeholder': 'Foydalanuvchi nomini kiriting'})
    )
    first_name = forms.CharField(
        label="Ism",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting'})
    )
    last_name = forms.CharField(
        label="Familiya",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Familiyangizni kiriting'})
    )
    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'placeholder': 'Parolni kiriting'}),
        help_text='Kamida 8 ta belgi',
    )
    password2 = forms.CharField(
        label="Parolni tasdiqlash",
        widget=forms.PasswordInput(attrs={'placeholder': 'Parolni tasdiqlash'}),
        help_text='Kamida 8 ta belgi',
    )



    class Meta:
        """
        Meta class defining model and fields.
        """
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


class TransactionForm(forms.ModelForm):
    """
    Form for creating or updating a transaction.

    Uses Transaction model to define fields.

    Attributes:
    amount (decimal): Amount of the transaction.
    transaction_type (str): Type of the transaction (KIRIM or CHIQIM).
    """
    class Meta:
        """
        Meta class defining model and fields.
        """
        model = Transaction
        fields = ['amount', 'transaction_type']
