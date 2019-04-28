const cv = require("opencv4nodejs");
const path = require('path');
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);
const wCap = new cv.VideoCapture(0);
const FPS=30;

app.use(express.static(path.join(__dirname, 'static')));

app.get('/', (req, res) => {
    res.sendFile('index.html');
})

setInterval(()=> {
  	const frame = wCap.read();
	const image = cv.imencode('.jpg', frame).toString('base64');
  	io.emit('image', image);
}, 1000 / FPS );

server.listen(3000,'0.0.0.0', ()=>{
    console.log('App listening on port 3000!');
});
