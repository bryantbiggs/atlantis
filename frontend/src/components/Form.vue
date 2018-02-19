<template>
  <div class="upload-form">
    <form enctype="multipart/form-data" class="md-layout">
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
            <md-file id="file-chooser" v-model="file" accept=".csv,.tsv" placeholder="Select *.tsv file" />
          </md-field>
        </md-card-content>

        <h3 v-if="uploading">...uploading</h3>

        <md-card-actions>
          <md-button type="submit" class="md-button md-raised" v-on:click="uploadFile">Upload</md-button>
        </md-card-actions>
      </md-card>

    </form>
  </div>
</template>

<script>
  import { s3 } from './aws_s3';
  export default {
    name: 'Form',
    data: () => ({
      file: null,
      uploading: false
    }),
    methods: {
      addFile() {
        // Upload file to S3
        const fileChooser = document.getElementById('file-chooser');
        if (!fileChooser.files.length) {
          return alert('Please choose a file to upload first.');
        }
        const file = fileChooser.files[0];
        const objKey = 'data/' + file.name;
        s3.upload({
          Key: objKey,
          Body: file,
          ACL: 'public-read'
        }, function(err, data) {
          if (err) {
            return alert('There was an error uploading your file: ', err.message);
          }
        });
      },
      // Reset file selection field
      clearForm () {
        this.file = null
      },
      uploadFile () {
        // Function triggered by button click event to perform upload steps
        this.uploading = true
        this.addFile()
        this.clearForm()
        this.uploading = false
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
