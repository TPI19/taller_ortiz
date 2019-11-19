$(document).ready(function(){

	$('#editar-especialidad-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var nombre = link.data('nombre');
        var descripcion = link.data('descripcion');

        var modal = $(this);

        modal.find('.modal-body #id-edit').val(id);
        modal.find('.modal-body #nombre-edit').val(nombre);
        modal.find('.modal-body #descripcion-edit').val(descripcion);

    });

    $('#eliminar-especialidad-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var nombre = link.data('nombre');

        var modal = $(this);

        modal.find('.modal-body #id-delete').val(id);
        modal.find('.modal-body #nombre-delete').val(nombre);

    });

})