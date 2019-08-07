var editor;

window.onload = () => {
    editor = ace.edit('editor');
};

url = "http://oao-oj.herokuapp.com";

function info() {
    $.get(url, function(data) {
        $("#info").html(marked(data));
    });
}

function submit() {
    $.post(url, { 'script': editor.getValue() }, function(data) {
        alert(data['result']);
    });
}

function test() {
    $.post(url, { 'input-data': $('#input').val(), 'output-data': $('#output').val(), 'script': editor.getValue() }, function(data) {
        alert(data['result']);
    });
}

function rmnewline() {
    str = editor.getValue();
    // console.log('str befor: ' + str);
    str = str.replace(/((\r\n|\r|\n)[ \t\n\r]*)+/g, '');
    // console.log('str after: ' + str);
    editor.setValue(str);
}

function scale_font(o) {
    var fontsize = o.value + 'px';
    // console.log('o: ' + o);
    $('#editor').css('fontSize', fontsize);
}