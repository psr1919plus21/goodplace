(function() {
  $(document).ready(function() {
    var $login;
    $login = $(".modal-lodin");
    $(".header-login_link").on("click", function(e) {
      e.preventDefault();
      return $login.addClass("modal__active");
    });
    $(".modal-close").on("click", function(e) {
      e.preventDefault();
      return $(this).closest(".modal").removeClass("modal__active");
    });
    $('div.prop-rating').rating();
    $('.bxslider').bxSlider({
      pagerCustom: '#bx-pager'
    });

    /*
    	Show Phone
     */
    return $(".prop-content_phonebtn").on("click", function() {
      $(this).hide();
      return $(".prop-content_phonebtn-number, .prop-content_phonetip").fadeIn();
    });
  });

}).call(this);
