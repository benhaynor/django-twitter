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
	var userzone = $("#userzone");
	userzone.append('<div class="user">' + "I could be a list of users" + '!</div>');
}

$(function(){
	$("#tweetGetter").click(getTweets);
	$("#tweetPoster").click(postTweet);
	$("#userGetter").click(getUsers);
});
