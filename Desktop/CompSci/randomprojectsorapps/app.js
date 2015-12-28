//require express, initialize into variable named app. 
//use bodyParser middleware to make it easier to use data we'll be getting in our POST request
var express = require('express'),
bodyParser = require('body-parser'),
app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: true
}));

var twilio = require('twilio'),
client = twilio('AC358a60437a112c5c59d3b52da1f0dcc7', 'e7ae1b711f733bae6c2647bd62154b77'),
cronJob = require('cron').CronJob;


//send to multiple numbers
var numbers = ['6507141188', '6103068360', '6502006162', '8453259986'];
var textJob = new cronJob('5 18 * * *', function(){
	for(var i = 0; i < numbers.length; i++) {
	client.sendMessage( { to:numbers[i], from:'6698004068', body:'Hello! Hope you’re having a good day.'}, function( err, data ) {
    console.log( data.body );
    });
}

//add route for /message that responds w/ some TwiML (set of instructions to tell Twilio 
	//what to do when receiving incoming message)
var server = app.listen(3000, function() {
	console.log('Listening on port %d', server.address().port);
});

app.post('/message', function (req, res) {
	var resp = new twilio.TwimlResponse();
	resp.message('Thanks for listening now message Lizzie at 6507878004 to confirm you got the message');
	res.writeHead(200, {
		'Content-Type':'text/xml'
	});
	res.end(resp.toString());
});

});






