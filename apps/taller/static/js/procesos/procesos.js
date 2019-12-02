$(document).ready(function(){

	var btn_nuevo_proceso = $('#btn-nuevo-proceso');
	var btn_quitar_proceso = $('#btn-quitar-proceso');

	btn_nuevo_proceso.click(function(e){

		e.preventDefault();

		$('#div-proceso').attr('class','col-12 mt-3 pt-2 border');

		$('#div-proceso-registrado').attr('class','d-none');

		$('#div-btn-agregar').attr('class','d-none');
		$('#nuevo').attr('value','1');


	});

	btn_quitar_proceso.click(function(e){

		e.preventDefault();

		$('#div-proceso-registrado').attr('class','form-group row align-items-center');

		$('#div-proceso').attr('class','d-none');
		$('#div-btn-agregar').attr('class','col-12 text-right');
		$('#nuevo').attr('value','0');
	});
	
});