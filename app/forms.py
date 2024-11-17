from django import forms

class PredictionForm(forms.Form):
    feature_1 = forms.FloatField(label="Feature 1", required=True)
    feature_2 = forms.FloatField(label="Feature 2", required=True)
    # Agrega más campos según sea necesario
