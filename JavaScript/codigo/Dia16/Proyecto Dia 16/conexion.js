const mysql = require('mysql2');
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'C0RONA2026',
    database: 'universidad'
});
connection.connect(function (error) {
    if (error) throw error;
    console.log('Conectado a la base de datos');
});

module.exports = { connection };