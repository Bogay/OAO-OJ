function submit() {
    $.post('/', { 'script': editor.getValue() }, function(data) {
        $('#info').html(data);
    });
}

function test() {
    $.post('/', { 'input_data': $('#input').val(), 'output_data': $('#output').val(), 'script': editor.getValue() }, function(data) {
        $('#info').html(data);
    });
}

function scale_font(o) {
	var fontsize = o.value + 'px';
	console.log('fontSize: ' + fontsize);
    $('#editor').css('fontSize', fontsize);
}
