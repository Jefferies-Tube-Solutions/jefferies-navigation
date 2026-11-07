// This namespace is independent of other dashboard resources.
if (window.jefferiesNavigation && window.jefferiesNavigation.apiVersion !== 2)
    throw new Error('Jefferies Navigation runtime namespace is occupied by an unknown API.');
window.jefferiesNavigation = window.jefferiesNavigation || {apiVersion: 2};

// Actual compiled module identity; ordinary release builds retain their version.
const build=require('./core/build-info');
window.jefferiesNavigation.version=build.version;
window.jefferiesNavigation.commit=build.commit;
