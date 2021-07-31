const express = require('express')
const app = express()


app.all('*', (req, res) => {
    res.send('Hello world!')
})


app.listen(process.env.PORT || 3000, () => console.info('Server started'))
