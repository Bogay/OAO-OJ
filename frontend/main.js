var editor;

window.onload = () => {
    editor = ace.edit('editor');

    $("#rule-modal").modal();

    $("#result-modal").on('show.bs.modal', function () {
        $("#result").html('<div class="spinner-border"></div>Judging...');
    });
};

url = "http://localhost:8000/";

function info() {
    $.get('prob/index.md', function(data) {
        $("#info").html(marked(data));
    });
}

function submit() {
    $("#result-modal").modal();
    $.post(url, { 'script': editor.getValue() }, function(data) {
        $("#result").html(data['result']);
    });
}

function test() {
    $("#result-modal").modal();
    $.post(url, { 'input-data': $('#input').val(), 'output-data': $('#output').val(), 'script': editor.getValue() }, function(data) {
        $("#result").html(data['result']);
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