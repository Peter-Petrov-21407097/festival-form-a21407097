# festival

Descreva aqui as alterações/correções que fez

Os dias do festival passaram a ser apresentados por ordem cronológica (data crescente).
O formulário de concertos foi ajustado para permitir criar e editar todos os campos: banda, dia, hora e palco.
Foi implementada a funcionalidade para criação de novos concertos e este é feito através do menu.
Adicionada a possibilidade de eliminar concertos através de um pedido POST na rota concertos/<int:concerto_id>/apagar/.
O modelo Palco foi expandido com o campo booleano acessibilidade_mobilidade_reduzida.
A página de palcos foi editada de forma a poder mostrar:
capacidade
número total de concertos agendados
indicação de acessibilidade com o símbolo ♿
Foi criada a funcionalidade que permite editar os dados de cada palco.
Mais alterado no views as palavras (por exemplo, alterei o caminho para o caminho certo, nome de ficheiro correto)
Foi colocado as urls referentes a alteracoes com o nome de ficheiro e path correto, para se poder editar.
