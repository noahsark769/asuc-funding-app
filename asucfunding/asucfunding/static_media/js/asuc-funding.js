$(document).ready(function() {

	// helper function to get numbers from IDs
	function extractNumber(id) {
		return parseInt(/\d+/.exec(id));
	}

	/* we're using FORMS because of CSRF simplicity
	we can now just use {% csrf_token %} in config.html, which avoids auth problems. */
	$('button.config_submit').click(function(event) {
		event.preventDefault();
		// console.log('submit fired');
		// get the button that was used to submit the form (see .click() below)
		$currentButton = $(this);
		// console.log($currentButton);

		// name of the table we're inserting into
		var config_key = $currentButton.closest('div').prop('id');

		var options = {};
		options['config_key'] = config_key;
		var $sibs = $currentButton.siblings('input');

		// we will name each consecutive input value0, value1, etc.
		var count = 1;
		$.each($sibs, function() {
			options['value' + count++] = $(this).val();

			// reset text box
			$(this).val('');
		});

		if (!$(this).closest('div').find('input').valid())
			return false;

		$.post('/update_config/', options, function(data) {
			if (data === 'FAILURE') {
				console.log("Failed to insert new data into list " + config_key);
				return;
			}
			$(data).insertBefore($currentButton.parent());
		});

		// just so that we don't go anywhere...
		return false;
	});

	//submit the form if enter was pressed
	$('form#config_form input').keypress(function(event){
		// console.log('key pressed');
		if (event.keyCode === 13) {
			event.preventDefault();
			$(this).siblings('.config_submit').click();
		}
	});

	// handles requests to remove objects
	$(document).on('click', 'a.config_remove', function() {
		// confirm...
		if (!window.confirm(this.title || 'Are you sure you wish to delete this?')) {
			return false;
		}

		$item = $(this).parent();

		// id of the parent <li>, which determines the id # of the item
		var parentID = extractNumber($item.prop('id'));
		// now we need to know which list we're in
		var config_key = $item.closest('div').prop('id');

		var options = {};
		options['id'] = parentID;
		options['remove'] = 1;
		options['config_key'] = config_key;

		$.post('/update_config/', options, function(data) {
			if (data === 'FAILURE') {
				console.log("Failed to remove item " + parentID + " from " + config_key);
				alert("Failed to remove item " + parentID + " from " + config_key + '.');
				return;
			}
			// get rid of it.
			$item.remove();
		});

		// just so that we don't go anywhere...
		return false;
	});

});
