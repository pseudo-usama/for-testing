/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'light-white-3': 'rgba(255, 255, 255, 0.3)',
        'light-white-4': 'rgba(255, 255, 255, 0.4)',
        'gray-1': 'rgba(100, 100, 100, 0.3)',
        'gray-2': '#C9C9CE',
        'gray-3': '#525479',
        'green-1': '#2FCB4F',
        'green-2': '#5DD25D',
        'yellow-1': '#F0D80C',
      }
    },
  },
  plugins: [],
}
