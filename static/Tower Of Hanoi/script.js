// Constants
var INIT_POST = 1;
var FINAL_POST = 3;
var NUM_DISCS = 9;
var EMPTY_POST_TEXT = 'The selected post does not have any discs '+
						'on it.';
var INVALID_MOVE_HEADER = 'You cannot move this disc onto post ';
var INVALID_MOVE_FOOTER = ', because the top disc is too small!';
var GAME_COMPLETE_TEXT = 'Congratulations! You won!\n\n'+
						'Would you like to play again?';
// "Class" variables
var posts = [];
posts[0] = [];
posts[1] = [];
posts[2] = [];
var selection = 0;

$(document).ready(function(){
	if (NUM_DISCS > 9) { // Game does not work w/ more than 9 discs
		NUM_DISCS = 9;
	}else if(NUM_DISCS < 1){
		NUM_DISCS = 1;
	}
	createDiscs();
	$(document).keyup(function(event){
		var post_num = event.which-48;
		if (post_num < 1 || post_num > 3){ // Only accept valid keys
			return;
		}
		var post, disc_num, $disc_to_move;
		var finished = false;
		if (selection === 0){ // Initial selection
			if(isPostEmpty(post_num)){
				errorLog(EMPTY_POST_TEXT);
			}else{
				post = posts[post_num-1];
				disc_num = post[post.length-1];
				$disc_to_move = $('.disc_'+disc_num);
				$disc_to_move.addClass('selected');
				selection = post_num;
				errorLog();
			}
			return;
		}else{
			post = posts[selection-1];
			disc_num = post[post.length-1];
			$disc_to_move = $('.disc_'+disc_num);
			if(selection !== post_num){ // Move disc
				if(isValidMove(disc_num,post_num)){ 
					posts[post_num-1].push(post.pop());
					$disc_to_move = changeLevel($disc_to_move,post,
						posts[post_num-1]);
					$('#post_'+post_num).append($disc_to_move);
					finished = isPostFull(FINAL_POST);
					errorLog();
				}else{
					errorLog(INVALID_MOVE_HEADER+post_num+
						INVALID_MOVE_FOOTER);
				}
			}else{
				errorLog();
			}
			$disc_to_move.removeClass('selected');
			selection = 0;
			if (finished){
				if (confirm(GAME_COMPLETE_TEXT)){
					resetDiscs();
				}else{
					$(document).unbind('keyup');
				}
			}
		}
	});
});

function createDiscs(){
	var $post = $('#post_'+INIT_POST);
	for(var index=NUM_DISCS; index>=1; index--){
		posts[INIT_POST-1].push(index);
		$('<div />').addClass('disc disc_'+index+' level_'+
			(NUM_DISCS-index+1)).appendTo($post);
	}
}

function isValidMove(disc_num,post_num){
	var post = posts[post_num-1];
	return isPostEmpty(post_num) || disc_num < post[post.length-1];
}

function isPostEmpty(post_num){
	return !posts[post_num-1].length;
}

function isPostFull(post_num){
	var post = posts[post_num-1];
	for (var index=0; index<post.length; index++){
		if(post[index] !== NUM_DISCS-index){
			return false;
		}
	}
	return post.length === NUM_DISCS;
}

function changeLevel($disc,oldPost,newPost){
	return $disc.removeClass('level_'+(oldPost.length+1)).
		addClass('level_'+newPost.length);
}

function resetDiscs(){
	posts[FINAL_POST-1] = [];
	var $post = $('#post_'+INIT_POST);
	$('#post_'+FINAL_POST).children('.disc').
		each(function(index,value){
		posts[INIT_POST-1].push(NUM_DISCS-index);
		$(value).appendTo($post);
	});
}

function errorLog(error_text){
	error_text = error_text || "";
	$('.error_msg').text(error_text);
}