// asuc-funding-summary.js - functions and bindings for sorting, filtering, and calculating things about the request summary table

$(document).ready(function () {
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

	// sorting
	var $rows,
		sorted,
		parentID;

	$('a.sort-up').click(function () {
		// get all the rows, then clear out everything, then put everything back in in sorted order.
		$rows = $('tbody tr');
		parentID = $(this).parent().prop('id');
		sorted = $rows.sort(function (a, b) {
			// a and b are tr html DOM elements.
			$aChild = $(a).children('td.' + parentID);
			$bChild = $(b).children('td.' + parentID);
			return $aChild.html().localeCompare($bChild.html());
		});
		$('tbody').append($(sorted));
	});
});