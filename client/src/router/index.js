import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import Main from '@/components/Main'

Vue.use(Router)
Vue.use(VueResource)

Vue.mixin({
  data: function () {
    return {
      get apiEndpoint () {
        return 'http://localhost:5000'
      }
    }
  }
})

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    }
  ]
})
