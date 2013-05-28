function getTweets(){ 
	$.getJSON('/api/users/' + userid + '/tweets', function(data){
		var tweetzone = $("#tweetzone");
		for(i = 0; i < data.length; i ++){
			tweetzone.append('<div class="tweet">' + data[i].text + '!</div>');
		};
	});
}

function postTweet(){
	text = $("#tweetText")[0].value;
	$.ajax({
		type: 'POST',
		url : '/api/users/' + userid + '/tweets',
		data : {author:userid, text:text}
	});
}

function getUsers(){
	var userzone = $("#userGetter");
	$.getJSON('/api/users/', function(data){
		for (i in data){
			window.console.log(data[i]);
			userzone.append('<div class="user">' + data[i].username + '!</div>');
		}	
	})
}

$(function(){
	$("#tweetGetter").click(getTweets);
	$("#tweetPoster").click(postTweet);
	$("#userGetter").click(getUsers);
});
