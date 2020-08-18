$(function() {
	console.log("whee!")

	// event handler
	$("#btn-click").click(function() {
		if ($("input").val() !== "") {
			var input = $("input").val()
			console.log(input)
			// add the value to the DOM
			$('ol').append('<li><a href="">x</a> - ' + input + '</li>');
		}
		$('input').val('');
	});
	
});

$(document).on('click', 'a', function (event) {
	event.preventDefault();
	$(this).parent().remove();
});