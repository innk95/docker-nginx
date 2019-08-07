<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import Login from './components/Auth.vue'

export default {
  name: 'app',
  components: {
    'login': Login
  },
  created () {
    this.check()
  },
  methods: {
    check () {

    }
  }
}
</script>

<style>
</style>
