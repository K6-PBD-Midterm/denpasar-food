module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js',
      './restaurants/**/*.html',
      './navigation/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
]
}