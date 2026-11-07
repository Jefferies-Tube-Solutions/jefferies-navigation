// Replaced by webpack, never inferred from the resource URL or HA version.
const version=typeof JTS_N_BUILD_VERSION === 'string' && JTS_N_BUILD_VERSION.trim()
    ? JTS_N_BUILD_VERSION : 'Version unavailable';
const commit=typeof JTS_N_BUILD_COMMIT === 'string' ? JTS_N_BUILD_COMMIT : null;
module.exports={version,commit};
