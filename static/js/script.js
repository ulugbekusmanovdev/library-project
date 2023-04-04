"use strict";
(function () {

    $(".books_slick-slider").slick({
        pauseOnHover: false,
        pauseOnFocus: false,
        // autoplay:true,
        autoplaySpeed: 4000,
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 4,
        arrows: true,
        responsive: [
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 3,
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 2,
              }
            }
          ]
    })

})(jQuery)

"use strict";
(function () {

    $(".photo_slick-slider").slick({
        pauseOnHover: false,
        pauseOnFocus: false,
        // autoplay:true,
        autoplaySpeed: 4000,
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        arrows: true,
    })

})(jQuery)

"use strict";
(function () {

    $(".news_slick-slider").slick({
        pauseOnHover: false,
        pauseOnFocus: false,
        // autoplay:true,
        autoplaySpeed: 4000,
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        arrows: true,
    })

})(jQuery)