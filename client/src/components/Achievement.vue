<template>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Select achievement</h3>
    </div>
    <div class="panel-body">
      <form role="form" id="achievement">
        <div class="form-group">
          <div class="btn-group btn-group-justified">
            <v-select placeholder="Nothing selected"
                      v-model="select.value"
                      :options="select.options"
                      options-value="id"
                      search justified required
                      close-on-select>
            </v-select>
          </div>
        </div>
        <button class="btn btn-block btn-primary">Add</button>
      </form>
    </div>
  </div>
</template>

<script>
import vSelect from 'vue-strap/src/Select.vue'

export default {
  name: 'achievement',
  data () {
    return {
      select: {
        value: '',
        options: [
          {id: 2, label: 'Explore...'}
        ]
      }
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
