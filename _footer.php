 
	<footer class="l-footer">
		<div class="l-restrictor">
			<div><a href="email:psr1919plus21@gmail.com" class="footer-author">psr1919plus21@gmail.com</a></div>
			<div class="footer-year">2015</div>	
		</div>
	</footer>
	<script src="http://api-maps.yandex.ru/2.0/?load=package.full&lang=ru-RU" type="text/javascript"></script>
	<script src="bower_components/jquery/dist/jquery.js"></script>
	<script src="dist/js/jquery.bxslider.js"></script>
	<script src="dist/js/jquery.rating.js"></script>
	<script src="dist/js/goodspace.handler.js"></script>
	<script type="text/javascript">
		
		$.get( "http://geocode-maps.yandex.ru/1.x/?geocode=Евпатория+Полупанова+40", function( data ) {
			mapLabel = $(data).find("pos")[0].textContent.split(" ");
			console.log($(data));
			
			var myMap;
		 	ymaps.ready(init); // Ожидание загрузки API с сервера Яндекса
		 	
		  	function init () {
		  		console.log(mapCenter);
		    	myMap = new ymaps.Map("map", {
			      center: mapLabel.reverse(), // Координаты центра карты
			      zoom:16 // Zoom
		    	});
		  	}
		});

	  
	</script>
 </body>
</html>