const cv = require("opencv4nodejs");
const path = require('path');
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);
const axios = require('axios');
const wCap = new cv.VideoCapture(0);
const FPS=30;


async function getJSONAsync(action){
    return await axios.get('http://localhost:5000/'+ action);
}

app.use(express.static(path.join(__dirname, 'static')));

app.get('/', (req, res) => {
    res.sendFile('index.html');
})

io.on('connection',function(socket){

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

setInterval(()=> {
  	const frame = wCap.read();
	const image = cv.imencode('.jpg', frame).toString('base64');
  	io.emit('image', image);
    }, 1000 / FPS );

server.listen(3000,'0.0.0.0', ()=>{
    console.log('App listening on port 3000!');
});
