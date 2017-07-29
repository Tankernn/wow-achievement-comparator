<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4 col-md-offset-2">
        <character @add-character="addCharacter"></character>
      </div>
      <div class="col-md-4">
        <achievement @add-achievement="addAchievement"></achievement>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <progress-table
            :characters="characters"
            :achievements="achievements"
        ></progress-table>
      </div>
    </div>
  </div>
</template>

<script>
import Character from './Character.vue'
import Achievement from './Achievement.vue'
import ProgressTable from './ProgressTable.vue'

export default {
  name: 'main',
  data () {
    return {
      characters: [],
      achievements: []
    }
  },
  methods: {
    addCharacter: function (character) {
      this.characters.push(character)
    },
    addAchievement: function (achievement) {
      this.achievements.push(achievement)
    }
  },
  components: {
    Character,
    Achievement,
    ProgressTable
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
