<template>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Select achievement</h3>
    </div>
    <div class="panel-body">
      <form role="form" id="achievement">
        <div class="form-group">
          <div class="btn-group btn-group-justified">
            <typeahead placeholder="Search achievement..."
                      :async="apiEndpoint + '/search/'"
                      :template="template"
                      :on-hit="callback"
                      v-model="selectText">
            </typeahead>
          </div>
        </div>
        <button @click="addAchievement" class="btn btn-block btn-primary">Add</button>
      </form>
    </div>
  </div>
</template>

<script>
import { typeahead } from 'vue-strap'

export default {
  name: 'achievement',
  data () {
    return {
      achievements: [],
      selected: {},
      selectText: '',
      asynchronous: '{{item.title}}',
      template: '<img :src=\'"http://media.blizzard.com/wow/icons/18/" + item.icon + ".jpg"\' /> <span>{{item.title}}</span>'
    }
  },
  methods: {
    callback: function (item) {
      this.selected = item
      return item.title
    },
    addAchievement: function () {
      this.$emit('add-achievement', this.selected)
      this.selected = {}
      this.selectText = ''
    }
  },
  components: {
    typeahead
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
