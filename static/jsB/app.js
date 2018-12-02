(function() {
	"use strict";

	var fcheck = document.getElementsByClassName("form-check");
	for(let i = 0; i < fcheck.length; i++) {
		fcheck[i].children[0].checked = false;
	}
	document.addEventListener('DOMContentLoaded', function(){

		function aleatorio(cantidad, rango) {
			var m_aleatorio = []
			for(let i = 0; i < cantidad; i++) {
				var n = Math.floor(Math.random() * rango)
				if(!m_aleatorio.includes(n))
					m_aleatorio.push(n);
				else
					i = i - 1;
			}
			return m_aleatorio;
		}

		class Pregunta {
			constructor(pregunta, r_correcta, r_negada, r_opcional) {
				this.pregunta = pregunta;
				this.respuestas = new Array(r_correcta, r_negada, r_opcional)
			}
		}

		class Cuestionario {
			constructor(questions = []) {
				this.preguntas = [];
				var q_aleatorias = aleatorio(10, 20);
				for(let i = 0; i < q_aleatorias.length; i++) {
					this.preguntas.push(questions[q_aleatorias[i]]);
				}
			}

		}

		const pregunta1 = new Pregunta('Pregunta1.', 'Si', 'No', 'Aveces');
		const pregunta2 = new Pregunta('Pregunta2.', 'Si', 'No', 'Aveces');
		const pregunta3 = new Pregunta('Pregunta3.', 'Si', 'No', 'Aveces');
		const pregunta4 = new Pregunta('Pregunta4.', 'Si', 'No', 'Aveces');
		const pregunta5 = new Pregunta('Pregunta5.', 'Si', 'No', 'Aveces');
		const pregunta6 = new Pregunta('Pregunta6.', 'Si', 'No', 'Aveces');
		const pregunta7 = new Pregunta('Pregunta7.', 'Si', 'No', 'Aveces');
		const pregunta8 = new Pregunta('Pregunta8.', 'Si', 'No', 'Aveces');
		const pregunta9 = new Pregunta('Pregunta9.', 'Si', 'No', 'Aveces');
		const pregunta10 = new Pregunta('Pregunta10.', 'Si', 'No', 'Aveces');
		const pregunta11 = new Pregunta('Pregunta11.', 'Si', 'No', 'Aveces');
		const pregunta12 = new Pregunta('Pregunta12.', 'Si', 'No', 'Aveces');
		const pregunta13 = new Pregunta('Pregunta13.', 'Si', 'No', 'Aveces');
		const pregunta14 = new Pregunta('Pregunta14.', 'Si', 'No', 'Aveces');
		const pregunta15 = new Pregunta('Pregunta15.', 'Si', 'No', 'Aveces');
		const pregunta16 = new Pregunta('Pregunta16.', 'Si', 'No', 'Aveces');
		const pregunta17 = new Pregunta('Pregunta17.', 'Si', 'No', 'Aveces');
		const pregunta18 = new Pregunta('Pregunta18.', 'Si', 'No', 'Aveces');
		const pregunta19 = new Pregunta('Pregunta19.', 'Si', 'No', 'Aveces');
		const pregunta20 = new Pregunta('Pregunta20.', 'Si', 'No', 'Aveces');
		var t_preguntas = [
		pregunta1,
		pregunta2,
		pregunta3,
		pregunta4,
		pregunta5,
		pregunta6,
		pregunta7,
		pregunta8,
		pregunta9,
		pregunta10,
		pregunta11,
		pregunta12,
		pregunta13,
		pregunta14,
		pregunta15,
		pregunta16,
		pregunta17,
		pregunta18,
		pregunta19,
		pregunta20
		];

		var cuestionario = new Cuestionario(t_preguntas);
		var question = document.getElementsByClassName("card-header");
		var calificar = document.getElementById("calificar");

		for(let i = 0; i < 10; i++) {
			question[i].innerHTML = (i+1) + ". " + cuestionario.preguntas[i].pregunta;
			var respuestas = cuestionario.preguntas[i].respuestas
			var answer = document.querySelectorAll(".pregunta" + (i+1));
			for(let j = 0; j < 3; j++){
				answer[j].innerHTML = respuestas[j];
			}
		}

		calificar.addEventListener('click', calificarCuestionario);



		function calificarCuestionario(event){
			var contador_correctas = 0;
			var contador_negadas = 0;
			var contador_opcional = 0;

			event.preventDefault();
			for(let i = 0; i < fcheck.length; i++) {
				if(fcheck[i].children[0].checked){	
					if(fcheck[i].children[1].innerHTML == 'Si'){
						contador_correctas += 1;
					}
					else if(fcheck[i].children[1].innerHTML == 'No'){
						contador_negadas += 1
					}
					else if(fcheck[i].children[1].innerHTML == 'Aveces') {
						contador_opcional += 1
					}
				}
			}
			//SI
			if(contador_correctas > contador_negadas && contador_correctas > contador_opcional){
				$(".modal-body").html('<img src="imgB/4.png" width="465px" height="650px"><br><a class="btn btn-primary" href="terminar.html">Terminar</a>');
				$('#respuesta').modal();
			}
			//NO
			if(contador_negadas > contador_correctas && contador_negadas > contador_opcional){
				$(".modal-body").html('<img src="imgB/6.png" width="465px" height="650px"><br><a class="btn btn-primary" href="terminar.html">Terminar</a>');
				$('#respuesta').modal();
			}
			//A veces
			if(contador_opcional > contador_correctas && contador_opcional > contador_negadas){
				$(".modal-body").html('<img src="imgB/5.png" width="465px" height="650px"><br><a class="btn btn-primary" href="terminar.html">Terminar</a>');
				$('#respuesta').modal();
			}

			if((contador_opcional == contador_correctas) && (contador_opcional == contador_negadas) && (contador_correctas == contador_negadas)){
				$(".modal-body").html('<h1>Ocurrió un error, responde el cuestionario de nuevo por favor.</h1><br><a class="btn btn-primary" href="terminar.html">Terminar</a>');
				$('#respuesta').modal();
			}
			if(contador_negadas == 10){
				$(".modal-body").html('<img src="imgB/6.png" width="465px" height="650px"><br><a class="btn btn-primary" href="terminar.html">Terminar</a>');
				$('#respuesta').modal();
			}
			if(contador_correctas ==10){
				$(".modal-body").html('<img src="imgB/4.png" width="465px" height="650px"><br><a class="btn btn-primary" href="terminar.html">Terminar</a>');
				$('#respuesta').modal();
			}
			if(contador_opcional == 10){
				$(".modal-body").html('<img src="imgB/5.png" width="465px" height="650px"><br><a class="btn btn-primary" href="terminar.html">Terminar</a>');
				$('#respuesta').modal();
			}

		}
    }); // DOM Content Loaded
})();