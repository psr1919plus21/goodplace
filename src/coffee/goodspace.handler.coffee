$(document).ready ->
	$login = $(".modal-lodin")

	$(".header-login_link").on "click", (e)->
		e.preventDefault()
		$login.addClass "modal__active"

	$(".modal-close").on "click", (e)->
		e.preventDefault()
		$(this).closest(".modal").removeClass "modal__active"

	$('div.prop-rating').rating()
	$('.bxslider').bxSlider({
 		 pagerCustom: '#bx-pager'
		})

	###
	Show Phone
	###
	$(".prop-content_phonebtn").on "click", ->
		$(this).hide()
		$(".prop-content_phonebtn-number, .prop-content_phonetip").fadeIn()

		