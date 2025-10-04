from django.forms import ModelForm
from django.utils.html import strip_tags
from django import forms
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        ordering = ['-created_at', 'name']
        model = Product
        fields = [
            "name", "price", "description", "thumbnail", "category", "is_featured",
            "team", "season", "size", "sleeve_type", "condition", "manufacturer", "stock",
        ]
        labels = {
            "sleeve_type": "Sleeve",
        }

    def clean_name(self):
        return strip_tags(self.cleaned_data.get("name", ""))

    def clean_description(self):
        return strip_tags(self.cleaned_data.get("description", ""))

    def clean_team(self):
        return strip_tags(self.cleaned_data.get("team", ""))

    def clean_season(self):
        return strip_tags(self.cleaned_data.get("season", ""))

    def clean_condition(self):
        return strip_tags(self.cleaned_data.get("condition", ""))

    def clean_manufacturer(self):
        return strip_tags(self.cleaned_data.get("manufacturer", ""))