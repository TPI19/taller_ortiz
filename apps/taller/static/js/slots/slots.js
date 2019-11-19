$(document).ready(function(){

	$('#editar-slot-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var disponible = link.data('disponible');
        var reservacion = link.data('reservacion');
        
        var modal = $(this);

        modal.find('.modal-body #id-edit').val(id);
        modal.find('.modal-body #disponible-edit').val(disponible);
        modal.find('.modal-body #reservacion-edit').val(reservacion);
    });

    $('#eliminar-slot-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');

        var modal = $(this);

        modal.find('.modal-body #id-delete').val(id);

    });

})