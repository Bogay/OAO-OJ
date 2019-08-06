var editor;

window.onload = () => {
	editor = ace.edit('editor');
}

function test() {
    $.post('/', { 'input_data': $('#input').val(), 'output_data': $('#output').val(), 'script': editor.getValue() }, function(data) {
        $('#info').html(data);
    });
}

function submit() {
    $.post('/', { 'script': editor.getValue() }, function(data) {
        $('#info').html(data);
    });
}

function rmnewline() {
	str = editor.getValue();
	console.log('str befor: ' + str);
	str = str.replace(/(\r\n|\r|\n)/g, ' ');
	// str.replace(/\r/g, '');
	console.log('str after: ' + str);
	editor.setValue(str);
}

function scale_font(o) {
	var fontsize = o.value + 'px';
	console.log('o: ' + o);
    $('#editor').css('fontSize', fontsize);
}
