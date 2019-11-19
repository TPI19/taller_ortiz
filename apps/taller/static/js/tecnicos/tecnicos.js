$(document).ready(function(){

	$('#editar-tecnico-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var nombre = link.data('nombre');
        var apellido = link.data('apellido');
        var correo = link.data('correo');
        var telefono = link.data('telefono');
        var direccion = link.data('direccion');
        var especializacion = link.data('especializacion');

        var modal = $(this);

        modal.find('.modal-body #id-edit').val(id);
        modal.find('.modal-body #nombre-edit').val(nombre);
        modal.find('.modal-body #apellido-edit').val(apellido);
        modal.find('.modal-body #correo-edit').val(correo);
        modal.find('.modal-body #telefono-edit').val(telefono);
        modal.find('.modal-body #direccion-edit').val(direccion);
        modal.find('.modal-body #especialidad-edit').val(especializacion);

    });

    $('#eliminar-tecnico-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var nombre = link.data('nombre');
        var apellido = link.data('apellido');

        var modal = $(this);

        modal.find('.modal-body #id-delete').val(id);
        modal.find('.modal-body #nombre-delete').val(nombre);
        modal.find('.modal-body #apellido-delete').val(apellido);

    });

})