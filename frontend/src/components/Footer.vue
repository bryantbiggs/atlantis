<template>
  <footer class="main-footer">

    <div class="container-wrapper md-layout-row">
      <md-button class="md-raised" href="http://github.com/bryantbiggs/atlantis" target="_blank">Atlantis</md-button>
      <md-button class="md-raised" href="http://github.com/bryantbiggs" target="_blank">Github</md-button>
      <md-button class="md-raised" href="https://www.linkedin.com/in/bryantbiggs/" target="_blank">LinkedIn</md-button>
    </div>

    <div class="container-wrapper md-layout-row">
      <p>All rights reserved Bryant Biggs 2018</p>
    </div>

  </footer>
</template>


<style scoped>
  footer {
    height: 132px;
    padding: 2em;
    position: relative;
    color: #0b132b;
    background-color: #fff;
    font-family: 'Roboto Mono', monospace;
  }

  .md-layout-row {
    text-align: center;
  }

  .md-raised {
    color: #0b132b;
  }
  
</style>

<script>
export default {
  name: 'Footer'
}
</script>
