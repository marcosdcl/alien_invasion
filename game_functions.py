import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Responde a solturas de teclas."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, alien, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza a posição dos projéteis
    bullets.update()

    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
