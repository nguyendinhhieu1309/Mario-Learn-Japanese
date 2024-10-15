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

    def __init__(self):
        self.dragon_img = pygame.image.load('assets/dragon.png')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = WINDOW_HEIGHT / 2
        self.dragon_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False

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

skip_count = 0

class JapaneseCharacter:
    character_velocity = 5  # Reduced character velocity
    hiragana = [
        ('あ', 'a'), ('い', 'i'), ('う', 'u'), ('え', 'e'), ('お', 'o'),
        ('か', 'ka'), ('き', 'ki'), ('く', 'ku'), ('け', 'ke'), ('こ', 'ko'),
        ('さ', 'sa'), ('し', 'shi'), ('す', 'su'), ('せ', 'se'), ('そ', 'so'),
        ('た', 'ta'), ('ち', 'chi'), ('つ', 'tsu'), ('て', 'te'), ('と', 'to'),
        ('な', 'na'), ('に', 'ni'), ('ぬ', 'nu'), ('ね', 'ne'), ('の', 'no'),
        ('は', 'ha'), ('ひ', 'hi'), ('ふ', 'fu'), ('へ', 'he'), ('ほ', 'ho'),
        ('ま', 'ma'), ('み', 'mi'), ('む', 'mu'), ('め', 'me'), ('も', 'mo'),
        ('や', 'ya'), ('ゆ', 'yu'), ('よ', 'yo'),
        ('ら', 'ra'), ('り', 'ri'), ('る', 'ru'), ('れ', 're'), ('ろ', 'ro'),
        ('わ', 'wa'), ('を', 'wo'), ('ん', 'n')
    ]
    katakana = [
        ('ア', 'a'), ('イ', 'i'), ('ウ', 'u'), ('エ', 'e'), ('オ', 'o'),
        ('カ', 'ka'), ('キ', 'ki'), ('ク', 'ku'), ('ケ', 'ke'), ('コ', 'ko'),
        ('サ', 'sa'), ('シ', 'shi'), ('ス', 'su'), ('セ', 'se'), ('ソ', 'so'),
        ('タ', 'ta'), ('チ', 'chi'), ('ツ', 'tsu'), ('テ', 'te'), ('ト', 'to'),
        ('ナ', 'na'), ('ニ', 'ni'), ('ヌ', 'nu'), ('ネ', 'ne'), ('ノ', 'no'),
        ('ハ', 'ha'), ('ヒ', 'hi'), ('フ', 'fu'), ('ヘ', 'he'), ('ホ', 'ho'),
        ('マ', 'ma'), ('ミ', 'mi'), ('ム', 'mu'), ('メ', 'me'), ('モ', 'mo'),
        ('ヤ', 'ya'), ('ユ', 'yu'), ('ヨ', 'yo'),
        ('ラ', 'ra'), ('リ', 'ri'), ('ル', 'ru'), ('レ', 're'), ('ロ', 'ro'),
        ('ワ', 'wa'), ('ヲ', 'wo'), ('ン', 'n')
    ]

    hiragana_dakuten = [
        ('が', 'ga'), ('ぎ', 'gi'), ('ぐ', 'gu'), ('げ', 'ge'), ('ご', 'go'),
        ('ざ', 'za'), ('じ', 'ji'), ('ず', 'zu'), ('ぜ', 'ze'), ('ぞ', 'zo'),
        ('だ', 'da'), ('ぢ', 'ji'), ('づ', 'zu'), ('で', 'de'), ('ど', 'do'),
        ('ば', 'ba'), ('び', 'bi'), ('ぶ', 'bu'), ('べ', 'be'), ('ぼ', 'bo'),
        ('ぱ', 'pa'), ('ぴ', 'pi'), ('ぷ', 'pu'), ('ぺ', 'pe'), ('ぽ', 'po')
    ]

    katakana_dakuten = [
        ('ガ', 'ga'), ('ギ', 'gi'), ('グ', 'gu'), ('ゲ', 'ge'), ('ゴ', 'go'),
        ('ザ', 'za'), ('ジ', 'ji'), ('ズ', 'zu'), ('ゼ', 'ze'), ('ゾ', 'zo'),
        ('ダ', 'da'), ('ヂ', 'ji'), ('ヅ', 'zu'), ('デ', 'de'), ('ド', 'do'),
        ('バ', 'ba'), ('ビ', 'bi'), ('ブ', 'bu'), ('ベ', 'be'), ('ボ', 'bo'),
        ('パ', 'pa'), ('ピ', 'pi'), ('プ', 'pu'), ('ペ', 'pe'), ('ポ', 'po')
    ]

    hiragana_yoon = [
        ('きゃ', 'kya'), ('きゅ', 'kyu'), ('きょ', 'kyo'),
        ('しゃ', 'sha'), ('しゅ', 'shu'), ('しょ', 'sho'),
        ('ちゃ', 'cha'), ('ちゅ', 'chu'), ('ちょ', 'cho'),
        ('にゃ', 'nya'), ('にゅ', 'nyu'), ('にょ', 'nyo'),
        ('ひゃ', 'hya'), ('ひゅ', 'hyu'), ('ひょ', 'hyo'),
        ('みゃ', 'mya'), ('みゅ', 'myu'), ('みょ', 'myo'),
        ('りゃ', 'rya'), ('りゅ', 'ryu'), ('りょ', 'ryo'),
        ('ぎゃ', 'gya'), ('ぎゅ', 'gyu'), ('ぎょ', 'gyo'),
        ('じゃ', 'ja'), ('じゅ', 'ju'), ('じょ', 'jo'),
        ('びゃ', 'bya'), ('びゅ', 'byu'), ('びょ', 'byo'),
        ('ぴゃ', 'pya'), ('ぴゅ', 'pyu'), ('ぴょ', 'pyo')
    ]

    katakana_yoon = [
        ('キャ', 'kya'), ('キュ', 'kyu'), ('キョ', 'kyo'),
        ('シャ', 'sha'), ('シュ', 'shu'), ('ショ', 'sho'),
        ('チャ', 'cha'), ('チュ', 'chu'), ('チョ', 'cho'),
        ('ニャ', 'nya'), ('ニュ', 'nyu'), ('ニョ', 'nyo'),
        ('ヒャ', 'hya'), ('ヒュ', 'hyu'), ('ヒョ', 'hyo'),
        ('ミャ', 'mya'), ('ミュ', 'myu'), ('ミョ', 'myo'),
        ('リャ', 'rya'), ('リュ', 'ryu'), ('リョ', 'ryo'),
        ('ギャ', 'gya'), ('ギュ', 'gyu'), ('ギョ', 'gyo'),
        ('ジャ', 'ja'), ('ジュ', 'ju'), ('ジョ', 'jo'),
        ('ビャ', 'bya'), ('ビュ', 'byu'), ('ビョ', 'byo'),
        ('ピャ', 'pya'), ('ピュ', 'pyu'), ('ピョ', 'pyo')
    ]
    def __init__(self, character_set):
        self.character_set = character_set
        self.hiragana, self.pronunciation = random.choice(self.character_set)
        self.character_img = font.render(self.hiragana, True, GREEN)
        self.character_img_rect = self.character_img.get_rect()
        self.character_img_rect.right = dragon.dragon_img_rect.left
        self.character_img_rect.top = dragon.dragon_img_rect.top + 30
    def update(self):
        canvas.blit(self.character_img, self.character_img_rect)
        if self.character_img_rect.left > 0:
            self.character_img_rect.left -= self.character_velocity

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
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.mario_img_rect.bottom >= fire_img_rect.top:
            game_over()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.up:
            self.mario_img_rect.top -= self.velocity
        if self.down:
            self.mario_img_rect.bottom += self.velocity

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
        set_options = ["Hiragana (Chữ mềm)", "Katakana (Chữ Cứng)", "Hiragana Dakuten (Biến Âm)", "Katakana Dakuten (Biến Âm)", "Hiragana Yoon (Âm ghép)", "Katakana Yoon (Âm ghép)"]
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

def get_character_set(selected_set):
    if selected_set == "Hiragana (Chữ mềm)":
        return JapaneseCharacter.hiragana
    elif selected_set == "Katakana (Chữ Cứng)":
        return JapaneseCharacter.katakana
    elif selected_set == "Hiragana Dakuten (Biến Âm)":
        return JapaneseCharacter.hiragana_dakuten
    elif selected_set == "Katakana Dakuten (Biến Âm)":
        return JapaneseCharacter.katakana_dakuten
    elif selected_set == "Hiragana Yoon (Âm ghép)":
        return JapaneseCharacter.hiragana_yoon
    elif selected_set == "Katakana Yoon (Âm ghép)":
        return JapaneseCharacter.katakana_yoon

def start_game():
    selected_set = display_menu()  # Chọn một trong 6 set từ
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
        pygame.display.update()

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
    current_set = selected_set  # Lưu lại set từ hiện tại để sử dụng lại khi restart game
    dragon = Dragon()
    characters_list = []
    mario = Mario()
    add_new_character_counter = 0
    global SCORE
    SCORE = 0
    global LEVEL
    LEVEL = 1
    global skip_count
    skip_count = 0  # Đếm số lần bỏ qua chữ cái
    hint_displayed = False  # Trạng thái hiển thị gợi ý

    pygame.mixer.music.load('assets/mario_theme1.mp3')
    pygame.mixer.music.play(-1, 0.0)

    current_input = ""
    character_set = get_character_set(selected_set)

    while True:
        canvas.fill(BLACK)
        check_level(SCORE)
        dragon.update()

        if not characters_list:  # Nếu không còn ký tự nào, thêm ký tự mới
            new_character = JapaneseCharacter(character_set)
            characters_list.append(new_character)

        for character in characters_list:
            if character.character_img_rect.left <= 0:  # Nếu ký tự bị bỏ qua
                characters_list.remove(character)
                skip_count += 1  # Tăng số lần bỏ qua ký tự
                if skip_count >= 5:
                    game_over()
                else:
                    new_character = JapaneseCharacter(character_set)
                    characters_list.append(new_character)
            character.update()

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
                elif event.key == pygame.K_1:  # Kiểm tra phím gợi ý
                    hint_displayed = True  # Hiển thị gợi ý
                elif event.unicode:
                    current_input += event.unicode
                    for character in characters_list:
                        if current_input == character.pronunciation:  # Nếu nhập đúng
                            characters_list.remove(character)
                            SCORE += 1
                            current_input = ""
                            hint_displayed = False  # Reset gợi ý khi nhập đúng
                            skip_count = 0  # Reset số lần bỏ qua khi nhập đúng
                            new_character = JapaneseCharacter(character_set)
                            characters_list.append(new_character)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    mario.up = False
                elif event.key == pygame.K_DOWN:
                    mario.down = False

        input_font = font.render('Input:' + current_input, True, GREEN)
        input_font_rect = input_font.get_rect()
        input_font_rect.center = (600, cactus_img_rect.bottom + input_font_rect.height / 2)
        canvas.blit(input_font, input_font_rect)

        score_font = font.render('Score:' + str(SCORE), True, GREEN)
        score_font_rect = score_font.get_rect()
        score_font_rect.center = (200, cactus_img_rect.bottom + score_font_rect.height / 2)
        canvas.blit(score_font, score_font_rect)

        level_font = font.render('Level:' + str(LEVEL), True, GREEN)
        level_font_rect = level_font.get_rect()
        level_font_rect.center = (400, cactus_img_rect.bottom + score_font_rect.height / 2)
        canvas.blit(level_font, level_font_rect)

        top_score_font = font.render('Top Score:' + str(topscore.high_score), True, GREEN)
        top_score_font_rect = top_score_font.get_rect()
        top_score_font_rect.center = (800, cactus_img_rect.bottom + score_font_rect.height / 2)
        canvas.blit(top_score_font, top_score_font_rect)

        skip_count_font = font.render('Skip Count:' + str(skip_count), True, GREEN)
        skip_count_font_rect = skip_count_font.get_rect()
        skip_count_font_rect.center = (1000, cactus_img_rect.bottom + score_font_rect.height / 2)
        canvas.blit(skip_count_font, skip_count_font_rect)

        # Hiển thị gợi ý nếu trạng thái hiển thị gợi ý được kích hoạt
        if hint_displayed:
            hint_font = font.render('Hint:' + characters_list[0].pronunciation[0], True, GREEN)
            hint_font_rect = hint_font.get_rect()
            hint_font_rect.center = (WINDOW_WIDTH / 2, fire_img_rect.top - 50)
            canvas.blit(hint_font, hint_font_rect)

        canvas.blit(cactus_img, cactus_img_rect)
        canvas.blit(fire_img, fire_img_rect)
        mario.update()

        if LEVEL == 'Final' and SCORE >= 50:
            congratulations_screen()

        for character in characters_list:
            if character.character_img_rect.colliderect(mario.mario_img_rect):
                game_over()

        pygame.display.update()
        CLOCK.tick(FPS)

start_game()
