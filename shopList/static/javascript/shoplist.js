
Socket = io.connect();//create new websocket, 
Socket.on('message', function(msg) {
			loading();
			var JSONdata = JSON.parse(msg);
			/*
			https://api.jquery.com/jquery.parsehtml/
			*/
			if (JSONdata.ingrd){
				console.log(JSONdata.ingrd)
				};
			for (var i=0; i <JSONdata.ingrd.length;i++){
				$('#shoplist').append('<p>'+JSONdata.ingrd[i]+'</p>');}
});

function loading(){
	$("#loading").toggle();
}

function getRecipe(url){
	
	/*
	send URL to server,
	server does get request then parses data
	returns ingredients as json
	*/
	Socket.send(JSON.stringify({'url':url}));
	loading();
	
	
	/*cant do $.get because of CORS*/
	/*$.get(url,function(data,status){
		console.log(data);
	});*/
	
}




$(document).ready(function(){
	loading();
	$('#submitRecipeURL').click( function() {
		var recipeURL = $('#recipeURL').val();
		getRecipe(recipeURL);
	});
});