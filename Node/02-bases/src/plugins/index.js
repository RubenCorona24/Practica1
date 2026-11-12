//Archivo de barril
const { getAge } = require('../plugins/get-age.plugin')
const { getUUID } = require('../plugins/get-id.plugin')

//exportamos las herramientas
module.exports = {
    getAge,
    getUUID
}