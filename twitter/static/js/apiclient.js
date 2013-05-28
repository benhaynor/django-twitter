function getTweets(){ 
	$.getJSON('/api/users/' + userid + '/tweets', function(data){
		var tweetzone = $("#tweetzone");
		for(i = 0; i < data.length; i ++){
			window.console.log(data[i]);
			window.console.log(data[i].text);
			tweetzone.append('<div class="tweet">' + data[i].text + '!</div>');
		}
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


$(function(){
	$("#tweetGetter").click(getTweets);
	$("#tweetPoster").click(postTweet);
});
