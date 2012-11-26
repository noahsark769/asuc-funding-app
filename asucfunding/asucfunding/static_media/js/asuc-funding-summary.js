// asuc-funding-summary.js - functions and bindings for sorting, filtering, and calculating things about the request summary table

$(document).ready(function () {
	// populate the options panel
	var $bodyElems,
		set,
		id,
		$toAppend,
		$elemsToShow,
		$allCheckboxes,
		checkboxHTML;

	var $label;
	// aka, take every header td element, and find the corresponding elements in the body
	// take the html from all of those and put it into a set, then for every element in the set,
	// make a checkbox for that, initially checked.
	$.when($('tr.table-header-row td.has-options').each(function () {
		id = $(this).prop('id');
		$bodyElems = $('tbody td.' + id);
		set = {};
		// console.log($('tbody td.' + id));
		$bodyElems.each(function () {
			// console.log('fuck yeah!!');
			// console.log($(this).html());
			set[$(this).html()] = true;
		});
		$toAppend = $('tr#request_summary_options_form td.' + id);
		// console.log($toAppend);
		$toAppend.empty();
		// console.log('got here');
		// console.log(set);
		for (var html in set) {
			// console.log('html is' + html)
			checkboxHTML = '<div class="form-option" id="' + html +'">' +
			'<input type="checkbox" name="' + id + '" value="' + html + '" >' +
			'<label for="' + id + '">'+ html + '</label></div>';
			$toAppend.append(checkboxHTML);
		}
	})).done(function () {
		// bind filter functionality to when the checkboxes get changed
		$('div.form-option input[type=checkbox]').change(function () {
			console.log('holy shit');
			// the important thing here is that we want within the td's to be an OR relationship but between td's
			// to be an AND relationship. which means we have to go through each td and add, then filter the results
			$allOptionGroups = $('tr#request_summary_options_form td:not(.id):not(.null)');
			// get the label associated with the checkbox, then find all the tr's with that label
			// hide everything, then show those tr's.
			$elemsIntersection = $('tbody tr');
			$allOptionGroups.each(function(){
				$elemsUnion = $();
				$(this).find('input[type=checkbox]').each(function () {
					parentID = $(this).parent().parent().prop('class'); //first parent is div, second is td
					// console.log(parentID);
					$label = $(this).siblings('label[for=' + $(this).prop('name') + ']');
					// console.log($label.html());
					if ($(this).prop('checked') === true) {
						$elemsUnion = $elemsUnion.add($('tbody tr').filter(function(index) {
							return $(this).children('td.' + parentID).html() == $label.html();
						}));
					}
				});
				console.log($elemsUnion);
				console.log($elemsIntersection.length);
				$elemsIntersection = $elemsIntersection.filter($elemsUnion);
				console.log($elemsIntersection.length);
				// } else {
				// 	$elemsToShow.remove($('tbody tr').filter(function(index) {
				// 		return $(this).children('td.' + parentID).html() == $label.html();
				// 	}));
				// }
			});

			console.log("trololo!" + $elemsIntersection.length);

			$('tbody tr').hide();
			$elemsIntersection.show();
		});
	});

	// bind select all
	$('a#select_all').click(function () {
		$('div.form-option input[type=checkbox]').prop('checked', 'true');
	});

	// sorting
	var $rows,
		sorted,
		parentID,
		isUp;

	$('a.sort-up, a.sort-down').click(function () {
		// get all the rows, then clear out everything, then put everything back in in sorted order.
		isUp = $(this).hasClass('sort-up');
		$rows = $('tbody tr');
		parentID = $(this).parent().prop('id');
		sorted = $rows.sort(function (a, b) {
			// a and b are tr html DOM elements.
			$aChild = $(a).children('td.' + parentID);
			$bChild = $(b).children('td.' + parentID);
			if (isUp) {
				return $aChild.html().localeCompare($bChild.html());
			} else {
				return $aChild.html().localeCompare($bChild.html()) * -1;
			}
		});
		$('tbody').empty();
		$('tbody').append($(sorted));
	});

	// calculate requested totals
	var grandRequestedTotal = 0,
		grandAwardedTotal = 0,
		number,
		html,
		value,
		$requestedData,
		$awardedData;

	$('tbody tr').each(function() {
		$requestedData = $(this).find('.requested-total');
		$awardedData = $(this).find('.awarded-total');
		html = $requestedData.html();
		number = html.slice(1); // have to slice off the $ sign
		value = parseFloat(number); //will break if something is not an integer
		grandRequestedTotal += value;

		html = $awardedData.html();
		number = html.slice(1); // have to slice off the $ sign
		value = parseInt(number); //will break if something is not an integer
		grandAwardedTotal += value;
	});

	$('td#requested_grand_total').html(grandRequestedTotal);
	$('td#awarded_grand_total').html(grandAwardedTotal);
});