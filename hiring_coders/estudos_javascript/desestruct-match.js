const pessoa = {
    nome: 'Ney',
    sobrenome: 'Backes',
    idade: 29,
    profissao: 'Estagiário de Testes Front-end'

};

//let nome = pessoa.nome;
//let sobrenome = pessoa.sobrenome;
//let idade = pessoa.idade;
//let profissao = pessoa.profissao;


//variável objeto

let {nome ,sobrenome, idade, profissao} = pessoa;



//match

const cpf = "Meu cpf é 123.456.789-11";

const regex = new RegExp('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}');


console.log(cpf.match(regex));