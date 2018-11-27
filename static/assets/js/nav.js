$(document).ready(function() {
  $(window).bind('scroll', function() {
    var navHeight = $('#headermain').height() + 400;
    if ($(window).scrollTop() > navHeight) {
      $('.nav-bar').addClass('fixed');
      $('.nav-1').addClass('toleft');
    } else {
      $('.nav-bar').removeClass('fixed');
      $('.nav-1').removeClass('toleft');
    }
  });
  $(".toggle").click(function() {
    $('.links').slideToggle();
  });
  $(window).resize(function() {
    if ($(window).width() > 768) {
      $('.links').show();
    } else {
      $('.links').hide();
    }
  });
});