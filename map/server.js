const express = require('express')
const app = express()
const path = require('path');

app.get('/', (_, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
})

app.use(express.static('public'))

app.listen(process.env.PORT || 3000, () => {
    console.log(`Listening at http://localhost:${port}`)
})