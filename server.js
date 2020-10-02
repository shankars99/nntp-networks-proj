var express = require('express');
var routes  = require("./routes.js");
var swig = require("swig");
var bodyParser = require('body-parser');

const app = express();

app.engine('html', swig.renderFile);
app.set('view engine', 'html');
app.set('views', __dirname + '/views');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/views"));

routes(app);

app.listen(4000, () => {
    console.log('ok serving at..  ' + 4000);
});
