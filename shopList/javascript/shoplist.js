







function getRecipe(url){
	/*
	send URL to server,
	server does get request then parses data
	returns ingredients as json
	*/
	
	
	/*cant do $.get because of CORS*/
	/*$.get(url,function(data,status){
		console.log(data);
	});*/
	
}




$(document).ready(function(){
	$('#submitRecipeURL').click( function() {
		var recipeURL = $('#recipeURL').val();
		getRecipe(recipeURL);
	});
});