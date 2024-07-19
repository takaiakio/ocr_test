import pytesseract
from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm

# Tesseractのパスを設定（Windowsの場合）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            text = pytesseract.image_to_string(Image.open(image))
            return HttpResponse(f'<h1>Extracted Text:</h1><p>{text}</p>')
    else:
        form = ImageUploadForm()
    return render(request, 'ocr_app/home.html', {'form': form})

def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            text = pytesseract.image_to_string(Image.open(image))
            return HttpResponse(f'<h1>Extracted Text:</h1><p>{text}</p>')
    else:
        form = ImageUploadForm()
    return render(request, 'ocr_app/upload.html', {'form': form})

