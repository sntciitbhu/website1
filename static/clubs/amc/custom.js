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
  images: ["/static/clubs/amc/img/header.jpg", "/static/clubs/amc/img/header2.jpg", "/static/clubs/amc/img/header3.jpg", "/static/clubs/amc/img/header4.jpg", "/static/clubs/amc/img/header5.jpg", "/static/clubs/amc/img/header6.jpg"],
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


/*Interactivity to determine when an animated element in in view. In view elements trigger our animation*/
$(document).ready(function() {

  //window and animation items
  var animation_elements = $.find('.animation-element');
  var web_window = $(window);

  //check to see if any animation containers are currently in view
  function check_if_in_view() {
    //get current window information
    var window_height = web_window.height();
    var window_top_position = web_window.scrollTop();
    var window_bottom_position = (window_top_position + window_height);

    //iterate through elements to see if its in view
    $.each(animation_elements, function() {

      //get the element sinformation
      var element = $(this);
      var element_height = $(element).outerHeight();
      var element_top_position = $(element).offset().top;
      var element_bottom_position = (element_top_position + element_height);

      //check to see if this current container is visible (its viewable if it exists between the viewable space of the viewport)
      if ((element_bottom_position >= window_top_position) && (element_top_position <= window_bottom_position)) {
        element.addClass('in-view');
      } else {
        element.removeClass('in-view');
      }
    });

  }

  //on or scroll, detect elements in view
  $(window).on('scroll resize', function() {
      check_if_in_view()
    })
    //trigger our scroll event on initial load
  $(window).trigger('scroll');

});