var editor;

const url = 'http://localhost:8000/';

window.onload = () => {
    editor = ace.edit('editor');

    $('#rule-modal').modal();

    $('#result-modal').on('shown.bs.modal', (event) => {
        let method = $(event.relatedTarget).data('method');

        let payload = {
            'script': editor.getValue(),
        };

        if(method === 'test') {
            payload['input-data'] = $('#test-input').val();
            payload['output-data'] = $('#test-output').val();
        }

        $.post(url, payload, function(data) {
            $('#result-modal').modal('hide');
            show_result(data['result']);
        })
    });
};

function show_result(result) {
    swal(
        ... {
            AC: ['Accepted!', 'Congrats!', 'success'],
            WA: ['Wrong Answer!', 'OAQ!', 'error'],
            LLE: ['Lines Limit Exceed!', 'OAO!', 'error'],
        }[result]
    )
}

function rule() {
    $.get('rule/main.md', function(data) {
        $('#rule').html(marked(data));
    });
}

function info() {
    $.get('prob/index.md', function(data) {
        $('#info').html(marked(data));
    });
}

function rmnewline() {
    str = editor.getValue();
    str = str.replace(/((\r\n|\r|\n)[ \t\n\r]*)+/g, '');
    editor.setValue(str);
}

function scale_font(o) {
    var fontsize = o.value + 'px';
    editor.setFontSize(fontsize);
}