package orientacao_objetos;

public class main {
    public static void main(String[] args) {

        Livro livro = new Livro();

        livro.nome = "Teste Linux";
        livro.descricao = "Livro sobre alguma coisa";
        livro.isbn = "9799898989898";
        livro.preco = 45.90;
        livro.autor = "Ney Backes";
        livro.dataPub = "03/05/2022";
        

        livro.dadosLivro();
        
    }
}
