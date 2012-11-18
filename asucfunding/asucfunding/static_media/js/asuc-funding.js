$(document).ready(function() {
	
	$('button.config_submit').click(function() {
		console.log('fuck!');

		$currentButton = $(this);

		var options = {};
		var config_key = $currentButton.parent().parent().parent().prop('id');
		console.log(config_key);
		options['config_key'] = config_key;
		var $sibs = $currentButton.siblings('input');
		$.each($sibs, function() {
			options[$(this).prop('id')] = $(this).val();
			$(this).val('');
		});

		console.log(options);
		$.post('/update_config/', options, function(data) {
			if (data === 'FAILURE') {
				return;
			}
			console.log(data);
			console.log($currentButton);
			console.log($currentButton.parent());
			// $currentButton.parent().append(data);
			$(data).insertBefore($currentButton.parent());
		});
	});

});