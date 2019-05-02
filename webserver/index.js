const path = require('path');
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);
const axios = require('axios');
const FPS= 25;
const net = require('net')
const stream = require("socket.io-client").connect('http://localhost:5000/');

async function getJSONAsync(action){
    return await axios.get('http://localhost:5000/'+ action);
}

app.use(express.static(path.join(__dirname, 'static')));

app.get('/', (req, res) => {
    res.sendFile('index.html');
})

io.on('connection',function(socket){

    setInterval(()=> {
	stream.emit("image", function(data){
	    io.emit('image', data);
	});  	
    }, 1000 / FPS );

    
    socket.on('foward', function(){
	getJSONAsync('foward').then( function(result) {
	    console.log('moving to foward');
	});
    });

    socket.on('rigth', function(){
	getJSONAsync('rigth').then( function(result) {
	    console.log('moving to rigth');
	});
    });

    socket.on('left', function(){
	getJSONAsync('left').then( function(result) {
	    console.log('moving to left');
	});
    });

    socket.on('reverse', function(){
	getJSONAsync('left').then( function(result) {
	    console.log('moving to reverse');
	});
    });
});



server.listen(3000,'0.0.0.0', ()=>{
    console.log('App listening on port 3000!');
});
