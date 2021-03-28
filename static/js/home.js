    $(document).ready(function(){
        $('.homepage-banner').slick({
            infinite: true,
            speed: 2000,
            dots: true,
            vertical: true,
            autoplay: true,
            slidesToShow: 1,
            arrows: false,
            adaptiveHeight: true,
            focusOnSelect: true,
            lazyLoad :true,
            autoplaySpeed: 7000
            });
    });