class heroi {
  constructor(classe, ataque){
    this.classe = classe
    this.ataque = ataque
  }
  atacar(){
    console.log(`O ${this.classe} atacou usando ${this.ataque}`)
  }
}

let guerreiro = new heroi("Guerreiro", "espada")
let mago = new heroi("Mago", "magia")
let monge = new heroi("Monge", "artes marciais")
let ninja = new heroi("Ninja", "shuriken")

guerreiro.atacar()
mago.atacar()
monge.atacar()
ninja.atacar()