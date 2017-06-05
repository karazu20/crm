/**
 * Created by Abraham on 24/05/2017.
 */


$( "#atras" ).click(function() {
  goBack();
});
function goBack() {
    window.history.back();
}

$('#submit_button').click(function(){
	$("#form").submit();
	//return true;
});


function date (label, id) {
     $("#div-date").clone(true).removeAttr("id").attr("id", "div-" + id).appendTo("#div-lead");
    $('#div-'+ id).show();
    $('#label_date').val(label);
    $('#label_date').text(label);
    var date_input = $('input[name="date"]'); //our date input has the name "date"
    var container = $('.bootstrap-iso form').length > 0 ? $('.bootstrap-iso form').parent() : "body";
    var options = {
        format: 'yyyy/mm/dd',
        container: container,
        todayHighlight: true,
        autoclose: true,
    };


    date_input.datepicker(options);
    //$("#div-date").clone(true).removeAttr("id").attr("id", "div-" + id).appendTo("#div-lead");
    //$('#div-'+ id).show();
}


function  addFecha (idForm,label, name){
    console.log( "add date");

    $('<p>').text(label).appendTo(idForm);
    $("<input type='text' value='' />")
     .attr("id", 'id_' + name)
     .attr("name", name)
     .appendTo(idForm);

}
function addTD (idTabla, value){

    $(idTabla).find('tbody')
    .append($('<tr>')
        .append($('<td>')
                .text(value)
        )
    );
}

function formEdit(){
     $('#div-empresa').hide();
     $('#div-salida').hide();
     $('#div-fuente').hide();
     //$('#div-fecha_plan_init').hide();
     //$('#div-fecha_real_init').hide();
}

function createDetail(){
     $('#div-empresa').hide();
     $('#div-contacto').hide();
     $('#div-ejecutivo_principal').hide();
     $('#div-ejecutivo_primario').hide();
     $('#div-ejecutivo_secundario').hide();
     $('#div-salida').hide();
     $('#div-estimado').hide();
     $('#div-producto').hide();
     $('#div-plaza').hide();
     $('#div-salida').hide();
     $('#div-fuente').hide();
     //$('#div-comentarios').hide();
     //$('#div-fecha_real_init').hide();
// deshabilta todos
}


function createDetailOper(){
     $('#div-empresa').hide();
     $('#div-contacto').hide();
     $('#div-ejecutivo_principal').hide();
     $('#div-ejecutivo_primario').hide();
     $('#div-ejecutivo_secundario').hide();
     $('#div-salida').hide();
     $('#div-estimado').hide();
     $('#div-producto').hide();
     $('#div-plaza').hide();
     $('#div-salida').hide();
     $('#div-fuente').hide();
     $('#div-comentarios').hide();
    // $('#div-fecha_plan_init').hide();
// deshabilta todos
}