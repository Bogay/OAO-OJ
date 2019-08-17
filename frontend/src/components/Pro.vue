<template>
  <div class="container-fluid">
    <!-- Result dialog (now replace with swal)-->
    <div class="modal fade" id="result-modal">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Result</h4>
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                </div>
                <div class="modal-body" id="result">
                    <div class="spinner-border"></div>
                    Judging...
                </div>
            </div>
        </div>
    </div>
    <div class="row">
      <div class="col-6">
        <b-tabs content-class="mt-3" fill>
          <b-tab title="Description" active></b-tab>
          <b-tab title="Submission"></b-tab>
          <b-tab title="Discussion"></b-tab>
        </b-tabs>
      </div>
        <!-- <div id="info-area" class="col-sm-6 d-flex flex-column">
            <ul id="info-nav" class="nav nav-tabs">
                <li class="nav-item"><a class="nav-link active" data-toggle="tab" href="#info">Description</a></li>
                <li class="nav-item"><a class="nav-link" data-toggle="tab" href="#submission">Submission</a></li>
                <li class="nav-item"><a class="nav-link" data-toggle="tab" href="#discussion">Discussion</a></li>
            </ul>
            <div id="info-content" class="tab-content flex-grow-1">
                <div id="info" class="tab-pane active">
                    <h1>Description</h1>
                </div>
                <div id="submission" class="tab-pane">
                    <h1>Submission</h1>
                </div>
                <div id="discussion" class="tab-pane">
                    <h1>Discussion</h1>
                </div>
            </div>
        </div> -->
      <div id="code-area" class="col-sm-6">
        <div class="card">
          <!-- Editor Style Setting -->
          <div id="fontsize-select-box" class="card-header">
            FontSize:
            <b-form-select title="FontSize:" v-model="selected" :options="options" size="sm" class="fss"></b-form-select>
          </div>
          <div class="card-body d-flex">
            <div id="editor" class="editor flex-grow-1"></div>
          </div>
        </div>
        <div id="run" class="mt-3">
          <b-tabs no-fade>
            <b-tab title="Input" active>
              <b-form-textarea v-model="input" placeholder="Input" rows="3" class="text-area"></b-form-textarea>
            </b-tab>
            <b-tab title="Output">
              <b-form-textarea v-model="output" placeholder="Output" rows="3" class="text-area"></b-form-textarea>
            </b-tab>
          </b-tabs>
          <div class="mt-3">
            <b-button-group>
              <b-button variant="success">Success</b-button>
              <b-button variant="info">Info</b-button>
              <b-button variant="warning">Warning</b-button>
            </b-button-group>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ace from '../../static/ace-builds/src-noconflict/ace.js'

// var editor = ace.edit('editor')
// editor.setOptions({
//   theme: 'ace/theme/monokai',
//   printMargin: false,
//   useWrapMode: true,
//   indentedSoftWrap: false
// })

// editor.session.setOptions({
//   mode: 'ace/mode/python',
//   newLineMode: 'unix',
//   useSoftTabs: true,
//   tabSize: 4,
//   wrap: true
// })

export default {
  name: 'Pro',
  data () {
    return {
      selected: null,
      options: [
        { value: null, text: '--' },
        { value: '8', text: '8' },
        { value: '10', text: '10' },
        { value: '11', text: '11' },
        { value: '12', text: '12' },
        { value: '13', text: '13' },
        { value: '14', text: '14' },
        { value: '16', text: '16' },
        { value: '18', text: '18' },
        { value: '24', text: '24' },
        { value: '32', text: '32' },
        { value: '48', text: '48' }
      ],
      input: '',
      output: ''
    }
  }
}
</script>

<style lang="css" scoped>
.fss {
  width: 10vh;
}

.text-area {
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
}
</style>
