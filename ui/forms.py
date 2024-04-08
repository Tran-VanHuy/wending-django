from django import forms
from .models import *


class GuestbookNumberForm(forms.ModelForm):
    class Meta:
        model = GuestbookNumber
        fields = ["name", "email", "content"]

    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Nhập họ và tên*",
                'data-sider-insert-id': '5ae28f03-4455-4a87-ac8b-6dd6a1a06010',
                'data-sider-select-id': '5657c260-f434-424a-a7b9-3c9528320c25'
            }
        )
    )

    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Nhập email",
                'data-sider-select-id': '7ce834b6-b304-4d81-868b-b3f6b60f2a72'
            }
        )
    )

    content = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.Textarea(
            attrs={
                'row': '5', 
                'class': 'form-control',
                'placeholder': "Nhập lời chúc của bạn*",
                'data-sider-insert-id': '09bd293c-6acd-4649-8695-c9f3e4f0c7d5',
                'data-sider-select-id': '2cdbd691-202f-499a-a675-32992dc844e1'
            }
        )
    )
