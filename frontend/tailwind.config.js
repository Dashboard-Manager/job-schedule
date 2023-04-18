/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    colors: {
      'black-bg': '#12181b',
      'gray-dark': '#2a2e35',
      'gray-light': '#454e56',
      'white-text': '#fff',
      'secondary-text': '#88919e',
      bloody: '#e2243f',
      success: '#09c372',
    },
    fontFamily: {
      sans: ['Open Sans', 'sans-serif'],
    },
    extend: {
      backgroundImage: {
        user: 'url("https://svgshare.com/i/sAi.svg")',
      },
    },
  },
  plugins: [],
}
