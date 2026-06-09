import { Component } from '@angular/core';

@Component({
  selector: 'app-saludador',
  imports: [],
  templateUrl: './saludador.html',
  styleUrl: './saludador.css',
})
export class Saludador {
  mensaje: string = '';//definimos mensaje
  saludar(){
    this.mensaje = "Hola Mundo";
  }
}
