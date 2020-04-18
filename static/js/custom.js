/* ---------------------------------------------
 javaScript Document
 --------------------------------------------- */
$(document).ready(function() {
    "use strict";

    /* ---------------------------------------------
     Carousel Slider
     --------------------------------------------- */

    var owl = $("#news-feed-carousel");
    owl.owlCarousel({
        autoPlay: 5000, //Set AutoPlay to 5 seconds
        navigation: false,
        singleItem: true,
        transitionStyle: "fade"
    });

    $("#content-slide").owlCarousel({
        //autoPlay: 5000, Set AutoPlay to 5 seconds
        items: 2,
        itemsDesktop: [1199, 2],
        itemsDesktopSmall: [980, 2],
        itemsTablet: [768, 2],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: true,
        navigationText: [
            "<i class='fa pe-7s-angle-left'></i>",
            "<i class='fa pe-7s-angle-right'></i>"
        ],
        afterInit: function(elem) {
            var that = this;
            that.owlControls.prependTo(elem);
        }
    });

    $("#content-slide-2").owlCarousel({
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: true,
        navigationText: [
            "<i class='fa pe-7s-angle-left'></i>",
            "<i class='fa pe-7s-angle-right'></i>"
        ],
        afterInit: function(elem) {
            var that = this;
            that.owlControls.prependTo(elem);
        }
    });

    $("#content-slide-3").owlCarousel({
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: true,
        navigationText: [
            "<i class='fa pe-7s-angle-left'></i>",
            "<i class='fa pe-7s-angle-right'></i>"
        ],
        afterInit: function(elem) {
            var that = this;
            that.owlControls.prependTo(elem);
        }
    });

    $("#content-slide-4").owlCarousel({
        autoPlay: 3000, //Set AutoPlay to 3 seconds
        items: 4,
        itemsDesktop: [1199, 4],
        itemsDesktopSmall: [980, 3],
        itemsTablet: [768, 3],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: false
    });

    $("#content-slide-5").owlCarousel({
        //autoPlay: 5000, Set AutoPlay to 5 seconds
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: true,
        navigationText: [
            "<i class='fa pe-7s-angle-left'></i>",
            "<i class='fa pe-7s-angle-right'></i>"
        ],
        afterInit: function(elem) {
            var that = this;
            that.owlControls.prependTo(elem);
        }
    });
    $("#content-slide-6").owlCarousel({
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: true,
        navigationText: [
            "<i class='fa pe-7s-angle-left'></i>",
            "<i class='fa pe-7s-angle-right'></i>"
        ],
        afterInit: function(elem) {
            var that = this;
            that.owlControls.prependTo(elem);
        }
    });

    $("#content-slide-7").owlCarousel({
        //autoPlay: 5000, Set AutoPlay to 5 seconds
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: true,
        navigationText: [
            "<i class='fa pe-7s-angle-left'></i>",
            "<i class='fa pe-7s-angle-right'></i>"
        ],
        afterInit: function(elem) {
            var that = this;
            that.owlControls.prependTo(elem);
        }
    });

    $("#video-slide").owlCarousel({
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsTabletSmall: false,
        itemsMobile: [479, 1],
        pagination: false,
        dots: false,
        lazyLoad: true,
        navigation: true,
        navigationText: [
            "<i class='fa pe-7s-angle-left left'></i>",
            "<i class='fa pe-7s-angle-right right'></i>"
        ],
        afterInit: function(elem) {
            var that = this;
            that.owlControls.prependTo(elem);
        }
    });

    var owl = $("#widget-slider");
    owl.owlCarousel({
        autoPlay: 5000, //Set AutoPlay to 5 seconds
        navigation: false,
        singleItem: true,
        transitionStyle: "fade"
    });

    /* ---------------------------------------------
     Video Effect
     --------------------------------------------- */

    $(".post-thumb").mouseenter(function() {
            $(this).addClass("hover");
        })
        // handle the mouseleave functionality
        .mouseleave(function() {
            $(this).removeClass("hover");
        });

    $(".img-thumb").mouseenter(function() {
            $(this).addClass("hover");
        })
        // handle the mouseleave functionality
        .mouseleave(function() {
            $(this).removeClass("hover");
        });
    /* ---------------------------------------------
     Scroll to Top Button it is called for scrolling down to top at html
     --------------------------------------------- */
    $('body').append('<div id="toTop" class="btn btn-info"><span class="fa fa-dot-circle-o top"></span><br>TOP</div>');


    $('#toTop').on('click', function() {
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });


    /* ---------------------------------------------
     Side Menu
    --------------------------------------------- */
    $('.side-menu').metisMenu();



    /* ---------------------------------------------
      Pre loader loader 
     --------------------------------------------- */

    $(".se-pre-con").fadeOut("slow");


    
    
    
    
    
    
    
    
    /* ---------------------------------------------
     newstricker
     --------------------------------------------- */
    $('.newsticker').newsTicker({
        row_height: 12,
        max_rows: 2,
        speed: 600,
        direction: 'up',
        duration: 4000,
        autostart: 1,
        pauseOnHover: 0,
        prevButton: $('#prev-button'),
        nextButton: $('#next-button'),
        stopButton: $('#stop-button'),
        startButton: $('#start-button')
    });


    /* ---------------------------------------------
     Tab
     --------------------------------------------- */

    $('.tab-inner ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
    $('.tab-inner ul.tabs li a').on('click', function(g) {
        var tab = $(this).closest('.tab-inner'),
            index = $(this).closest('li').index();

        tab.find('ul.tabs > li').removeClass('current');
        $(this).closest('li').addClass('current');

        tab.find('.tab_content').find('div.tab-item-inner').not('div.tab-item-inner:eq(' + index + ')').slideUp();
        tab.find('.tab_content').find('div.tab-item-inner:eq(' + index + ')').slideDown();

        g.preventDefault();
    });



    /* ---------------------------------------------
     Date picker  
     --------------------------------------------- */

    $("#from").datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3,
        onClose: function(selectedDate) {
            $("#to").datepicker("option", "minDate", selectedDate);
        }
    });
    $("#to").datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3,
        onClose: function(selectedDate) {
            $("#from").datepicker("option", "maxDate", selectedDate);
        }
    });




    /* ---------------------------------------------
     Youtube Video
     --------------------------------------------- */
    var api_key = 'AIzaSyAroKpLQWTON6y34m5VqGcLCPtOmfLBqh4'; // use your own api key

    // Start all players on the page with default options
    $('.RYPP').rypp('AIzaSyAroKpLQWTON6y34m5VqGcLCPtOmfLBqh4'); // use your own api key

    // Start two players by ID, with default settings
    $('#rypp-demo-4').rypp(api_key, {
        autoplay: false,
        autonext: false,
        loop: false,
        mute: true
    });

    /* ---------------------------------------------
     Youtube Video for home page four
     --------------------------------------------- */

    $(".arrow-right").bind("click", function(event) {
        event.preventDefault();
        $(".vid-list-container").stop().animate({
            scrollLeft: "+=336"
        }, 750);
    });
    $(".arrow-left").bind("click", function(event) {
        event.preventDefault();
        $(".vid-list-container").stop().animate({
            scrollLeft: "-=336"
        }, 750);
    });

    /* ---------------------------------------------
       youtube video for home page five
       --------------------------------------------- */

    $('#player-button').on('click', function(ev) {

        $("#yt")[0].src += "?autoplay=1";
        $("#player").hide();
        $("#post-info").hide();
        ev.preventDefault();
    });


    /* ---------------------------------------------
     tricker animation for home page four
     --------------------------------------------- */


    function tick() {
        $('#ticker li:first').animate({ 'opacity': 0 }, 400, function() {
            $(this).appendTo($('#ticker')).css('opacity', 1);
        });
    }
    setInterval(function() { tick() }, 3000);

    /* ---------------------------------------------
     Form 
     --------------------------------------------- */

    if (!String.prototype.trim) {
        (function() {
            // Make sure we trim BOM and NBSP
            var rtrim = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;
            String.prototype.trim = function() {
                return this.replace(rtrim, '');
            };
        })();
    }
    [].slice.call(document.querySelectorAll('input.input_field,textarea.input_field')).forEach(function(inputEl) {
        // in case the input is already filled..
        if (inputEl.value.trim() !== '') {
            classie.add(inputEl.parentNode, 'input--filled');
        }
        // events:
        inputEl.addEventListener('focus', onInputFocus);
        inputEl.addEventListener('blur', onInputBlur);
    });

    function onInputFocus(ev) {
        classie.add(ev.target.parentNode, 'input--filled');
    }

    function onInputBlur(ev) {
        if (ev.target.value.trim() === '') {
            classie.remove(ev.target.parentNode, 'input--filled');
        }
    }

});




$(window).on({
    load: function() {

        /* ---------------------------------------------
          Scroll Box 
         --------------------------------------------- */

        $(".mobile-menu").mCustomScrollbar({ theme: "minimal" });
        $(".archive-post").mCustomScrollbar({ theme: "minimal-dark" });


    },

    scroll: function() {

        /* ---------------------------------------------
        Scroll to Top 
        --------------------------------------------- */

        if ($(this).scrollTop() !== 0) {
            $('#toTop').fadeIn();
        } else {
            $('#toTop').fadeOut();
        }
    }

});



/* ---------------------------------------------
 This is for Mobile Menu
 --------------------------------------------- */

//Nav Icon at mobile 
$('.nav-icon').on('click', function() {
    $(this).toggleClass('open');
});

//mobile Menu showLeft at mobile
var menuLeft = document.getElementById('mobile-menu'),
    showLeft = document.getElementById('showLeft'),
    body = document.body;
var classie;
showLeft.onclick = function() {
    classie.toggle(this, 'active');
    classie.toggle(menuLeft, 'mobile-menu-open');
    disableOther('showLeft');
};

function disableOther(button) {
    if (button !== 'showLeft') {
        classie.toggle(showLeft, 'disabled');
    }
}
