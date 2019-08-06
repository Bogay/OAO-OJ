url = "http://oao-oj.herokuapp.com";

function submit() {
    $.post(url, { "script": editor.getValue() }, function(data) {
        $("#info").html(data);
    });
}

function test() {
    $.post(url, { "input_data": $("#input").val(), "output_data": $("#output").val(), "script": editor.getValue() }, function(data) {
        $("#info").html(data);
    });
}

function info() {
    $.get(url, function(data) {
        $("#info").html(marked(data));
    });
}