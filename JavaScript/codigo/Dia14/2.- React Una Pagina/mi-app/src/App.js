import React from 'react';
import Saludo from './saludo' //importamos saludo
import Mensaje from './mensaje';
function App(){
  return (
    <div>
      <Saludo nombre="Pedro"/>
      <Mensaje mensaje="Bienvenido a esta página React"/>
    </div>
  )
}
export default App;