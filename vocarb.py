import pygame
import sys
import random
pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
FPS = 20
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ADD_NEW_CHARACTER_RATE = 25

# Load images
cactus_img = pygame.image.load('assets/cactus_bricks.png')
cactus_img_rect = cactus_img.get_rect()
cactus_img_rect.left = 0

fire_img = pygame.image.load('assets/fire_bricks.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0

# Load background images
background_img = pygame.image.load('assets/background.png')
background_rect = background_img.get_rect()
winner_img = pygame.image.load('assets/winer.png')
winner_rect = winner_img.get_rect()

# Load font
font_path = 'assets/NotoSansJP-Regular.ttf'
font_size = 20
font = pygame.font.Font(font_path, font_size)

# Initialize Pygame clock
CLOCK = pygame.time.Clock()

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Mario Learn Japanese')

class Topscore:
    def __init__(self):
        self.high_score = 0

    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

topscore = Topscore()

class Dragon:
    dragon_velocity = 10
    fireball_rate = 40  # Higher value means fewer fireballs

    def __init__(self):
        self.dragon_img = pygame.image.load('assets/dragon.png')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = WINDOW_HEIGHT / 2
        self.dragon_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False
        self.fireball_counter = 0

    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velocity

        self.fireball_counter += 1
        if self.fireball_counter >= self.fireball_rate:
            self.fireball_counter = 0
            return Fireball(self.dragon_img_rect.midleft)
        return None

class Fireball:
    fireball_velocity = 7

    def __init__(self, position):
        self.fireball_img = pygame.image.load('assets/fireball.png')
        self.fireball_img_rect = self.fireball_img.get_rect()
        self.fireball_img_rect.midleft = position

    def update(self):
        self.fireball_img_rect.left -= self.fireball_velocity
        canvas.blit(self.fireball_img, self.fireball_img_rect)

    def is_off_screen(self):
        return self.fireball_img_rect.right < 0

class Mario:
    velocity = 5  # Reduced movement speed

    def __init__(self):
        self.mario_img = pygame.image.load('assets/maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = WINDOW_HEIGHT / 2 - 100
        self.down = False
        self.up = False
        self.mario_score = 0

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top <= cactus_img_rect.bottom:
            game_over()
        if self.mario_img_rect.bottom >= fire_img_rect.top:
            game_over()
        if self.up:
            self.mario_img_rect.top -= self.velocity
        if self.down:
            self.mario_img_rect.bottom += self.velocity

class JapaneseCharacter:
    vocarb_JPD113 = [
        ('わたし', 'Tôi'), ('おなまえ', 'Tên (bạn)'), ('おくに', 'Đất nước (bạn)'),
        ('にほん', 'Nhật Bản'), ('かんこく', 'Hàn Quốc'), ('ちゅうごく', 'Trung Quốc'),
        ('アメリカ', 'Mỹ'), ('イタリア', 'Ý'), ('オーストラリア', 'Úc'),
        ('ロシア', 'Nga'), ('タイ', 'Thái Lan'), ('こうこう', 'Trường trung học phổ thông (cấp 3)'),
        ('だいがく', 'Trường đại học'), ('にほんごがっこう', 'Trường tiếng Nhật'),
        ('おしごと', 'Công việc (của bạn)'), ('がくせい', 'Học sinh'),
        ('せんせい', 'Thầy/Cô giáo'), ('きょうし', 'Giáo viên'), ('かいしゃいん', 'Nhân viên văn phòng'),
        ('しゃいん', 'Nhân viên (của công ty nào đó)'), ('さん', 'Anh/Chị/Ông/Bà/Bạn 〜'),
        ('じん', 'Người (nước nào)'), ('ご', 'Tiếng (nước nào)'), ('どちら', 'Ở đâu / Phía nào'),
        ('たんじょうび', 'Ngày sinh / Sinh nhật'), ('ブラジル', 'Brazil'), ('しゅみ', 'Sở thích'),
        ('スポーツ', 'Thể thao'), ('サッカー', 'Bóng đá'), ('テニス', 'Tennis (Quần vợt)'),
        ('すいえい', 'Bơi lội'), ('おんがく', 'Âm nhạc'), ('どくしょ', 'Đọc sách'),
        ('りょこう', 'Du lịch'), ('りょうり', 'Nấu ăn / Món ăn'), ('なに', 'Cái gì')
    ]

    vocarb_JPD123 = [
        ('きた', 'Phía bắc'), ('みなみ', 'Phía nam'), ('ひがし', 'Phía đông'),
        ('にし', 'Phía tây'), ('まんなか', 'Chính giữa'), ('くるま', 'Ô tô'),
        ('しんかんせん', 'Tàu cao tốc Shinkansen'), ('でんしゃ', 'Tàu điện'), ('ひこうき', 'Máy bay'),
        ('えき', 'Nhà ga'), ('まち', 'Thành phố, thị trấn'), ('じかん', 'Tiếng'),
        ('じかんはん', 'Tiếng rưỡi'), ('ふん', 'Phút'), ('あるいて', 'Đi bộ'),
        ('くらい', 'Khoảng'), ('どのくらい', 'Bao lâu'), ('おんせん', 'Suối nước nóng'),
        ('かわ', 'Sông'), ('やま', 'Núi'), ('きょうかい', 'Nhà thờ'),
        ('おしろ', 'Lâu đài'), ('じんじゃ', 'Đền'), ('おてら', 'Chùa'),
        ('ビル', 'Tòa nhà'), ('ところ', 'Nơi, chỗ'), ('ひと', 'Người'),
        ('みどり', 'Màu xanh; Cây xanh'), ('あります', 'Có'), ('あたらしい', 'Mới'),
        ('ふるい', 'Cũ'), ('いい', 'Tốt'), ('おおい', 'Nhiều 〜'),
        ('すくない', 'Ít 〜'), ('おおきい', 'To, lớn'), ('ちいさい', 'Nhỏ, bé'),
        ('たかい', 'Cao, đắt'), ('ひくい', 'Thấp'), ('きれい（な）', 'Đẹp, sạch sẽ'),
        ('しずか（な）', 'Yên tĩnh'), ('にぎやか（な）', 'Náo nhiệt, nhộn nhịp'), ('ゆうめい（な）', 'Nổi tiếng'),
        ('どんな', 'Như thế nào'), ('そして', 'Và'), ('あめ', 'Mưa'),
        ('ゆき', 'Tuyết'), ('ひ', 'Ngày / Mặt trời'), ('メロン', 'Dưa gang (dưa lưới)'),
        ('あたたかい', 'Ấm áp (thời tiết)'), ('すずしい', 'Mát mẻ'), ('あつい', 'Nóng bức (thời tiết)'),
        ('さむい', 'Lạnh, rét (thời tiết)'), ('てんきがいい', 'Thời tiết đẹp'), ('てんきがわるい', 'Thời tiết xấu'),
        ('あたたかい', 'Ấm (nhiệt độ, cảm giác)'), ('あつい', 'Nóng (nhiệt độ)'), ('つめたい', 'Lạnh / Mát (nhiệt độ, cảm giác)'),
        ('おいしい', 'Ngon'), ('あまい', 'Ngọt'), ('からい', 'Cay'),
        ('にがい', 'Đắng'), ('すっぱい', 'Chua'), ('いちねんじゅう', 'Suốt 1 năm'),
        ('あまり', 'Không 〜 lắm'), ('すこし', 'Một chút, ít'), ('とても', 'Rất'),
        ('どう', 'Thế nào'), ('そうですね。', 'Câu nói thể hiện sự đồng tình với ý kiến của người khác')
    ]

def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('assets/mariodie.wav')
    music.play()
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load('assets/end.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100)
    canvas.blit(game_over_img, game_over_img_rect)

    play_again_text = font.render("Press 'R' to Restart or 'M' for Main Menu", True, (255,0,0))
    play_again_text = pygame.transform.scale(play_again_text, (600, 50))
    play_again_rect = play_again_text.get_rect()
    play_again_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50)
    canvas.blit(play_again_text, play_again_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    music.stop()
                    game_loop(current_set)
                if event.key == pygame.K_m:
                    music.stop()
                    start_game()
        pygame.display.update()

def display_menu():
    menu_running = True
    selected_set = None

    # Load font cho dòng chữ mới
    team_text = font.render("Developed By Team: Sao Băng Tự Do", True, (255,255,255))  # Đổi màu chữ thành màu trắng
    team_text = pygame.transform.scale(team_text, (300, 50))
    team_text_rect = team_text.get_rect()
    team_text_rect.topright = (WINDOW_WIDTH - 20, 20)  # Đặt góc trên bên phải

    while menu_running:
        canvas.blit(background_img, background_rect)  # Hiển thị hình nền
        # Vẽ dòng chữ của team ở góc trên bên phải
        canvas.blit(team_text, team_text_rect)

        # Vẽ các tùy chọn menu ở đây
        menu_text = font.render("Chọn một set từ:", True, (0, 0, 0))  # Đổi màu chữ thành màu đen
        menu_text = pygame.transform.scale(menu_text, (400, 50))  # Thay đổi kích thước chữ
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = (WINDOW_WIDTH / 2, 100)
        canvas.blit(menu_text, menu_text_rect)

        # Danh sách các set từ
        set_options = ["Từ vựng tiếng Nhật", "Vocarb JPD113", "Vocarb JPD123"]
        for index, option in enumerate(set_options):
            option_text = font.render(option, True, (255, 0, 255))  # Đổi màu chữ thành màu đỏ 
            option_text = pygame.transform.scale(option_text, (300, 50))  # Thay đổi kích thước chữ
            option_text_rect = option_text.get_rect()
            option_text_rect.center = (WINDOW_WIDTH / 2, 200 + index * 50)
            canvas.blit(option_text, option_text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Kiểm tra xem người chơi nhấp vào tùy chọn nào
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for index, option in enumerate(set_options):
                    option_text_rect = font.render(option, True, (255, 0, 0)).get_rect()  # Đổi màu chữ thành màu đỏ 
                    option_text_rect.center = (WINDOW_WIDTH / 2, 200 + index * 50)
                    if option_text_rect.collidepoint(mouse_x, mouse_y):
                        selected_set = option
                        menu_running = False

    return selected_set

def waiting_screen():
    # Tải hình ảnh nền
    background_img = pygame.image.load('assets/background.png')
    background_rect = background_img.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return  # Kết thúc hàm và quay lại game_loop()

        # Vẽ hình ảnh nền lên màn hình
        canvas.blit(background_img, background_rect)

        # Vẽ văn bản trên màn hình
        waiting_text = font.render("Nhấn phím bất kỳ để bắt đầu game", True, (255, 0, 255))
        waiting_text = pygame.transform.scale(waiting_text, (600, 50))
        waiting_text_rect = waiting_text.get_rect()
        waiting_text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        canvas.blit(waiting_text, waiting_text_rect)

        pygame.display.update()

def start_game():
    selected_set = display_menu()  # Chọn một trong các set từ
    waiting_screen()  # Gọi màn hình chờ
    canvas.fill(BLACK)
    start_img = pygame.image.load('assets/start.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    canvas.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop(selected_set)

def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 10):
        cactus_img_rect.bottom = 50
        fire_img_rect.top = WINDOW_HEIGHT - 50
        LEVEL = 1
    elif SCORE in range(10, 20):
        cactus_img_rect.bottom = 100
        fire_img_rect.top = WINDOW_HEIGHT - 100
        LEVEL = 2
    elif SCORE in range(20,30):
        cactus_img_rect.bottom = 150
        fire_img_rect.top = WINDOW_HEIGHT - 150
        LEVEL = 3
    elif SCORE in range(30, 40):
        cactus_img_rect.bottom = 200
        fire_img_rect.top = WINDOW_HEIGHT - 200
        LEVEL = 4
    elif SCORE > 40:
        cactus_img_rect.bottom = 250
        fire_img_rect.top = WINDOW_HEIGHT - 250
        LEVEL = 'Final'

def congratulations_screen():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('assets/mario_win.mp3')
    music.play()
    winner_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    canvas.blit(winner_img, winner_rect)

    congrats_text = font.render("Press 'M' for Main Menu or 'Q' to Quit", True, (255, 0, 0))  # Đổi màu chữ thành màu đỏ 
    congrats_text = pygame.transform.scale(congrats_text, (600, 50))  # Thay đổi kích thước chữ
    congrats_rect = congrats_text.get_rect()
    congrats_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100)
    canvas.blit(congrats_text, congrats_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    music.stop()
                    start_game()
        pygame.display.update()

def game_loop(selected_set):
    global dragon
    global current_set
    current_set = selected_set
    if selected_set == "Vocarb JPD113":
        character_set = JapaneseCharacter.vocarb_JPD113
    elif selected_set == "Vocarb JPD123":
        character_set = JapaneseCharacter.vocarb_JPD123
    else:
        character_set = JapaneseCharacter.vocarb_JPD113  # Default set

    dragon = Dragon()
    fireballs = []
    mario = Mario()
    global SCORE
    SCORE = 0
    global LEVEL
    LEVEL = 1

    pygame.mixer.music.load('assets/mario_theme.mp3')
    pygame.mixer.music.play(-1, 0.0)

    # Hàm tạo các nghĩa ngẫu nhiên, trong đó có một nghĩa đúng
    def generate_random_meanings(correct_pair, all_pairs, num_options=4):
        meanings = [correct_pair]
        while len(meanings) < num_options:
            random_pair = random.choice(all_pairs)
            if random_pair not in meanings:
                meanings.append(random_pair)
        random.shuffle(meanings)
        return meanings

    all_pairs = character_set
    correct_pair = ()
    displayed_meanings = []
    current_input = ""
    hint_count = 0
    max_hints = 5

    while True:
        canvas.fill(BLACK)
        check_level(SCORE)
        new_fireball = dragon.update()
        if new_fireball:
            fireballs.append(new_fireball)

        fireballs = [fireball for fireball in fireballs if not fireball.is_off_screen()]
        
        for fireball in fireballs:
            fireball.update()

        if not displayed_meanings:  # Nếu không còn nghĩa nào, tạo nghĩa mới
            correct_pair = random.choice(all_pairs)
            displayed_meanings = generate_random_meanings(correct_pair, all_pairs)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mario.up = True
                    mario.down = False
                elif event.key == pygame.K_DOWN:
                    mario.down = True
                    mario.up = False
                elif event.key == pygame.K_BACKSPACE:
                    current_input = current_input[:-1]
                elif event.unicode.isdigit():
                    current_input += event.unicode
                    selected_index = int(event.unicode) - 1
                    if 0 <= selected_index < len(displayed_meanings) and displayed_meanings[selected_index] == correct_pair:
                        SCORE += 1
                        displayed_meanings = []
                        current_input = ""
                elif event.key == pygame.K_h and hint_count < max_hints:
                    hint_count += 1
                    current_input = str(displayed_meanings.index(correct_pair) + 1)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    mario.up = False
                elif event.key == pygame.K_DOWN:
                    mario.down = False

        for fireball in fireballs:
            if fireball.fireball_img_rect.colliderect(mario.mario_img_rect):
                game_over()

        score_font = font.render('Score:' + str(SCORE), True, GREEN)
        score_font_rect = score_font.get_rect()
        score_font_rect.center = (200, cactus_img_rect.bottom + score_font_rect.height / 2)
        canvas.blit(score_font, score_font_rect)

        level_font = font.render('Level:' + str(LEVEL), True, GREEN)
        level_font_rect = level_font.get_rect()
        level_font_rect.center = (400, cactus_img_rect.bottom + score_font_rect.height / 2)
        canvas.blit(level_font, level_font_rect)

        vocarb_font = font.render('Vocarb: ' + correct_pair[0], True, GREEN)
        vocarb_font_rect = vocarb_font.get_rect()
        vocarb_font_rect.center = (800, cactus_img_rect.bottom + score_font_rect.height / 2)
        canvas.blit(vocarb_font, vocarb_font_rect)

        if displayed_meanings:  # Hiển thị các nghĩa ngẫu nhiên
            for i, pair in enumerate(displayed_meanings):
                meaning_font = font.render(f'{i+1}: {pair[1]}', True, GREEN)
                meaning_font_rect = meaning_font.get_rect()
                meaning_font_rect.left = 20
                meaning_font_rect.top = 400 + i * 30
                canvas.blit(meaning_font, meaning_font_rect)

        input_font = font.render('Input: ' + current_input, True, GREEN)
        input_font_rect = input_font.get_rect()
        input_font_rect.center = (WINDOW_WIDTH / 2, fire_img_rect.top - 50)
        canvas.blit(input_font, input_font_rect)

        hint_font = font.render('Hints used: ' + str(hint_count) + '/' + str(max_hints), True, GREEN)
        hint_font_rect = hint_font.get_rect()
        hint_font_rect.center = (WINDOW_WIDTH / 2, fire_img_rect.top - 20)
        canvas.blit(hint_font, hint_font_rect)

        canvas.blit(cactus_img, cactus_img_rect)
        canvas.blit(fire_img, fire_img_rect)
        mario.update()

        if LEVEL == 'Final' and SCORE >= 50:
            congratulations_screen()

        pygame.display.update()
        CLOCK.tick(FPS)

start_game()
