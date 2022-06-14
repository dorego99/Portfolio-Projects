/* This cretaes the movement of the webpage to switch to the registration or login page*/
$('.message a').click(function() {
  $('form').animate({
    height: "toggle",
    opacity: "toggle"
  }, "slow");
});
