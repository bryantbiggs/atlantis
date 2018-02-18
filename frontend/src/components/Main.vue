<template>
  <div class="main">
    <h1>Welcome!</h1>
    <Form/>
  </div>
</template>

<script>
import Form from './Form'
export default {
  name: 'Main',
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
