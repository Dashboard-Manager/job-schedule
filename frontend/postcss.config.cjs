/** @type {import('postcss-load-config').Config} */

module.exports = {
    plugins: [
        require('postcss-nested'),
        require('tailwindcss'),
        require('postcss-flexbugs-fixes'),
        require('postcss-preset-env'),
    ],
};
