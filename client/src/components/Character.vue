<template>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Add character</h3>
    </div>
    <div class="panel-body">
      <form role="form" id="character">
        <div class="form-group">
          <div class="btn-group btn-group-justified">
            <v-select placeholder="No region selected"
                      v-model="region.value"
                      :options="region.options"
                      value="value"
                      search justified required
                      close-on-select>
            </v-select>
          </div>
        </div>
        <div class="form-group">
          <div class="btn-group btn-group-justified">
            <v-select placeholder="No realm selected"
                      v-model="realm.value"
                      :options="realm.options"
                      search justified required
                      close-on-select>
            </v-select>
          </div>
        </div>
        <div class="form-group">
          <input class="form-control" placeholder="Character name" v-model="name" autofocus="" type="text">
        </div>
        <button @click="addCharacter" class="btn btn-block btn-primary">Add <i class="fa fa-plus"></i></button>
      </form>
    </div>
  </div>
</template>

<script>
import vSelect from 'vue-strap/src/Select.vue'

export default {
  name: 'character',
  data () {
    return {
      region: {
        value: 'eu',
        options: [
          {value: 'eu', label: 'Europe'},
          {value: 'us', label: 'United States'},
          {value: 'kr', label: 'Korea'},
          {value: 'tw', label: 'Taiwan'}
        ]
      },
      realm: {
        value: '',
        options: [
        ]
      },
      name: ''
    }
  },
  methods: {
    getData: function () {
      this.$http.get(this.apiEndpoint + '/realms/' + this.region.value)
        .then(response => {
          console.log(response)
          this.realm.options = response.body
        }, response => {
          console.error(response)
        })
    },
    addCharacter: function () {
      this.$http.get([this.apiEndpoint, 'character', this.region.value, this.realm.value, this.name].join('/'))
        .then(response => {
          var character = response.body
          character.region = this.region.value
          this.$emit('add-character', character)
        }, response => {
          console.error(response)
        })
    }
  },
  watch: {
    'region.value': function (oldVal, newVal) {
      this.getData()
    }
  },
  mounted: function () {
    this.getData()
  },
  components: {
    vSelect
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
