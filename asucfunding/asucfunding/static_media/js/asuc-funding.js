$(document).ready(function() {
	
	/* we're using FORMS because of CSRF simplicity
	we can now just use {% csrf_token %} in config.html, which avoids auth problems. */
	$('form#config_form').submit(function() {
		// get the button that was used to submit the form (see .click() below)
		$currentButton = $('.config_submit[clicked=true]');

		// name of the table we're inserting into
		var config_key = $currentButton.parent().parent().parent().prop('id'); //not very good coding practice

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

	// when a submit button for adding is clicked, make it the only one with the "clicked" attribute.
	$('button.config_submit').click(function() {
		$('button.config_submit').removeAttr("clicked");
    	$(this).attr("clicked", "true");
	});

	// handles requests to remove objects
	$('a.config_remove').click(function() {
		// confirm...
		if (!window.confirm(this.title || 'Are you sure you wish to delete this?')) {
			return false;
		}

		$item = $(this).parent();

		// id of the parent <li>, which determines the id # of the item
		var parentID = parseInt(/\d+/.exec($item.prop('id')))
		// now we need to know which list we're in
		var config_key = $item.parent().parent().prop('id');

		var options = {};
		options['id'] = parentID;
		options['remove'] = 1;
		options['config_key'] = config_key;

		$.post('/update_config/', options, function(data) {
			if (data === 'FAILURE') {
				console.log("Failed to remove item " + parentID + " from " + config_key);
				return;
			}
			// get rid of it.
			$item.remove();
		});

		// just so that we don't go anywhere...
		return false;
	});

});