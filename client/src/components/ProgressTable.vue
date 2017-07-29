<template>
  <table class="table table-striped no-footer" role="grid" cellspacing="0">
    <thead>
      <tr role="row">
        <th>
          Character
        </th>
        <th v-for="achievement in achievements">
          {{achievement.title}}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="character in characters">
        <td>
          {{character.name}}
        </td>
        <td v-for="achievement in achievements">
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
  props: ['characters', 'achievements'],
  components: {
    progressbar
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
