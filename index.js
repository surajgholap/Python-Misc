const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('How are you?');
});

app.listen(8080, () => {
    console.log('Listening on the port 8080');
});