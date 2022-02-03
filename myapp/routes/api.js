var express = require('express');
var router = express.Router();

var {PythonShell} = require('python-shell');
var options = {
    pythonPath: '',
    scriptPath: '../core',
    args: []
};

router.get('/:inputString', function(req, res) {
    var inputString = req.params.inputString;
    options.args[0] = inputString;
    PythonShell.run('test.py', options, function(err, results) {
        if (err) throw err;
        res.status(200).json (
            {
                "result": results[0]
            }
        );
    });
});

module.exports = router;
