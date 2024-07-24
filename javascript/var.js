import { pedido } from "./pedido";

let bebida = prompt("¿Qué desea ordenar?");
pedido.bebida = bebida;
let cliente = prompt("¿Cuál es su nombre?");
pedido.cliente = cliente;

alert(`¡Gracias ${pedido.cliente}! En un momento le llamamos.`)

const cashier = 'Pedro 🦝';
alert(`¡Que tenga buen día! Le atendio ${cashier}`);