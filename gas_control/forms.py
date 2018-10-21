from django import forms


class PostForm(forms.Form):
    Gas = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'gás que deseja atualizar'
            }
        )
    )
    Volume_Verificado = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': '(apenas numeros)'
            }
        )
    )
    Nome_do_Verificador = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'nome e sobrenome'
            }
        )
    )
    Data_de_Verificacao = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 70%; width:100%;',
                'placeholder': 'dd/mm/aaaa'
            }
        )
    )
