import { Cliente } from './../cliente';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.css']
})
export class ClientesComponent implements OnInit {
  cliente:Cliente={
    nome:"",
    idade:0
  };
  clientes = [];

  addCliente(){
    let aux = Object.assign({} , this.cliente)
    this.clientes.push(aux)
  }
  
  constructor() { }

  ngOnInit() {
  }

}
