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
      <!-- left part -->
      <div class="col-6">
        <b-card no-body>
          <b-tabs content-class="m-0" card fill>
            <b-tab title="Description" active class="pt-0" >
              <h1>Hello</h1>
            </b-tab>
            <b-tab title="Submission" class="pt-0"></b-tab>
            <b-tab title="Discussion" class="pt-0"></b-tab>
          </b-tabs>
        </b-card>
      </div>
      <!-- right part -->
      <div class="col-6">
        <!-- Editor-->
        <div class="card">
          <div class="card-header mb-0 pb-2">
            <label>FontSize:</label>
            <b-form-select v-model="selected" v-on:change="getSelectedItem" :options="options" size="sm" class="fss"></b-form-select>
          </div>
          <!-- codemirror -->
          <div class="card-body p-0" v-if="show"><Editor :code="source" :fontSize="fontSizeValue"></Editor></div>
        </div>
        <!--  -->
        <b-tabs no-fade class="mt-3">
          <b-tab title="Input" active class="p-0">
            <b-form-textarea v-model="input" placeholder="Input" rows="3" class="text-area"></b-form-textarea>
          </b-tab>
          <b-tab title="Output" class="p-0">
            <b-form-textarea v-model="output" placeholder="Output" rows="3" class="text-area"></b-form-textarea>
          </b-tab>
        </b-tabs>
        <div class="mt-3 mb-3">
          <b-button-group>
            <b-button variant="success">Success</b-button>
            <b-button variant="info">Info</b-button>
            <b-button variant="warning">Warning</b-button>
          </b-button-group>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Editor from './Editor'

export default {
  name: 'Pro',
  data () {
    return {
      selected: 12,
      options: [
        { value: 8, text: '8' },
        { value: 9, text: '9' },
        { value: 10, text: '10' },
        { value: 11, text: '11' },
        { value: 12, text: '12' },
        { value: 13, text: '13' },
        { value: 14, text: '14' },
        { value: 15, text: '15' },
        { value: 16, text: '16' },
        { value: 18, text: '18' },
        { value: 24, text: '24' },
        { value: 32, text: '32' },
        { value: 48, text: '48' }
      ],
      source: 'print(\'Hello, World!\')',
      fontSizeValue: '12px',
      show: true,
      input: '',
      output: ''
    }
  },
  components: {
    Editor
  }
}
</script>

<style lang="scss">
.fss {
  width: 10vh;
}

.text-area {
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
}

.CodeMirror {
  font-family: 'Monaco';
}
</style>
