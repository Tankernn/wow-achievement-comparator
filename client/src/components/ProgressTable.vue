<template>
  <table class="table table-striped no-footer" role="grid" cellspacing="0">
    <thead>
      <tr role="row">
        <th>
          Character
        </th>
        <th>
          Progress
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          Example
        </td>
        <td>
          <progressbar now=10 label type="success"></progressbar>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { progressbar } from 'vue-strap'

export default {
  name: 'progress-table',
  data () {
    return {
      characters: [],
      achievements: []
    }
  },
  components: {
    progressbar
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
