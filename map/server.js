const express = require('express')
const app = express()
const path = require('path');
const port = process.env.PORT || 3000

app.get('/', (_, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
})

app.use(express.static('public'))

app.listen(port, () => {
    console.log(`Listening at port ${port}`)
})