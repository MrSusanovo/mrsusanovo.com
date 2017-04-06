$(document).ready(function(){
    $("#menutag-About").on("click",function(){
	console.log("about clicked");
	$.get("about",function(data){
	    $(".title").css("display","none");
	    $(".content").fadeOut(100,function(){
		$(".content").html(data);
	    });
	    $(".content").fadeIn(1000);
	});
    });

    $("#menutag-Home").on("click",function(){
	console.log("home clicked");
	$.get("home",function(data){
	    $(".content").fadeOut(500,function(){
		$(".content").html(data);
	    }).delay(200).fadeIn(500);
	});
    });

    $("#menutag-Intro").on("click",function(){
	window.location.replace("intro");
    });
    
    $("#menutag-GitHub").on("click",function(){
	window.open("http://github.com/MrSusanovo");
    });
});

    
