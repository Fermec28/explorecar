console.log('Hola Mundo')
/*
  Plantar el evento del teclado
  leer sobre promises
  usar wait sobre promises para enviar la peticion ajax
  url/car/foward
  url/car/right
  url/car/left
  url/car/reverse
  Seria genial usar JWT para que las solicitudes sean aceptadas
  solo por este servidor
*/
const URI = 'http:192.168.1.9:3001'

ajaxCall = function(action){
    $.ajax({
        url: URI+'/'+ action,
        type: 'GET',
        async: false,
        cache: false,
        timeout: 300,
        error: function(){
            return true;
        },
        success: function(msg){
            console.log(msg)
        }
    });

$(document).ready(function(){
    $(document).keydown(function(e) {
    switch(e.which) {
        case 37: // left
	console.log('left');
	ajaxCall('left');
	break;

        case 38: // up
	console.log('foward');
	ajaxCall('foward');
	break;

        case 39: // right
	console.log('rigth');
	ajaxCall('rigth');
	break;

        case 40: // down
	console.log('reverse');
	ajaxCall('reverse');
	break;

        default: return; // exit this handler for other keys
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
    });
})
