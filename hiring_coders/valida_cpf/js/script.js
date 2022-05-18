console.log("Javascript carregado");

function validaCPF(cpf) {       
    if (cpf.length != 11){
        return false;
    } else {

        var numeros = cpf.substring(0, 9);
        var digitos = cpf.substring(9);

        var soma = 0 

        for (var i = 10; i > 1; i--) {

          soma += numeros.charAt(10 - i) * i;

        }
        console.log(soma);

        var resultado = soma % 11 < 2 ? 0 : 11 - (soma % 11);

        if(resultado != digitos.charAt(0)) {
            return false;
        }
        soma = 0;

        numeros = cpf.substring(0,10);

        for(var k = 11; k > 1; k--){
          soma += numeros.charAt(11-k)*k;
        }

        resultado = soma % 11 < 2 ? 0: 11 - (soma % 11);

        if(resultado != digitos.charAt(1)) {            
            return false;
            
        }
        
        console.log(soma)
        return true;
    }
   
}
function validacao() {

    console.log("Iniciando validação do CPF ");
    console.log("Funcionou"); 
    

    var cpf = document.getElementById("cpf_digitado").value;
    var nome = document.getElementById("nome").value;

    var resultadovalidacao = validaCPF(cpf);  
    
    if (resultadovalidacao) {        
        alert(`Olá, ${nome} o CPF informado de número: ${cpf} é válido`);
        c
        
    } else {
        alert(`Olá, ${nome} o CPF informado de número: ${cpf} é inválido`);
    
    }   
      

    }
    
  

