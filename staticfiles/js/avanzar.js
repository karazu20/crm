/**
 * Created by Abraham on 24/05/2017.
 */
var estatus = parseInt($("#estatus").val());
$( document ).ready(function() {
	$(this).scrollTop(0);
    $('#id_comentarios').val('');
	console.log( "Ready avanzar");
    $('#div-date').hide();
	switch (estatus) {
        case 1: $('#submit_button').val('Avanzar a LC');
                formEdit();
                addTD ('#header_lead', 'Etapa: LNC --> LC');
                break;//LNC --> LC
        case 2: $('#submit_button').val('Avanzar a OP');
                formEdit();
                addTD ('#header_lead', 'Etapa: LC --> OP');
                break;//LC --> OP
        case 3: $('#submit_button').val('Avanzar a NEG');
                formEdit();
                addTD ('#header_lead', 'Etapa: OP --> NEG');
                break;//OP --> NEG
        case 4: $('#submit_button').val('Avanzar a CIE');
                 formEdit();
                 //$('#div-date').show();
                 date('Fecha planeada de inicio', 'init');
                 //addFecha('#lead_form', 'Fecha de inicio', 'fecha_init');
                addTD ('#header_lead', 'Etapa: NEG --> CIE');
                break;//NEG --> CIE
        //case 4: $('#nextButton').val('Avanzar a OPER');
        //        createDetailOper ();
        //        break;//NEG --> CIE
        default:
            console.log(" Estatus invalido");//

    }


});
