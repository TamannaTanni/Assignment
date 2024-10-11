from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def tempconv(request):
    if request.method == 'POST':
        # Get data from the form
        precision = int(request.POST.get('precision'))
        temperature = float(request.POST.get('temperature'))
        scale = request.POST.get('scale')

        # Convert Fahrenheit to Celsius
        if scale == 'C':
            converted_temp = (temperature - 32) * 5.0 / 9.0
            result = f"{converted_temp:.{precision}f} °C"

        # Convert Celsius to Fahrenheit (if needed)
        # You can add this if functionality extends to the reverse
        elif scale == 'F':
            converted_temp = (temperature * 9.0/5.0) + 32
            result = f"{converted_temp:.{precision}f} °F"

        # Pass the converted temperature to the template
        return render(request, 'temp.html', {'converted_temperature': result})

    return render(request, 'temp.html')

