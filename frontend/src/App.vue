<template>
  <div>
    <div class="page-container">
      <md-app md-mode="fixed">

        <md-app-toolbar class="md-toolbar main-header md-theme-default md-elevation-2 md-elevation-2">
          <span class="md-title">Atlantis</span>
        </md-app-toolbar>

        <md-app-content>
          <div id="app">
            <Main/>
          </div>
        </md-app-content>

      </md-app>
    </div>

    <Footer/>

  </div>
</template>

<style scoped>

  .md-toolbar {
    background-color: #1c2541;
  }

  .md-title {
    color: #6fffe9 !important;
  }

  .page-container {
    min-height: calc(100vh - 148px);
    font-family: 'Roboto Mono', monospace;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background-color: #e5e5e5;
    color: #0b132b;
  }

  #app {
    text-align: center;
    color: #0b132b;
  }

</style>

<script>
import Main from './components/Main'
import Footer from './components/Footer'

export default {
  name: 'App',
  components: {
    Main,
    Footer
  }
}
</script>
