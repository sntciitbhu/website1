$(function() {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 65)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 65
    })

$("header").bgswitcher({
  images: ["/static/clubs/csi/img/header.jpg", "/static/clubs/csi/img/header2.jpg", "/static/clubs/csi/img/header3.jpg", "/static/clubs/csi/img/header4.jpg", "/static/clubs/csi/img/header5.jpg", "/static/clubs/csi/img/header6.jpg"],
  effect: "fade",
  interval: 4000,
  duration: 1000
});
$('#clubs').hover(function() {
  $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideDown();
}, function() {
  $(this).find('.dropdown-menu').first().stop(true, true).delay(80).slideUp();
});


 // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    });

 // Initialize WOW.js Scrolling Animations
    new WOW().init();
});
