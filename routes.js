(function(){
    var homeHandler   = require('./handler/homeHandler');
	module.exports = function(app){
        app.all("/home",homeHandler);
    };
})();
