from django import forms
from .models import DatosPersonales, Cuestionario

class DatosForm(forms.ModelForm):
	class Meta:
		model = DatosPersonales
		fields = ('Nombre','Ap_Paterno','Ap_Materno','Edad','Correo', 'Genero')

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Cuestionario
		fields = (
			'Respuesta1',
			'Respuesta2',
			'Respuesta3',
			'Respuesta4',
			'Respuesta5',
			'Respuesta6',
			'Respuesta7',
			'Respuesta8',
			'Respuesta9',
			'Respuesta10',
			'Respuesta11',
			'Respuesta12',
			'Respuesta13',
			'Respuesta14',
			'Respuesta15',
			'Respuesta16',
			'Respuesta17',
			'Respuesta18',
			'Respuesta19',
			'Respuesta20',
			)
		labels = {
		'Respuesta1' : "1-¿Sabes lo que es un ciberataque?",
		'Respuesta2' : "2-¿Cuentas con algún antivirus y antimalware en tus dispositivos electrónicos ?",
		'Respuesta3' : "3-¿Le pones contraseñas de seguridad a tus dispositivos electrónicos ?",
		'Respuesta4' : "4-¿Alguna vez has obtenido Sotfware Pirata ?",
		'Respuesta5' : "5-¿Realizas copias de seguridad en tus equipos ?",
		'Respuesta6' : "6.-¿Usas navegacion privada?",
		'Respuesta7' : "7.- ¿Vacunas tus USB´S?",
		'Respuesta8' : "8.-¿Descargas archivos de paginas oficiales?",
		'Respuesta9' : "9.-¿Sabes cual es el antivirus más efectivo en la acutalidad?",
		'Respuesta10' : "10.-¿Te preocupa navegar en sitios inseguros?",
		'Respuesta11' : "11.-¿Te has conectado a la red del metro?",
		'Respuesta12' : "12. ¿Conoces más de una medida de seguridad, para navegar con seguridad?",
		'Respuesta13' : "13. ¿Actualizas tu antivirus con frecuencia y antes de ejecutarlo?",
		'Respuesta14' : "14. ¿Actualizas el software de tus dispositivos?",
		'Respuesta15' : "15. ¿Conoces las medidas que tomar en caso de sitios electrónicos nocivos?",
		'Respuesta16' : "16. ¿Está al tanto de los nuevos métodos usados por la ingeniería social?",
		'Respuesta17' : "17.¿Utilizas extenciones o complementos en tus navegadores web, que bloqueen páginas emergentes que podrían violar tu privacidad?",
		'Respuesta18' : "18.¿Tienes encriptados tus fotos, audios, videos, mensajes, datos personales etc,de la memoria microsd de tus dispositivos moviles, para proteger tu identidad en caso de robo o extravío?",
		'Respuesta19' : "19.¿Tú dispositivo móvil te permite saber su localizacón en caso de extravío o robo ?",
		'Respuesta20' : "20.¿En redes sociales compartes datos personales, como ubicación, lugar de trabajo, escuela a la que asistes, pareja sentimental, parentesco con los diversos integrantes de tu familia, que te pueden exponer ante ataques a tu integridad digital y personal?"
		}