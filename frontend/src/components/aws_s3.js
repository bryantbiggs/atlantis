const bucketName = 'theatlantis.xyz'
const bucketRegion = 'us-east-1'
const IdentityPoolId = 'us-east-1:0024c677-f796-4019-9d39-424c955a3e8c'
let AWS = require('aws-sdk')

AWS.config.update({
  region: bucketRegion,
  credentials: new AWS.CognitoIdentityCredentials({
    IdentityPoolId: IdentityPoolId
  })
})

export let s3 = new AWS.S3({
  apiVersion: '2006-03-01',
  params: {
    Bucket: bucketName
  }
})
