url = "http://oao-oj.herokuapp.com";

function submit() {
    $.post(url, { 'script': editor.getValue() }, function(data) {
        alert(data['result']);
    });
}

function test() {
    $.post(url, { 'input_data': $('#input').val(), 'output_data': $('#output').val(), 'script': editor.getValue() }, function(data) {
        alert(data['result']);
    });
}

function scale_font(o) {
    var fontsize = o.value + 'px';
    console.log('o: ' + o);
    $('#editor').css('fontSize', fontsize);
}


function info() {
    $.get(url, function(data) {
        $("#info").html(marked(data));
    });
}