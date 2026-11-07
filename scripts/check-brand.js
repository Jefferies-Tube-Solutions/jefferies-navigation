'use strict';

const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

const repository = 'Jefferies-Tube-Solutions/jefferies-navigation';
const whiteLockup = 'assets/brand/navigation-lockup-white.png';
const deepSpaceLockup = 'assets/brand/navigation-lockup-deep-space.png';
const backgroundLockup = 'assets/brand/navigation-lockup-background.png';
const artwork = Object.freeze({
    [backgroundLockup]: 'ecb31199fd5cb1d6972da0fc2aacdf379361c3e853706eb8a65957b38979eb89',
    [whiteLockup]: 'd6ecf4c931250da855f4b051df9003a5c0fe6a975631494d6d67ec1fc9857f08',
    [deepSpaceLockup]: 'f19e85d9886b44e57a634b7d5eae9cec96f9e856bc078eef799f28086747e451',
    'assets/navigation-compass.png': '793f2f612bf899de6847b497719d51a9ac7ef38c7f8b6bbe7517e717c7257040'
});

function readBrand() {
    const read = file => fs.readFileSync(path.join(__dirname, '..', file));
    return {
        package: JSON.parse(read('package.json')),
        hacs: JSON.parse(read('hacs.json')),
        release: JSON.parse(read('release.json')),
        runtime: read('src/runtime.js').toString('utf8'),
        readme: read('README.md').toString('utf8'),
        artwork: Object.fromEntries(Object.keys(artwork).map(file => [
            file, crypto.createHash('sha256').update(read(file)).digest('hex')
        ]))
    };
}

function validateBrand(brand) {
    assert.equal(brand.package.name, 'jefferies-navigation', 'Unexpected package identity');
    assert.equal(brand.package.repository.url, 'git+https://github.com/' + repository + '.git', 'Unexpected repository identity');
    assert.equal(brand.hacs.name, 'JTS - Jefferies Navigation', 'Unexpected HACS name');
    assert.equal(brand.hacs.filename, 'jefferies-navigation.js', 'Unexpected HACS bundle name');
    const title = 'Jefferies Navigation v' + brand.package.version;
    assert.ok(brand.release.title === title || brand.release.title.startsWith(title + ' — '), 'Unexpected release identity');
    assert.match(brand.runtime, /window\.jefferiesNavigation\s*=/, 'Unexpected runtime identity');

    for (const [file, hash] of Object.entries(artwork)) {
        assert.equal(brand.artwork[file], hash, 'Unapproved artwork bytes for ' + file);
    }

    const heading = '\n# Jefferies Navigation for Home Assistant';
    const titleIndex = brand.readme.indexOf(heading);
    assert.ok(titleIndex > 0, 'README product heading missing');
    const header = brand.readme.slice(0, titleIndex).replace(/\r\n/g, '\n').trimEnd();
    assert.equal(header, [
        '<p align="right">',
        `  <a href="https://github.com/${repository}/releases/latest">`,
        `    <img alt="Latest stable version" src="https://img.shields.io/github/v/release/${repository}?label=stable&amp;color=2ea44f">`,
        '  </a>',
        '</p>',
        '',
        '<p align="center">',
        `  <img src="${backgroundLockup}" alt="Jefferies Navigation full logo on Deep Space" width="760">`,
        '</p>'
    ].join('\n'), 'README header must use one approved Deep Space Navigation lockup below the status badge');
    const sections = [
        'Mission Directive', 'System Registry', 'Commissioning', 'Operational Protocol',
        'Verification', 'Fault Isolation and Recovery', 'Manuals', 'Operations Log', 'Approved artwork'
    ];
    const actualSections = [...brand.readme.matchAll(/^## (.+)$/gm)].map(match => match[1].trim());
    assert.deepEqual(actualSections, sections, 'README must follow the JTS product section order');
    for (const type of ['navigation-hub', 'navigation-control']) {
        assert.match(brand.readme, new RegExp('^type: custom:' + type + '$', 'm'),
            'README example must use custom:' + type);
    }
    assert.match(brand.readme, /\[.*\]\(docs\/AI_SETUP\.md\)/, 'README must link the AI setup guide');
    assert.match(brand.readme, /\]\(docs\/CAPTAINS_LOG\.md\)/, 'README must link the Captain’s Log');
    assert.doesNotMatch(brand.readme,
        /^#{2,6} (?:Floorplan sizing in v1\.8\.0-beta\.6|v1\.8\.0-beta\.[67]:|Anchored child menus \(v1\.9\.0-beta\.4\))/m,
        'Historical release headings belong in the Captain’s Log');
}

module.exports = {readBrand, validateBrand};

if (require.main === module) {
    validateBrand(readBrand());
    console.log('JTS-N artwork and product identity verified.');
}
