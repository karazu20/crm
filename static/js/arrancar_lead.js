/**
 * Created by Abraham on 30/05/2017.
 */
$( document ).ready(function() {
    $(this).scrollTop(0);
    $('#id_comentarios').val('');
    console.log( "Ready arrancar");
    $('#div-date').hide();
    date('Fecha real de inicio', 'init');
    createDetail();
});