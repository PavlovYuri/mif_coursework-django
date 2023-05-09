var current_value_share = document.getElementById('current-value-share-span');
var all_shares = document.getElementById('all-shares-span');
var number_shares_input = document.getElementById('number-shares-input');
var your_share = document.getElementById('your-share-span');
var your_investment = document.getElementById('your-investment-span');


number_shares_input.addEventListener("input", function() {
    your_share.innerHTML = Number(number_shares_input.value) / Number(all_shares.innerHTML); 
    your_investment.innerHTML = Number(number_shares_input.value) * Number(current_value_share.innerHTML);
});

number_shares_input.addEventListener('focusout', function() {
    your_share.innerHTML = '';
    your_investment.innerHTML = '';
});

