let isValid = false;


//sem ternário
function verify(isValid) {
    if(isValid) {
        return false
    }
    return true
};

//com ternário 

const result =  isValid ? true: false;

let zero = 0;

const numeroResultado = zero > 0 ? 0: -1;

//Funções

function soma(x, y) {
    return x + y;
};
const multiplicacao = function(x, y) {
    return x * y;
};

const dividir = (x, y) => {
    return x / y;
};