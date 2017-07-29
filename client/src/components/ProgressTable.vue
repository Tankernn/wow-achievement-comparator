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
        <td style="font-weight: bold;" :style="{ color: classColors[character.class] }">
          <a target="_blank" :href="'https://worldofwarcraft.com/' + languages[character.region] + '/character/' + character.realm + '/' + character.name">
            <img height="18" width="18" :src="'http://render-api-' + character.region + '.worldofwarcraft.com/static-render/' + character.region + '/' + character.thumbnail" />
            {{character.name}}
          </a>
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
  data () {
    return {
      classColors: {
        1: '#C79C6E',
        2: '#F58CBA',
        3: '#ABD473',
        4: '#FFF569',
        5: '#000000',
        6: '#C41F3B',
        7: '#0070DE',
        8: '#69CCF0',
        9: '#9482C9',
        10: '#00FF96',
        11: '#FF7D0A',
        12: '#A330C9'
      },
      languages: {
        'us': 'en-us',
        'eu': 'en-gb',
        'kr': 'ko-kr',
        'tw': 'zh-tw'
      }
    }
  },
  props: ['characters', 'achievements'],
  components: {
    progressbar
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
