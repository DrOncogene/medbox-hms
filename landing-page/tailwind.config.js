/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
],
  theme: {
    extend: {
      colors: {
        'pri': '#256EFF',
        'sec': '#FE8344',
        'pri-dark': '#0F2F67',
      },
      backgroundColor: {
        'pri': '#256EFF',
        'pri-light': '#508CFE',
        'pri-trans': 'rgba(37, 110, 255, 0.5)',
        'sec': '#FE8344',
        'tert': '#EFF3F4',
        'milk': '#EFF3F4',
        'dark-blue': 'rgba(0, 14, 41, 0.9)'
      },
      borderColor: {
        'pri': '#256EFF',
        'sec': '#FE8344'
      }
    },
  },
  plugins: [],
}

