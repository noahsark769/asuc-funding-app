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
				return;
			}
			// get rid of it.
			$item.remove();
		});

		// just so that we don't go anywhere...
		return false;
	});

	// ===== REQUEST FORM HANDLERS =====

	// Initialize
	{
		// hide unnecessary blocks
		$('#request_form > div').hide();
		$('#request_selector_block').show();
		$('#ug_request_categories').hide();
		$('#grad_request_categories').hide();
		$('#ug_grant_categories').hide();
		$('#grad_grant_categories').hide();
		$('#event_type').hide();

		// add/remove event buttons
		$('#add_event').hide();
		$('#remove_event').hide();

		// disable student group textbox
		$('input:text[name=pending_student_group]').prop('disabled', true);
	}

	// handle request_type choice
	$('input:radio[name=request_type]').change(function() {
		switch ($(this).val()) {
			case 'G':
				// request selector block options
				$('#ug_request_categories').hide();
				$('#grad_request_categories').show();
				$('#ug_grant_categories').hide();
				$('#grad_grant_categories').show();
				$('#event_type').show();

				// header block options
				$('#graduate_request_block').show();
				$('#undergraduate_request_block').hide();
				$('#travel_request_block').hide();

				// travel event/budget blocks
				$('#travel_event_block').hide();
				$('#travel_budget_block').hide();
				break;
			case 'U':
				// request selector block options
				$('#ug_request_categories').show();
				$('#grad_request_categories').hide();
				$('#ug_grant_categories').show();
				$('#grad_grant_categories').hide();
				$('#event_type').show();

				// header block options
				$('#graduate_request_block').hide();
				$('#undergraduate_request_block').show();
				$('#travel_request_block').hide();

				// travel event/budget blocks
				$('#travel_event_block').hide();
				$('#travel_budget_block').hide();
				break;
			case 'T':
				// request selector block options
				$('#ug_request_categories').hide();
				$('#grad_request_categories').hide();
				$('#ug_grant_categories').hide();
				$('#grad_grant_categories').hide();
				$('#event_type').hide();

				// header block options
				$('#graduate_request_block').hide();
				$('#undergraduate_request_block').hide();
				$('#travel_request_block').show();

				// travel event/budget blocks
				$('#travel_event_block').show();
				$('#travel_budget_block').show();

				// reset event_type and event/budget blocks
				$('#event_type input:radio').prop('checked', false);
				resetEventsAndBudgets();
				break;
		}
	});
	
	// handle pending student group choice
	$('select[name=student_group]').change(function() {
		if ($(this).val() === 'pending')
			$('input:text[name=pending_student_group]').prop('disabled', false);
		else
			$('input:text[name=pending_student_group]').prop('disabled', true);
	});

	// handle event_type choice
	$('input:radio[name=event_type]').change(function() {
		switch ($(this).val()) {
			case 'S':
				// show the appropriate header
				$('#event_header_block').show();
				$('#recurring_event_header_block').hide();

				/* we want to have 1 event and 1 budget,
				but their values are preserved, in the case
				of changing from R to S*/
				resetEventsAndBudgets(false);
				$('#event_block_1').show();
				$('#budget_block_1').show();
				resetBudget($('#budget_block_1'), 1);

				// add/remove event buttons
				$('#add_event').hide();
				$('#remove_event').hide();
				break;
			case 'R':
				// show the appropriate header
				$('#event_header_block').hide();
				$('#recurring_event_header_block').show();

				// we want to reset the blocks, and prompt for same/diff. budget choice
				resetEventsAndBudgets(false);

				// then, reset same/diff budget choice
				$('#recurring_same_budget_Y').removeAttr('checked');
				$('#recurring_same_budget_N').removeAttr('checked');
				break;
			case 'O':
				// show the appropriate header
				$('#event_header_block').hide();
				$('#recurring_event_header_block').hide();

				// we want to completely reset everything, and show one budget.
				resetEventsAndBudgets(true);
				$('#budget_block_1').show();
				resetBudget($('#budget_block_1'), 1);

				// add/remove event buttons
				$('#add_event').hide();
				$('#remove_event').hide();
				break;
		}
	});
	
	// handle same/diff. budget choice
	$('input:radio[name=recurring_same_budget]').change(function() {
		switch ($(this).val()) {
			case 'Y': // same
				// here, we're starting from nothing, add 3 events, 1 budget
				if ($('#event_block_1').is(':hidden')) {
					$('#event_block_1').show();
					$('#budget_block_1').show();
					resetBudget($('#budget_block_1'), 1);
					addEvent('#event_block_1');
					addEvent('#event_block_2');
					addEvent('#event_block_3');
				}
				else {
					// remove other budgets, and place 1st budget after last event
					resetBudgets(false);
					$('#budget_block_1').insertAfter($('#event_block_' + $('.event_block').length));
					$('#budget_block_1').show();
					resetBudget($('#budget_block_1'), 1);
				}

				// add/remove event buttons
				$('#add_event').show();
				$('#remove_event').show();
				break;
			case 'N': // diff
				// starting from nothing, alternate 4 events and budgets
				if ($('#event_block_1').is(':hidden')) {
					$('#event_block_1').show();
					$('#budget_block_1').show();
					resetBudget($('#budget_block_1'), 1);
					for (var i=1;i<=3;i++) {
						addEvent('#budget_block_' + i);
						addBudget('#event_block_' + (i+1));
					}
				}
				else {
					// reset budgets, give each event one budget.
					resetBudgets(true);
					$('#budget_block_1').insertAfter($('#event_block_1'));
					$('#budget_block_1').show();
					resetBudget($('#budget_block_1'), 1);
					$('.event_block').each(function() {
						var id = $(this).prop('id');
						if (id != 'event_block_1') {
							addBudget('#' + id);
						}
					});
				}

				// add/remove event buttons
				$('#add_event').show();
				$('#remove_event').show();
				break;
		}
	});

	function addEvent(after) {
		// figure out how many event blocks we already have
		var numEvents = $('.event_block').length;
		// clone the event, copying data and handlers
		$clone = $('#event_block_' + numEvents).clone();
		// fix the numbers
		setEventInputNumbers($clone, numEvents+1);
		// add the clone to the document to 'after'
		$(after).after($clone);
	}

	function setEventInputNumbers($elem, num) {
		var elToAttr = [ // elements to attributes
			['label', 'for'],
			['input', 'name'],
			['input', 'id'],
			['select', 'name']
		];
		// replace ID string of the div
		var idString = $elem.prop('id');
		var prefix = idString.replace(/[0-9]+/,'');
		if (prefix && prefix != idString) {
			$elem.prop('id', prefix + num);
		}
		// replace all other attributes.
		for (var i=0; i<elToAttr.length; i++) {
			$elem.find(elToAttr[i][0]).each(function() {
				var string = $(this).attr(elToAttr[i][1]);
				if (string) {
					prefix = string.replace(/[0-9]+/,'');
					if (prefix && prefix != string) {
						$(this).attr(elToAttr[i][1], prefix + num);
					}
				}
			});
		}
	}

	function addBudget(after) {
		// figure out how many event blocks we already have
		var numBudgets = $('.budget_block').length;
		// clone the event, copying data and handlers
		$clone = $('#budget_block_' + numBudgets).clone();
		// add the clone to the document to 'after'
		$(after).after($clone);
		// reset the item description fields
		resetBudget($clone, numBudgets+1);
	}

	// budget item add/remove handlers

	$(document).on('click', '.add_budget_item', function() {
		addItemDescription($(this).closest('div'));
		$(this).siblings().each(function() {
			if ($(this).get(0).tagName === 'BUTTON')
				$(this).prop('disabled', false);
		});
		return false;
	});

	function addItemDescription($b) {
		num = extractNumber($b.prop('id'));
		var numItemDescriptions = $b.find('.budget_item_description').length;
		$clone = $('#budget_item_description_' + num + '_' + numItemDescriptions).clone();
		setBudgetItemNumbers($clone, num, numItemDescriptions+1);
		$clone.insertAfter($('#budget_item_description_' + num + '_' + numItemDescriptions));
	}

	function setBudgetItemNumbers($elem, num, numItems) {
		// change item's id
		var id = $elem.prop('id');
		$elem.prop('id', id.replace(/[0-9]+_[0-9]+/,'') + num + '_' + numItems);
		// change each input
		$elem.find('input:text').each(function() {
			var prefix = $(this).prop('id').replace(/[0-9]+_[0-9]+/,'');
			$(this).prop('id', prefix + num + '_' + numItems);
			$(this).prop('name', prefix + num + '_' + numItems);
		});
	}

	$(document).on('click', '.remove_budget_item', function() {
		var $parent = $(this).closest('div');
		var numItems = $parent.find('tr').length - 1;
		if (numItems === 1)
			return;
		else if (numItems === 2)
			$(this).prop('disabled', true);

		var id = extractNumber($parent.prop('id'));
		$('#budget_item_description_' + id + '_' + numItems).remove();
		return false;
	});

	// travel budget item add/remove handlers

	$(document).on('click', '.travel_add_budget_item', function() {
		addTravelItemDescription($(this).closest('div'));
		$(this).siblings().each(function() {
			if ($(this).get(0).tagName === 'BUTTON')
				$(this).prop('disabled', false);
		});
		return false;
	});

	function addTravelItemDescription($b) {
		var num = $b.find('.travel_budget_item_description').length;
		$clone = $('#travel_budget_item_description_' + num).clone();
		setTravelBudgetItemNumbers($clone, num+1);
		$clone.insertAfter($('#travel_budget_item_description_' + num));
	}

	function setTravelBudgetItemNumbers($elem, numItems) {
		// change item's id
		var id = $elem.prop('id');
		$elem.prop('id', id.replace(/[0-9]+/,'') + numItems);
		// change each input
		$elem.find('input:text').each(function() {
			var prefix = $(this).prop('id').replace(/[0-9]+/,'');
			$(this).prop('id', prefix + numItems);
			$(this).prop('name', prefix + numItems);
		});
	}

	$(document).on('click', '.travel_remove_budget_item', function() {
		var $parent = $(this).closest('div');
		var numItems = $parent.find('tr').length - 1;
		if (numItems === 1)
			return;
		else if (numItems === 2)
			$(this).prop('disabled', true);

		$('#travel_budget_item_description_' + numItems).remove();
		return false;
	});

	// handle adding/removing events
	$(document).on('click', '#add_event', function() {
		// re-enable remove button
		if ($('.event_block').length === 1) {
			$(this).siblings().each(function() {
				if ($(this).get(0).tagName === 'BUTTON')
					$(this).prop('disabled', false);
			});
		}
		// check whether we are using the same budget or not.
		var sameBudget;
		$('input:radio[name=recurring_same_budget]').each(function() {
			if ($(this).prop('checked') === true)
				sameBudget = $(this).prop('value');
		});
		// add only an event
		if (sameBudget == 'Y') {
			addEvent('#event_block_' + $('.event_block').length);
		}
		// add an event and a budget
		else {
			addEvent('#budget_block_' + $('.budget_block').length);
			addBudget('#event_block_' + $('.event_block').length);
		}
		return false;
	});

	// handle adding/removing events
	$(document).on('click', '#remove_event', function() {
		// disable button if necessary
		var numEventBlocks = $('.event_block').length;
		if (numEventBlocks === 1) {
			return;
		}
		else if (numEventBlocks === 2) {
			$(this).prop('disabled', true);
		}
		// check whether we are using the same budget or not.
		var sameBudget;
		$('input:radio[name=recurring_same_budget]').each(function() {
			if ($(this).prop('checked') === true)
				sameBudget = $(this).prop('value');
		});
		// remove only an event
		if (sameBudget == 'Y') {
			$('#event_block_' + $('.event_block').length).remove();
		}
		// remove an event and a budget
		else {
			$('#event_block_' + $('.event_block').length).remove();
			$('#budget_block_' + $('.budget_block').length).remove();
		}
		return false;
	});

	// reset handlers

	function resetEventsAndBudgets(preserve) {
		resetEvents(preserve);
		resetBudgets(preserve);
	}

	function resetEvents(preserve) {
		// remove all event blocks except for the first
		$('.event_block').each(function() {
			if ($(this).prop('id') === 'event_block_1') {
				$(this).hide();
				// reset the form fields, if we're not preserving them
				if (!preserve)
					$('#event_block_1').find('input:text, select').val('');
			}
			else
				$(this).remove();
		});
	}

	function resetBudgets(preserve) {
		// remove all budget blocks except for the first
		$('.budget_block').each(function() {
			if ($(this).prop('id') === 'budget_block_1')
				$(this).hide();
			else
				$(this).remove();
		});
	}

	function resetBudget($budget, num) {
		// rename ID string
		$budget.prop('id', 'budget_block_' + num);

		// rename additional info
		var elToAttr = [
			['label', 'for'],
			['textarea', 'id'],
			['textarea', 'name']
		];
		for (var i=0; i<elToAttr.length; i++) {
			$budget.find(elToAttr[i][0]).each(function() {
				var string = $(this).attr(elToAttr[i][1]);
				if (string) {
					prefix = string.replace(/[0-9]+/,'');
					if (prefix && prefix != string) {
						$(this).attr(elToAttr[i][1], prefix + num);
					}
				}
			});
		}

		// reset first budget item, remove the rest
		$budget.find('tr').each(function() {
			var id = $(this).prop('id');
			if (id === 'budget_item_headers')
				return;

			else if (id.substr(id.length-1) === '1') {
				// add proper number to id string
				$(this).prop('id', 'budget_item_description_' + num + '_1');
				$(this).find('input:text').val('');
				// rename each input
				$(this).find('input:text').each(function() {
					var prefix = $(this).prop('id').replace(/[0-9]+_[0-9]+/,'');
					$(this).prop('id', prefix + num + '_1');
					$(this).prop('name', prefix + num + '_1');
				});
			}
			// if it's another budget item, delete it.
			else
				$(this).remove();
		});
		// add 3 new ones.
		for (var i=0;i<3;i++) {
			addItemDescription($budget);
		}
	}

});
