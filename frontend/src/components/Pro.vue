<template>
  <div class="container-fluid">
    <div class="row">
      <!-- left part -->
      <div class="col-6">
        <b-card no-body class="info-area">
          <b-tabs content-class="m-0" card fill>
            <b-tab title="Description" active class="pt-0" ><h5>{{ pid }} - {{ title }}</h5><vue-markdown :source='desc'></vue-markdown></b-tab>
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
            <b-form-select v-model="selected" @change="onChange($event)" :options="options" size="sm" class="fss"></b-form-select>
          </div>
          <!-- codemirror -->
          <div class="card-body p-0" v-if="show"><Editor :source="source" :fontSize="fontSizeValue"></Editor></div>
        </div>
        <!-- test-area -->
        <b-tabs no-fade class="mt-3">
          <b-tab title="Input" active class="p-0">
            <b-form-textarea v-model="input" placeholder="Input" rows="3" class="text-area"></b-form-textarea>
          </b-tab>
          <b-tab title="Output" class="p-0">
            <b-form-textarea v-model="output" placeholder="Output" rows="3" class="text-area"></b-form-textarea>
          </b-tab>
        </b-tabs>
        <div class="mt-3">
          <b-button-group>
            <b-button class="tri-btn" variant="primary" @click="onTest">Test</b-button>
            <b-button class="tri-btn" variant="success" @click="onSubmit">Submit</b-button>
            <b-button class="tri-btn" variant="dark">Statistics</b-button>
          </b-button-group>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Editor from './Editor'
import VueMarkdown from 'vue-markdown'
import swal from 'sweetalert'

const API_PORT = ':8000'
const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT)
const FONTSIZE_OPTION = [8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 24, 32, 48]

export default {
  name: 'Pro',
  data () {
    return {
      pid: '',
      title: '',
      desc: 'loading',
      selected: 12,
      options: FONTSIZE_OPTION,
      source: 'print(\'Hello, World!\')',
      fontSizeValue: '12px',
      show: true,
      input: '',
      output: ''
    }
  },
  components: {
    Editor,
    VueMarkdown
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/probs/${this.$route.params.id}`)
      .then((response) => {
        this.pid = response.data.pid
        this.title = response.data.title
        this.desc = response.data.desc
      })
      .catch((error) => {
        this.desc = error
      })
  },
  methods: {
    getChildText (value) {
      this.source = value
    },
    onChange (event) {
      this.fontSizeValue = this.selected + 'px'
    },
    onTest (event) {
      let DATA = {
        'pid': this.pid,
        'script': this.source,
        'input-data': this.input,
        'output-data': this.output
      }
      this.$http.post(`${API_BASE_URL}/judge/submit`, DATA)
        .then((response) => {
          console.log(JSON.stringify(DATA, null, 2))
          console.log(JSON.stringify(response.data, null, 2))
          if (response.data.results[0] === 'AC') {
            swal('Test Result: YES', '', 'success')
          } else if (response.data.results[0] === 'WA') {
            swal('Test Result: NO', '', 'error')
          } else if (response.data.results[0] === 'LLE') {
            swal('Test Result: LLE', 'Your source code is more than one line(contain \\n, \\r, ;).', 'error')
          } else {
            swal('Judge Error', 'please contact with us, sorry!', 'info')
          }
        })
        .catch((error) => {
          console.log(error)
        })
    },
    onSubmit (event) {
      let DATA = {
        'pid': this.pid,
        'script': this.source
      }
      this.$http.post(`${API_BASE_URL}/judge/submit`, DATA)
        .then((response) => {
          if (response.data.results[0] === 'AC') {
            swal('Accepted', 'You solved the problem!', 'success')
          } else if (response.data.results[0] === 'WA') {
            swal('Wrong Answer', 'Your output is not correct.', 'error')
          } else if (response.data.results[0] === 'LLE') {
            swal('Line Limit Exceeded', 'Your source code is more than one line(contain \\n, \\r, ;).', 'error')
          } else {
            swal('Judge Error', 'please contact with us, sorry!', 'info')
          }
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style lang="scss">
.info-area {
  height: 85vh;
  overflow-y: auto;
}

.fss {
  width: 10vh;
}

.text-area {
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
  border: solid 0.01vw #dee2e6;
}

.CodeMirror {
  font-family: 'Monaco';
}

.tri-btn {
  font-size: 1.25vw;
  width: 16vw;
}
</style>
