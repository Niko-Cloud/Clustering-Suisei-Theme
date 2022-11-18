/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/*.{html,js}"
  ],
  theme: {
    extend: {
      scale: {
        '-1': '-1'
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}
