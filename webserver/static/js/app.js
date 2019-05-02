console.log('Hola Mundo')

$(document).ready(function(){
    $(document).keydown(function(e) {
    switch(e.which) {
        case 37: // left
	console.log('left');
	socket.emit('left')
	break;

        case 38: // up
	console.log('foward');
	socket.emit('foward');
	break;

        case 39: // right
	console.log('rigth');
	socket.emit('rigth');
	break;

        case 40: // down
	console.log('reverse');
	socket.emit('reverse');
	break;

        default: return; // exit this handler for other keys
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
    });
})
