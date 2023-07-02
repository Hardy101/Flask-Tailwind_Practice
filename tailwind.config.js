/** @type {import('tailwindcss').Config} */
module.exports = {
  mode:'jit',
   content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
     colors: {
        'regal-blue': '#243c5a',
        'sky-blue': '#87CEEB',
        'sec-blue': '#4FC0D0',
        'sand-beige': '#E6D5B8',
      },
    },
  },
  plugins: [],
}

