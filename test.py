import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("카운트 업 프로그램")

# 폰트 설정
font = pygame.font.Font(None, 74)

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 카운트 초기값
count = 0

# 시간 관련 설정
clock = pygame.time.Clock()

# 카운트 업 플래그
counting = True
fps=pygame.time.Clock()
# 메인 루프
running = True
while running:
    clock.tick(60)
    m_x, m_y = pygame.mouse.get_pos()
    deltatime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 루프 종료로 게임 종료
        elif event.type == pygame.MOUSEBUTTONDOWN:
            counting = False  # 마우스 클릭하면 카운트업 멈춤

    if counting:
        # 카운트업
        count += deltatime *0.001

    # 화면 지우기
    screen.fill(WHITE)

    # 카운트 텍스트 생성
    count_text = font.render(f"{count:.2f}", True, BLACK)

    # 화면에 텍스트 그리기
    screen.blit(count_text, (screen.get_width() // 2 - count_text.get_width() // 2,
                             screen.get_height() // 2 - count_text.get_height() // 2))

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정 (초당 60프레임)
    clock.tick(60)

# Pygame 종료
pygame.quit()