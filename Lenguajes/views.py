from django.shortcuts import render, redirect
from .forms import DatosForm, QuestionForm
from .models import Cuestionario
from django.db.models import F

# Create your views here.

def inicio(request):
	return render(request, 'index.html')

def objetivo(request):
	return render(request, 'objetivo.html')

def datos(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = DatosForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			form.save()
			# redirect to a new URL:
			return redirect('cuestionario')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = DatosForm()
	return render(request, 'datos.html', {'form': form})

def cuestionario(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = QuestionForm(request.POST)
		lista = []
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			respuesta = form.cleaned_data['Respuesta1']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta2']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta3']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta4']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta5']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta6']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta7']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta8']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta9']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta10']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta11']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta12']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta13']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta14']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta15']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta16']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta17']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta18']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta19']
			lista.append(respuesta)
			respuesta = form.cleaned_data['Respuesta20']
			lista.append(respuesta)

			nos = lista.count('0') * 0
			sis = lista.count('2') * 0.5
			noses = lista.count('1') * 0.25

			nos2 = lista.count('0')
			sis2 = lista.count('2')
			noses2 = lista.count('1')

			maximos = [nos2, noses2, sis2]
			valmax = maximos.index(max(maximos))

			if(valmax == 0):
				request.session["max"] = 0
			elif(valmax == 1):
				request.session["max"] = 1
			elif(valmax == 2):
				request.session["max"] = 2

			total = nos + sis + noses
			total = repr(total)

			form.save()

			C = Cuestionario.objects.all()[Cuestionario.objects.count()-1]
			C.Calificacion = F('Calificacion') + total
			C.Num_Si = F('Num_Si') + sis2
			C.Num_No = F('Num_No') + nos2
			C.Num_Aveces = F('Num_Aveces') + noses2
			C.save()

			# redirect to a new URL:
			return redirect('terminar')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = QuestionForm()
	return render(request, 'cuestionario.html', {'form': form})

def terminar(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = QuestionForm(request.POST)
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return render(request, 'terminar.html', {'form': form})
	# if a GET (or any other method) we'll create a 
	# if a GET (or any other method) we'll create a blank form
	else:
		form = QuestionForm()
	return render(request, 'terminar.html', {'form': form})