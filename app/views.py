from django.shortcuts import render
from .forms import PredictionForm
from django.http import JsonResponse
import joblib

# Cargar el modelo
MODEL_PATH = 'SVC.pkl'
model = joblib.load(MODEL_PATH)

def index(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extraer los valores del formulario
            feature_1 = form.cleaned_data['feature_1']
            feature_2 = form.cleaned_data['feature_2']
            # Realizar predicción
            prediction = model.predict([[feature_1, feature_2]])[0]
            return JsonResponse({'prediction': prediction})
    else:
        form = PredictionForm()

    return render(request, 'index.html', {'form': form})
