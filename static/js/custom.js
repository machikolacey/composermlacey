$(document).ready(function(){

    $('.toast').toast('show');


    $(window).scroll(function() {
        if ($(this).scrollTop()) {
            $('#toTop').fadeIn();
        } else {
            $('#toTop').fadeOut();
        }
    });
    $("#toTop").click(function() {
        console.log('clicked');
        $("body, html").animate({scrollTop: 0}, 1000);
    });

 });