/**
 * @Author: Sian Croser
 * @Date:   2020-04-27T05:25:15+09:30
 * @Email:  CQoute@gmail.com
 * @Filename: webpack.config.js
 * @Last modified by:   Sian Croser
 * @Last modified time: 2020-04-27T05:26:01+09:30
 * @License: GPL-3
 */
const path = require('path');
const webpack = require('webpack');
const build=require('./scripts/build-version').localMetadata(require('./package.json').version,{development:process.env.JTS_N_DEVELOPMENT_BUILD==='1'});

module.exports = {
    entry: './src/navigation-menu.js',
    plugins: [new webpack.BannerPlugin({banner: `Jefferies Navigation v${build.version}`}),
        new webpack.DefinePlugin({JTS_N_BUILD_VERSION:JSON.stringify(build.version),JTS_N_BUILD_COMMIT:JSON.stringify(build.commit)})],
    mode: 'production',
    output: {
        filename: 'jefferies-navigation.js',
        path: path.resolve(__dirname)
    }
};
