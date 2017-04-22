function loadHome(){
    $(".content").fadeOut(500,function(){
	$.get("home",function(data){
	    $(".content").html(data);
	    $(".content").fadeIn(500);
	});
    });
}


function loadAbout(){
    $(".title").fadeOut(100);
    $(".content").fadeOut(500,function(){
	$.get("about",function(data){
	    $(".content").html(data);
	    $(".content").fadeIn(500);
	});
    });

}


function goGit(){
    window.open("http://github.com/MrSusanovo");
}

function goLinkedIn(){
    window.open("http://www.linkedin.com/in/%E7%A7%89%E6%AD%A3-%E5%86%AF-b0096ab0/");
}

function goIntro(){
    window.location.replace("http://mrsusanovo.com/intro");
}

$(document).ready(function(){

    $("#menutag-About").on("click",function(){
	loadAbout();
    });
    
    $("#menutag-Home").on("click",function(){
	loadHome();
    });
    
    $("#menutag-Intro").on("click",function(){
	goIntro();
    });
    
    $("#menutag-GitHub").on("click",function(){
	goGit();
    });
    
    $(".content").on("click","#mondsq0",function(){
	goGit();
    });

    $(".content").on("mouseenter","#mondsq0",function(){
	var display = $(".content").find("#mondsq7");
	var mess = $(".content").find("#mondsq0").find(".store").html();
	display.find(".static").fadeOut(300,function(){
	    display.find(".dynamic").html(mess);
	    display.find(".dynamic").fadeIn(300);
	});
    });

    $(".content").on("mouseleave","#mondsq0",function(){
	var display = $('.content').find("#mondsq7");
	display.find(".dynamic").fadeOut(300,function(){
	    display.find(".dynamic").html("");
	    display.find(".static").fadeIn(300);
	});
    });

    $(".content").on("click","#mondsq1",function(){
	goIntro();
    });

    $(".content").on("mouseenter","#mondsq1",function(){
	var display = $(".content").find("#mondsq7");
	var mess = $(".content").find("#mondsq1").find(".store").html();
	display.find(".static").fadeOut(300,function(){
	    display.find(".dynamic").html(mess);
	    display.find(".dynamic").fadeIn(300);
	});
    });

    $(".content").on("mouseleave","#mondsq1",function(){
	var display = $('.content').find("#mondsq7");
	display.find(".dynamic").fadeOut(300,function(){
	    display.find(".dynamic").html("");
	    display.find(".static").fadeIn(300);
	});
    });

    $(".content").on("click","#mondsq2",function(){
	goLinkedIn();
    });

    $(".content").on("mouseenter","#mondsq2",function(){
	var display = $(".content").find("#mondsq7");
	var mess = $(".content").find("#mondsq2").find(".store").html();
	display.find(".static").fadeOut(300,function(){
	    display.find(".dynamic").html(mess);
	    display.find(".dynamic").fadeIn(300);
	});
    });

    $(".content").on("mouseleave","#mondsq2",function(){
	var display = $('.content').find("#mondsq7");
	display.find(".dynamic").fadeOut(300,function(){
	    display.find(".dynamic").html("");
	    display.find(".static").fadeIn(300);
	});
    });
    
    
    $(".content").on("click","#mondsq6",function(){
	loadAbout();
    });

    $(".content").on("mouseenter","#mondsq6",function(){
	var display = $('.content').find("#mondsq7");
	var mess = $(".content").find("#mondsq6").find(".store").html();
	display.find(".static").fadeOut(300,function(){
	    display.find(".dynamic").html(mess);
	    display.find(".dynamic").fadeIn(400);
	});
    });
    $(".content").on("mouseleave","#mondsq6",function(){
	var display = $(".content").find("#mondsq7");
	display.find(".dynamic").fadeOut(300,function(){
	    display.find(".static").fadeIn(400)
	});
    });
});
