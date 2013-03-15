$(function(){
	$("#new_tweet_box").keydown(function(event){
		if(event.keyCode == 13){
			var tweetText = $("#new_tweet_box").val();		
			$.ajax({
				type:'POST',
				url:'/tweets/new',
				data:{tweet:tweetText,user_id:$.cookie('user_id')}
			}).done(function(msg){
				alert('Data Saved :' + msg);
			});
		}
	});
});
