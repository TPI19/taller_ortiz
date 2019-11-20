$(document).ready(function(){

	$('#editar-vehiculo-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var placa = link.data('placa');
        var tipo = link.data('tipo');
        var marca = link.data('marca');
        var modelo = link.data('modelo');
        var anio = link.data('anio');
        var cliente = link.data('cliente');

        var modal = $(this);

        modal.find('.modal-body #id-edit').val(id);
        modal.find('.modal-body #placa-edit').val(placa);
        modal.find('.modal-body #tipo-edit').val(tipo);
        modal.find('.modal-body #marca-edit').val(marca);
        modal.find('.modal-body #modelo-edit').val(modelo);
        modal.find('.modal-body #anio-edit').val(anio);

    });

    $('#eliminar-visita-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var fecha = link.data('fecha');

        var modal = $(this);

        modal.find('.modal-body #id-delete').val(id);
        modal.find('.modal-body #fecha-delete').val(fecha);

    });

})