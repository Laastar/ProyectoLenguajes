from django.db import models
from django.utils import timezone

# Create your models here.

GENDER_CHOICES = (
   ('Masculino', 'Masculino'),
   ('Femenino', 'Femenino'),
   ('Otros', 'Otros'),
)

QUESTION_CHOICES = (
	('2', 'Si'),
	('0', 'No'),
	('1', 'A veces'),
)

class DatosPersonales(models.Model):
	Nombre = models.CharField(max_length = 254)
	Ap_Paterno = models.CharField(max_length = 254)
	Ap_Materno = models.CharField(max_length = 254)
	Edad = models.CharField(max_length = 3)
	Correo = models.EmailField(max_length = 254)
	Genero = models.CharField(choices = GENDER_CHOICES, max_length = 128)

	def __str__(self):
		return self.Nombre + " " + self.Ap_Paterno

class Cuestionario(models.Model):
	Nombre = models.ForeignKey(DatosPersonales,on_delete=models.CASCADE, null=True, default=DatosPersonales)
	Fecha = models.DateField(default=timezone.now)
	Calificacion  = models.CharField(max_length=10, default=0)
	Num_Si = models.CharField(max_length=10, default=0)
	Num_No = models.CharField(max_length=10, default=0)
	Num_Aveces = models.CharField(max_length=10, default=0)
	Respuesta1 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, es un método por el cual un individuo, mediante un sistema informático, intenta tomar el control, desestabilizar o dañar otro sistema informático (ordenador, red privada, etcétera).")
	Respuesta2 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, se deberia de contar con uno para la proteccion contra malware.")
	Respuesta3 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, para controlar el acceso a ellos.")
	Respuesta4 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="No, porque provienen de fuentes desconocidas y muchas veces contienen malware.")
	Respuesta5 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, por si nuestro dispositivo llega a fallar tener nuestra informacion controlada.")
	Respuesta6 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, porque logra proteger nuestro intereses en la red y cuidar nuestra informacion que dejamos.")
	Respuesta7 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, para evitar la infeccion de virus.")
	Respuesta8 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, es más seguro y normalmente contienen un hash para comprobar los archivos descargados.")
	Respuesta9 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, es importante saber esto para poder mejorar la proteccion que le damos a nuestro equipo.")
	Respuesta10 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, esto debido al hecho que contienen una mayor cantidad de clickbaits y malware.")
	Respuesta11 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="No, las redes gratuitas normalmente están plagadas de malware y es facil que te puedan infectar, aparte los datos trasmitidos no son encriptados.")
	Respuesta12 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, es importante conocerlas para no caer presas de terceros y no dejar tanta informacion en la red.")
	Respuesta13 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, se calcula que al mes salen mas de 1000 viruses y por eso es importante siempre mantener actualizada la base de datos del antivirus.")
	Respuesta14 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, normalmente las actualizaciones contienen mejores medidad de seguridad y por eso es bueno mantener acutalizados nuestros dispositivos.")
	Respuesta15 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, es necesario saber esto para poder protegernos eficazmente contra ataques MITM, archivos auto-ejecutables, entre otros.")
	Respuesta16 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, a traves de la ingenieria social nos pueden violentar nuestra seguridad, para poder protegernos es necario no dejar tanta informacion de nosotros en la red y no compartir informacion de nosotros con personas ajenas.")
	Respuesta17 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, usualmente los pop-ups llegan a recabar informacion de nuestro navegador y para poder protegernos existen multiples instancias que pueden bloquearlos.")
	Respuesta18 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, es necesario hacer esto para poder evitar que utilizen nuestros datos en nuestra contra y proteger la privacidad tuya y de otras personas.")
	Respuesta19 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="Si, esto para que podamos recuperar nuestra informacion y en lagunos casos poder bloquear nuestro dispositivo de forma remota.")
	Respuesta20 = models.CharField(choices = QUESTION_CHOICES, max_length = 128, help_text="No, esto puede representar una vulnerabilidad de seguridad y somo propensos a la ingenieria social y por lo tanto nuestra informacion sea facilmente violentada.")