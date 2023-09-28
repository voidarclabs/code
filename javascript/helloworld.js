var sql = require('mysql');

var con = sql.createConnection({
    host: '192.168.1.118',
    username: 'root',
    password: 'toor',
    database: 'ilham',
});

con.connect(function(err) {
    if (err) throw err;
    con.query('list databases', function (err, result, fields) {
        if (err) throw err;
        console.log(result)
    });
});