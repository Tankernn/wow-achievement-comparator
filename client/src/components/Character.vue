<template>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Add character</h3>
    </div>
    <div class="panel-body">
      <form role="form" id="character">
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
        <button class="btn btn-block btn-primary">Add <i class="fa fa-plus"></i></button>
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
      realm: {
        value: 'Neptulon',
        options: [
          'Neptulon',
          'Darksorrow',
          'Darkspear'
        ]
      },
      name: ''
    }
  },
  components: {
    vSelect
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
