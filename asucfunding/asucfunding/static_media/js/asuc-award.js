$(document).ready(function() {
	//if ($('#recurring_event_footer_block').is(':visible')) {
	if ($('#recurring_event_footer_block').is(':visible')) {
		var totalAmtReq = 0;
		var totalOthFund = 0;
		$('.req_amt').each(function() {
			totalAmtReq += parseFloat($(this).attr('value'));
		});
		$('.oth_fund').each(function() {
			totalOthFund += parseFloat($(this).attr('value'));
		});
		$('#recurring_total_amount_requested').html('$' + totalAmtReq);
		$('#recurring_total_other_funding').html('$' +totalOthFund);
		$('#recurring_grand_total').html('$' + (totalAmtReq + totalOthFund));
	}

	if ($('#travel_budget_block').is(':visible')) {
		var total = 0;
		$(this).find('.travel_item_total').each(function() {
			total += parseFloat($(this).attr('value'));
		});
		$('#travel_budget_total_1').html('$' + total);
	}

	var i = 0;
	$('.recurring_budget_block').each(function() {
		i++;
		if ($('.recurring_budget_block').is(':visible')) {
			$('.budget_item_description').each(function() {
				$block = $(this).closest('.recurring_budget_block');
				var totalAmtReq = 0;
				var totalOthFund = 0;
				$block.find('.req_amt').each(function() {
					totalAmtReq += parseFloat($(this).attr('value'));
				});
				$block.find('.oth_fund').each(function() {
					totalOthFund += parseFloat($(this).attr('value'));
				});
				$('#budget_total_amount_requested_' + i).html('$' + totalAmtReq);
				$('#budget_total_other_funding_' + i).html('$' +totalOthFund);
				$('#budget_total_' + i).html('$' + (totalAmtReq + totalOthFund));
			});
		}
	});

	$('.budget_block').each(function() {
		if ($('.budget_block').is(':visible')) {
			$('.budget_item_description').each(function() {
				$block = $(this).closest('.budget_block');
				var totalAmtReq = 0;
				var totalOthFund = 0;
				$block.find('.req_amt').each(function() {
					totalAmtReq += parseFloat($(this).attr('value'));
				});
				$block.find('.oth_fund').each(function() {
					totalOthFund += parseFloat($(this).attr('value'));
				});
				$('#budget_total_amount_requested_1').html('$' + totalAmtReq);
				$('#budget_total_other_funding_1').html('$' +totalOthFund);
				$('#budget_total_1').html('$' + (totalAmtReq + totalOthFund));
			});
		}
	});

	$('#award_form').ajaxForm({
		beforeSubmit: function() {
			if (!window.confirm(this.title || 'Are you sure you wish to submit?')) {
				return false;
			}
			return true;
		},
		success: function() {
			window.location.href = '/';
		}
	});

});