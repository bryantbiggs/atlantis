<template>
  <div class="main">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data () {
    return {
      msg: 'Welcome!'
    }
  }
}
</script>

<style scoped>
h1 {
  font-weight: normal;
}
</style>
