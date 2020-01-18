const express = require('express');
const app = express();
const port = 3000;
//include other libraries
require('./routes')(app);
require('./db')(app);

app.listen(port, (err) => {
  if (err){
    return console.log('Error: ', err)
  }
  console.log(`server is listening on ${port}`);
});