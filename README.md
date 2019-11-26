# Invasão Alienígena

 Na Invasão Alienígena, o jogador controla uma espaçonave que aparece na parte inferior central da tela. O jogador pode mover a espaçonave para a direita e para a esquerda usando as teclas de direção e atirar usando espaço. Quando o jogo começa, uma frota de alienígenas enche o céu e se desloca na tela para os lados e para baixo. O jogador atira nos alienígenas e os destrói. Se o jogador atingir todos os alienígenas, uma nova frota, que se moverá mais rapidamente que a frota anterior, aparecerá. Se algum alienígena atingir a espaçonave do jogador ou alcançar a parte inferior da tela, o jogador perderá uma nave. Se o jogador perder três espaçonaves, o jogo terminará.

# Seguindo o Python Crash Course

 O projeto esta sendo feito com o livro "Python Crash Course"  para que depois eu possa seguir sozinho fazendo minhas alterações.

# Para que serve cada arquivo?

    alien_invasion.py
 O arquivo principal alien_invasion cria vários objetos importantes usados no jogo: as configurações são armazenadas em ai_settings, a superfície principal de display é armazenada em screen e uma instância de ship é criada nesse arquivo. Também em alien_invasion.py está o laço principal do jogo: um laço while que chama check_events(), ship.update() e update_screen().
 alien_invasion.py é o único arquivo que deve ser executado quando você quiser jogar Invasão Alienígena. Os outros arquivos - settings.py, game_functions.py, ship.py - contêm códigos que são importados, de forma direta ou não, nesse arquivo.

    settings.py
 O arquivo settings.py contém a classe Settings. Essa classe tem apenas um método _init__(), que inicializa os atributos para controlar a aparência do jogo e a velocidade da espaçonave.

    game_functions.py
 O arquivo game_functions.py contém várias funções que executam a maior parte das tarefas do jogo. A função check_events() detecta eventos relevantes, como pressionamentos e solturas de teclas, além de processar cada um desses tipos de evento por meio das funções auxiliares check_keydown_events() e check_keyup_events(). Por enquanto, essas funções administram o movimento da espaçonave. O módulo game_functions também contém update_screen(), que redesenha a tela a cada passagem pelo laço principal.

    ship.py
 O arquivo ship.py contém a classe Ship. A classe Ship tem um método _init__(), um método update() para administrar a posição da espaçonave e um método blitme() para desenhar a espaçonave na tela. A imagem propriamente dita da espaçonave está armazenada em ship.bmp, que está na pasta images.

# O laço principal do jogo:

     while True:
            gf.check_events(ai_settings, screen, ship, bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(ai_settings, screen, ship, bullets)

onde:

    gf.check_events()
 Verifica se a entradas do jogador.

    ship.update()
 Atualiza a posição da espaçonave.

    gf.update_bullets()
 Atualiza a posição dos projéteis disparados.

    gr.update_screen()
 Usa as posições atualizadas pelos métodos 'ship_updates()' e 'gf.update_bullets()' para desenhar uma nova tela.

# Atualizações

sex 22 nov -> Criação de uma janela com o pygame e que leia o teclado, criação do módulo 'settings' onde é definido tamanho e cor da tela, criação do módulo 'ship' que adiciona a imagem da nave e suas ações.

sab 23 nov -> Refatoração do código com a criação do módulo 'game_functions' na qual armazenará várias funções que farão o jogo executar deixando o código main (alien_invasion.py) mais fácil de entender.

dom 24 nov -> Foi adicionado a 'game_functions.py' instruções para responder a eventos de pressionamento de teclas, adicionado flags no módulo 'ship.py' para movimento continua quando a tecla for pressionada e atualizado o laço do código principal 'alien_invasion.py' para rodar a resposta dos eventos.

seg 25 nov ->  Foi adicionado em settings uma váriavel para controle de velocidade da nave, alteração no modulo 'ship.py' para que rect reconheça o valor como float, adicionado o parâmetro 'ai_settings' para a váriavel ship no código principal para a alteração da velocidade, assim fica mais fácil fazer alteração da velocidade da nave quando for necessário. Foi feita uma modificação no método 'update()' em 'ship.py' para que a espaçonave pare o movimento ao alcançar a borda da tela. Foi feita uma refatoração na função 'check_events()' em 'game_functions.py' que foi dividida em mais duas outras funções, uma para responder quando as teclas forem pressionadas e outra para reconhecer quando as teclas forem soltas, foi refatorado pois a função 'check_events()' ficará muito grande ao decorrer do desenvolvimento. Foi criado um novo módulo, 'bullet.py' contém a classe 'Bullet()' que administrará projéteis disparados pela espaçonave. Criado em 'bullet.py' o método 'update()' que administra a posição do projétil e o método 'draw_bullet()' para desenhar um projétil. Os projéteis foram armazenados em um grupo chamado 'bullets', o grupo foi feito para desenhar os projéteis na tela a cada passada pelo laço principal e atualizar a posição de cada projétil e por último 'check_keydown_events()' em 'game_functions.py' foi modificado para que o projétil seja disparado ao pressionar a tecla espaço.

ter 26 nov -> Foi feito um laço for em 'alien_invasion.py' para apagar projéteis que saiam da tela para liberar espaço na mémoria. Foi feita uma modificação em 'settings.py' e 'game_functions.py' para limitar o número de projéteis disparados em 3.Foi feita mais uma refatoração onde a ação de atualizar os projéteis na tela foram apagadas de 'alien_invasion.py' para que o código while fique mais simples e foram passadas para uma nova função em 'game_functions.py' chamada 'update_bullets()'.
