$(document).ready(function() {
	var tool = "Pencil";
	var $canvas = $("#drawingSurface");
	var context = $canvas.get(0).getContext('2d');
	var drawing = false;
	var lastX, lastY;
	var canvX = $canvas.offset().left;
	var canvY = $canvas.offset().top;
	var color = "#000000";

	// your code here
	$('.swatch').each(function(){
		$(this).css("background-color",$(this).text()).empty();
	});
	
	$('.swatch').click(function(){
		color = $(this).css('background-color');
		context.strokeStyle = color;
		context.fillStyle = color;
	});
	
	var clear = function()
	{
		context.clearRect(0,0,$canvas.attr("width"),$canvas.attr("height"));		
	};

	$('.tool').click(function(evt){
		var t_old = tool;
		tool = $(this).text().trim();
		if( tool != "Clear" )
		{
			$('.tool').removeClass("selected");
			$(this).addClass("selected");
			console.log("select " + tool);
		}
		else
		{
			setTimeout(clear,300);
			$canvas.slideToggle(300).slideToggle(300);
			tool = t_old;
		}
		
	});

	function spray()
	{
		var ang,rad,px,py;
		for(var i=0; i<10; ++i)
		{
			ang = Math.random()*2*Math.PI;
			rad = Math.random()*20;
			px = lastX + rad*Math.cos(ang);
			py = lastY + rad*Math.sin(ang);
			context.fillRect(px-1,py-1,1,1);
		}
		if(drawing)
			setTimeout(spray,10);
	}

	$('#drawingSurface').mousedown(function(evt){
		drawing = true;
		lastX = evt.pageX - canvX;
		lastY = evt.pageY - canvY;
		if(drawing && tool=="Sprayer")
		{
			spray();
		}
		if( tool == "Brush" )
		{
			context.beginPath();
			context.arc(lastX,lastY,5,0,Math.PI*2);
			context.fill();	
		}
	}).mouseup(function(evt){
		drawing = false;
	}).mousemove(function(evt){
		if(drawing)
		{
			var cx = evt.pageX - canvX;
			var cy = evt.pageY - canvY;
			switch(tool)
			{
				case "Pencil":
					context.lineWidth = 1;
					context.beginPath();
					context.moveTo(lastX,lastY);
					context.lineTo(cx,cy);
					context.stroke();
				break;
				case "Brush":
				{	
					var dx = cx-lastX;
					var dy = cy-lastY;
					var px = lastX;
					var py = lastY;
					var steps = Math.floor(Math.sqrt(dx*dx+dy*dy));
					dx /= steps;
					dy /= steps;
					for(var i=0; i<steps; ++i)
					{
						context.beginPath();
						context.arc(px,py,5,0,Math.PI*2);
						context.fill();	
						px += dx;
						py += dy;
					}
				}
				break;
			}
			lastX = cx;
			lastY = cy;
		}
	}).mouseenter(function(evt){
		lastX = evt.pageX - canvX;
		lastY = evt.pageY - canvY;
	});
	

});