from django import forms
from . import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('CINEMA_KG', 'CINEMA_KG'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'CINEMA_KG':
            clothes_parser = parser.parser()
            for i in clothes_parser:
                models.Clothes.objects.create(**i)
