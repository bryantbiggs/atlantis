<template>
  <div class="upload-form">
    <form class="md-layout">
      <md-card class="md-layout-item md-size-50 md-small-size-100">
        <md-card-header>
          <div class="md-title">Upload Data</div>
        </md-card-header>

        <md-card-content>
          <ol>
            To upload data to the database:
            <li>Please select a local *.tsv using the field below</li>
            <li>Click the `Upload` button</li>
          </ol>

          <md-field class="md-field-upload">
            <label>Data file</label>
            <md-file v-model="file" placeholder="Select *.tsv file" />
          </md-field>

        </md-card-content>

        <md-card-actions>
          <md-button type="submit" class="md-button md-raised" v-on:click="uploadFile">Upload</md-button>
        </md-card-actions>
      </md-card>

    </form>
  </div>
</template>

<script>
  export default {
    name: 'Form',
    data: () => ({
      file: null,
      uploading: false
    }),
    methods: {
      clearForm () {
        this.file = null
      },
      uploadFile () {
        this.uploading = true
        window.setTimeout(() => {
          console.log("TIMEOUT DONE");
          this.uploading = false
          this.clearForm()
        }, 1500)
      }
    }
  }
</script>

<style scoped>

  ol {
    margin-bottom: 2em;
  }

  .md-field-upload {
    padding: 1em;
    background-color: #e5e5e5;
  }

  .md-layout {
    margin: 2em 0;
    padding: 1em;
    justify-content: center;
  }

  .md-layout-item {
    background-color: #ffffff;
  }

  .md-button {
    margin: 1em !important;
    color: #1c2541;
    background-color: #6fffe9;
  }

</style>
