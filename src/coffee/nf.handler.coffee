$(document).ready ->
	$login = $(".modal-lodin")

	$(".header-login_link").on "click", (e)->
		e.preventDefault()
		$login.addClass "modal__active"

	$(".modal-close").on "click", (e)->
		e.preventDefault()
		$(this).closest(".modal").removeClass "modal__active"
		