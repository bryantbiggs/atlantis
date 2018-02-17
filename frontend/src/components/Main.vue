<template>
  <div class="main">
    <h1>Welcome!</h1>
    <Form></Form>
  </div>
</template>

<script>
import Form from './Form.vue'
export default {
  components: {
    Form
  }
}
</script>

<style scoped>
h1 {
  font-weight: normal;
}
</style>
