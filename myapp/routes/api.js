var express = require('express');
var router = express.Router();

var {PythonShell} = require('python-shell');
var options = {
    pythonPath: '',
    scriptPath: '../core',
    args: [],
    encoding: 'utf8'
};

router.get('/:inputString', function(req, res) {
    var inputString = decodeURIComponent(req.params.inputString);
    options.args[0] = inputString;
    PythonShell.run('api.py', options, function(err, results) {
        if (err) throw err;
        var output = results[0].replace(`b\'`, '').replace(`\'`, '');
        output = Buffer.from(output, 'base64').toString('utf-8');
        res.status(200).json (
            {
                "result": output
            }
        );
    });
});

module.exports = router;
