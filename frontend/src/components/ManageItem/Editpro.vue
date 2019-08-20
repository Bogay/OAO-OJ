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
          placeholder="Enter pid, such as 0001"
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
        <div class="col-12">
          <b-form-group id="input-group-desc" label="description:" label-for="input-desc">
            <b-form-textarea
              id="input-desc"
              v-model="form.desc"
              placeholder="problem description in markdown"
              rows="3"
            ></b-form-textarea>
          </b-form-group>
        </div>
        <!-- <div class="col-6 prevw">
          <vue-markdown>{{ form.desc }}</vue-markdown>
        </div> -->
      </div>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
      <b-button variant="info" @click="onDefault">Defaults</b-button>
      <b-button variant="info" @click="onPreview">Preview</b-button>
      <b-button variant="danger" @click="onDelete">Delete</b-button>
    </b-form>

    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </b-container>
</template>

<script>
import VueMarkdown from 'vue-markdown'
import swal from 'sweetalert'
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
    if (this.$route.params.pid !== 'new') {
      this.$http.get(`${API_BASE_URL}/admin/probs/${this.$route.params.pid}`)
        .then((response) => {
          this.items = response.data
          // set default value
          this.form.pid = this.$route.params.pid
          this.form.title = this.items.title
          this.form.status = this.items.status
          this.form.desc = this.items.desc
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      let DATA = {
        'title': this.form.title,
        'status': this.form.status,
        'desc': this.form.desc
      }
      if (this.$route.params.pid === 'new') {
        this.$http.post(`${API_BASE_URL}/admin/probs/${this.form.pid}`, DATA)
          .then((response) => {
            swal('Success', 'the problem has been added.', 'success')
            window.location.replace('/#/manage/problems')
          })
          .catch((error) => {
            swal('Fail', error, 'error')
          })
      } else {
        this.$http.put(`${API_BASE_URL}/admin/probs/${this.form.pid}`, DATA)
          .then((response) => {
            swal('Success', 'the problem has been updated.', 'success')
            window.location.replace('/#/manage/problems')
          })
          .catch((error) => {
            swal('Fail', error, 'error')
          })
      }
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.pid = ''
      this.form.title = ''
      this.form.status = null
      this.form.desc = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    onDefault (evt) {
      evt.preventDefault()
      this.form.pid = this.$route.params.pid
      this.form.title = this.items.title
      this.form.status = this.items.status
      this.form.desc = this.items.desc
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    onDelete (evt) {
      evt.preventDefault()
      swal({
        title: 'Are you sure?',
        text: 'Once deleted, you will not be able to recover this problem!',
        icon: 'warning',
        buttons: true,
        dangerMode: true
      })
        .then((willDelete) => {
          if (willDelete) {
            this.$http.delete(`${API_BASE_URL}/admin/probs/${this.$route.params.pid}`)
              .then((response) => {
                swal('Boo! The problem has been deleted!', {icon: 'success'})
                window.location.replace('/#/manage/problems')
              })
              .catch((error) => {
                swal('Oops! Failed to delete the problem!' + error, {icon: 'info'})
              })
          }
        })
    }
  }
}
</script>

<style lang="css" scoped>
/*.prevw {
  border: 0.1vw solid #ccc;
  border-radius: 1vw;
  max-height: 50vh;
  overflow-y: auto;
}*/
</style>
