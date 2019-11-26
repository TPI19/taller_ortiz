$(document).ready(function(){

	$('#agregar-visita-modal').on('show.bs.modal', function(event){

		var modal = $(this);
		var link = $(event.relatedTarget);

		var id_vehiculo = link.data('id-vehiculo');
		var id_cliente = link.data('id-cliente');
		var placa = link.data('placa');
		var marca = link.data('marca');
		var modelo = link.data('modelo');
		var anio = link.data('anio');

		modal.find('.modal-body #vehiculo-visita').val(id_vehiculo);
		modal.find('.modal-body #cliente-visita').val(id_cliente);
		modal.find('.modal-body #placa-visita').val(placa);
		modal.find('.modal-body #marca-visita').val(marca);
		modal.find('.modal-body #modelo-visita').val(modelo);
		modal.find('.modal-body #anio-visita').val(anio);


	});

	$('#fecha-visita').datetimepicker({
		sideBySide: true,
		format: 'DD/MM/YYYY HH:mm A',
		icons:
		{
			time: "fa fa-clock-o",
			date: "fa fa-calendar",
			up: "fa fa-arrow-up",
			down: "fa fa-arrow-down",
			previous: "fa fa-chevron-left",
			next: "fa fa-chevron-right",
			today: "fa fa-clock-o",
			clear: "fa fa-trash-o"
		},

	});


	vehiculo_sin_visitas();
	function vehiculo_sin_visitas(){

		var visitas = document.getElementsByClassName('tbody-visitas');

		for (var i = visitas.length - 1; i >= 0; i--) {

			if(!(visitas[i].childNodes.length>1)){

				var tr = document.createElement('tr');
				tr.setAttribute('class','d-flex text-center');
				
				var td = document.createElement('td');
				td.setAttribute('class','col-12');

				var p = document.createElement('p');
				p.setAttribute('class','lead');
				p.innerHTML='No se han registrado visitas con el vehículo';

				td.appendChild(p);

				tr.appendChild(td);

				visitas[i].appendChild(tr);
			}
		}
	}

})