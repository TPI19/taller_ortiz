$(document).ready(function(){

	$('#editar-cita-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var fecha_propuesta = link.data('fecha_propuesta');
        var caracter = link.data('caracter');
        var estado = link.data('estado');
        var mensaje = link.data('mensaje');
        var cliente = link.data('cliente');


        var modal = $(this);

        modal.find('.modal-body #id-edit').val(id);
        modal.find('.modal-body #fecha-edit').val(fecha_propuesta);
        modal.find('.modal-body #caracter-edit').val(caracter);
        modal.find('.modal-body #estado-edit').val(estado);
        modal.find('.modal-body #mensaje-edit').val(mensaje);
     
    });

    $('#eliminar-cita-modal').on('show.bs.modal', function(event){

        var link = $(event.relatedTarget);

        var id = link.data('id');
        var fecha_propuesta = link.data('fecha_propuesta');

        var modal = $(this);

        modal.find('.modal-body #id-delete').val(id);
        modal.find('.modal-body #fecha-delete').val(fecha_propuesta);

    });


   

})

document.getElementById("controlE").onkeyup = function() {
    var controlE_= this.value.toLowerCase() ;
    document.querySelectorAll('.table tbody tr').forEach(function(e){
      var encontro_ =false;
      e.querySelectorAll('td').forEach(function(e){
        if (e.innerHTML.toLowerCase().indexOf(controlE_)>=0){
          encontro_=true;
        }
      }); 
      if (encontro_){
        e.style.display = '';
      }else{
        e.style.display = 'none';
      }
    });              
}