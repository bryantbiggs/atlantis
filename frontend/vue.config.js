module.exports = {
  chainWebpack: config => {
    const imgRule = config.module.rule('images')
    imgRule.use('file-loader')
      .loader('image-webpack-loader')
      .tap(options => {
        const ret = options || {}
        ret.pngquant = {
          quality: '65-90',
          speed: 4
        }
        return ret;
      })
  }
}
