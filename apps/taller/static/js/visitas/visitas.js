$(document).ready(function(){

	$('#editar-visita-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var fecha = link.data('fecha');
        var caracter = link.data('caracter');
        var comentario = link.data('comentario');
        var slot_id = link.data('slot_id');
        var tecnico_id = link.data('tecnico_id');
        var vehiculo_id = link.data('vehiculo_id');

        var modal = $(this);

        modal.find('.modal-body #id-edit').val(id);
        modal.find('.modal-body #fecha-edit').val(placa);
        modal.find('.modal-body #caracter-edit').val(tipo);
        modal.find('.modal-body #comentario-edit').val(marca);
        modal.find('.modal-body #slot-edit').val(modelo);
        modal.find('.modal-body #tecnico-edit').val(anio);

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