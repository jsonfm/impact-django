const colors = require('tailwindcss/colors');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html'
  ],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      black: colors.black,
      white: colors.white,
      gray: colors.gray,
      emerald: colors.emerald,
      indigo: colors.indigo,
      yellow: colors.yellow,
      pink: "#FFC4DD",
      "dark-gray": "#222022",
      dark: "#131313",
      blue: "#2C13DD"
    },
  },
  plugins: [],
}
