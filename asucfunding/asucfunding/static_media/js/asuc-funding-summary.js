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
		$requestedData = $(this).child('.requested-total');
		$awardedData = $(this).child('.awarded-total');
		html = $requestedData.html();
		number = html.slice(1); // have to slice off the $ sign
		value = parseInt(number); //will break if something is not an integer
		grandRequestedTotal += value;

		html = $awardedData.html();
		number = html.slice(1); // have to slice off the $ sign
		value = parseInt(number); //will break if something is not an integer
		grandAwardedTotal += value;
	});
});