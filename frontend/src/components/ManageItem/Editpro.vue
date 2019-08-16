<template>
  <b-container fluid>
      <!--  -->
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group-pid" label="pid:" label-for="input-pid"
        description="problem's id, wont let it be modified in the future."
      >
        <b-form-input
          id="input-pid"
          v-model="form.pid"
          type="text"
          required
          :placeholder="`Enter pid, such as ${$route.params.pid}`"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-title" label="title:" label-for="input-title">
        <b-form-input
          id="input-title"
          v-model="form.title"
          type="text"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-status" label="status:" label-for="input-status">
        <b-form-select
          id="input-status"
          v-model="form.status"
          :options="status"
          required
        ></b-form-select>
      </b-form-group>

      <div class="row">
        <div class="col-6">
          <b-form-group id="input-group-desc" label="description:" label-for="input-desc">
            <b-form-textarea
              id="input-desc"
              v-model="form.desc"
              placeholder="preview on the right side"
              rows="3"
            ></b-form-textarea>
          </b-form-group>
        </div>
        <div class="col-6 prevw">
          <vue-markdown>{{ form.desc }}</vue-markdown>
        </div>
      </div>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
      <b-button variant="info" @click="onDefault">Defaults</b-button>
      <b-button variant="info" @click="onPreview">Preview</b-button>
    </b-form>

    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </b-container>
</template>

<script>
import VueMarkdown from 'vue-markdown'
const API_PORT = ':8000'
const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT)

export default {
  name: 'Editpro',
  data () {
    return {
      form: {
        pid: '',
        title: '',
        status: null,
        desc: ''
      },
      status: [
        { text: 'Select One', value: null },
        { text: 'Online', value: 0 },
        { text: 'Hidden', value: 2 },
        { text: 'Offline', value: 1 }
      ],
      show: true,
      items: []
    }
  },
  components: {
    VueMarkdown
  },
  mounted () {
    console.log(`${API_BASE_URL}/probs/${this.$route.params.pid}`)
    this.$http.get(`${API_BASE_URL}/probs/${this.$route.params.pid}`)
      .then((response) => {
        this.items = response.data
        // set default value
        this.form.pid = this.items.pid
        this.form.title = this.items.title
        // this.form.status = this.items.status
      })
      .catch((error) => {
        this.items = error
        console.log('err: ' + error)
      })
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.pid = ''
      this.form.title = ''
      this.form.status = null
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    onDefault (evt) {
      evt.preventDefault()
      this.form.pid = this.items.pid
      this.form.title = this.items.title
      // this.form.status = this.items.status
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    onPreview (evt) {
      evt.preventDefault()
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style lang="css" scoped>
.prevw {
  border: 0.1vw solid #ccc;
  border-radius: 1vw;
  max-height: 50vh;
  overflow-y: auto;
}
</style>
