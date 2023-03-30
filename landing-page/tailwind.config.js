/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
],
  theme: {
    extend: {
      colors: {
        'pri': '#256EFF'
      },
      backgroundColor: {
        'pri': '#256EFF',
        'pri-light': '#508CFE',
        'pri-trans': 'rgba(37, 110, 255, 0.9)',
        'sec': '#FE8344',
        'tert': '#EFF3F4'
      },
      borderColor: {
        'pri': '#256EFF',
        'sec': '#FE8344'
      }
    },
  },
  plugins: [],
}

