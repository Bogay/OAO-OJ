// const url = 'http://localhost:8000/';
const API_PORT = ':8000';
const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT);
const API_PROB_URL = API_BASE_URL + '/problems';

function list() {
	$.get(API_PROB_URL, function(prob) {
	    $('#table').bootstrapTable({
	        data: prob,
	    });
    });
}
