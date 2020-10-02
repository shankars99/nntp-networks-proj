const express     = require('express');
const bodyParser  = require('body-parser');
const fs          = require('fs');
const home        = express.Router();

//using body parser to read values of fields(such as field name) in webpages
home.use(bodyParser.json());

//Displays homepage
home.route('/home')
.get( (req, res, next) => {
    res.statusCode = 200;
    console.log("displaying home page");

    var output = {"links" : [1,2,3,4,5] };

    res.render("index.html",output);
}).
post((req,res,next) => {
    res.statusCode = 200;
    console.log("displaying article number:" + req.body.number);
    res.setHeader('Content-Type', 'text/html');
    res.end("howdy there you clicked link " + req.body.number);
    //res.render("index.html",output);
})

module.exports = home;
