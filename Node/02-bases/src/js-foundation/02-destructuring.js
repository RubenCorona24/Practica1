//console.log(process.env)

//Desestructuramos objetos
const { TEMP, PUBLIC } = process.env
const characters = ['Flash', "Superman", 'Green Lantern', 'Batman']
const [, , , batman] = characters
//console.log("--------------------------------------------------")
//console.table({ TEMP, PUBLIC })