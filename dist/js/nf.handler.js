(function() {
  $(document).ready(function() {
    var $login;
    $login = $(".modal-lodin");
    $(".header-login_link").on("click", function(e) {
      e.preventDefault();
      return $login.addClass("modal__active");
    });
    return $(".modal-close").on("click", function(e) {
      e.preventDefault();
      return $(this).closest(".modal").removeClass("modal__active");
    });
  });

}).call(this);
