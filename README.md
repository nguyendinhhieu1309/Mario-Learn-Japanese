
# 🎮 Mario Learn Japanese

**Mario Learn Japanese** is a fun and interactive game designed to help you learn Japanese Hiragana, Katakana, and vocabulary through two engaging mini-games. You can choose between a character recognition game or a vocabulary learning game, all while guiding Mario through various levels and challenges!

## 🕹️ Features
- **Alphabet Game**: Practice your Japanese Hiragana and Katakana recognition by typing the correct pronunciation as characters move across the screen.
- **Vocabulary Game**: Enhance your Japanese vocabulary by matching words with their meanings in an exciting game environment.
- **Interactive Gameplay**: The games are integrated with fun challenges like dodging obstacles and collecting points, making learning more engaging.
- **Simple GUI**: A user-friendly Tkinter interface allows you to select your game mode easily.

## 🛠️ Technologies and Libraries Used
- ![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
- ![Pygame](https://img.shields.io/badge/Pygame-2.0.1-green.svg)
- ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-brightgreen.svg)
- ![PIL](https://img.shields.io/badge/PIL-8.x-orange.svg)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Mario-Learn-Japanese.git
cd Mario-Learn-Japanese
```

### 2. Install dependencies
Ensure you have Python 3.9 or higher installed, then install the required libraries:
```bash
pip install pygame pillow
```

### 3. Run the Application
To start the game, simply run the following command:
```bash
python MarioLearnJapanese.py
```

## 📂 Project Structure
```
Mario-Learn-Japanese/
│
├── alphabet.py              # The Hiragana and Katakana recognition game
├── vocarb.py                # The vocabulary learning game
├── MarioLearnJapanese.py     # The main launcher for the two games
├── assets/                  # Directory containing images and sound files
│   ├── background.png       # Background image for the game
│   ├── dragon.png           # Dragon obstacle in the game
│   ├── fire_bricks.png      # Fire obstacle in the game
│   ├── cactus_bricks.png    # Cactus obstacle in the game
│   ├── maryo.png            # Mario character image
│   └── ...                  # Other game assets
└── README.md                # Documentation
```

## 🖥️ Game Modes

### 1. Alphabet Game (alphabet.py)
- **Goal**: Learn Japanese characters (Hiragana, Katakana) by typing the correct Romanized pronunciation of each character as it appears on the screen.
- **Gameplay**: Control Mario to avoid obstacles while entering the correct pronunciation of the displayed Japanese characters to score points.
- **Characters**: Hiragana, Katakana, Dakuten, and Yoon combinations.

### 2. Vocabulary Game (vocarb.py)
- **Goal**: Improve your Japanese vocabulary by selecting the correct meaning of Japanese words.
- **Gameplay**: For each displayed Japanese word, select the correct meaning from multiple choices, while Mario dodges obstacles and progresses through the levels.
- **Levels**: Vocabulary from JPD113 and JPD123 courses, with increasing difficulty as you progress.

## 🎮 How to Play

1. **Main Menu**: Run the `MarioLearnJapanese.py` file and select either the "Alphabet" game or the "Vocabulary" game.
2. **Controls**: 
   - **Up Arrow**: Move Mario up.
   - **Down Arrow**: Move Mario down.
   - **Keyboard**: Type the pronunciation of characters or select the correct vocabulary meaning.
3. **Goal**: Achieve the highest score possible while learning Japanese characters and words, and avoid game-ending obstacles like dragons and fireballs.

## 📸 Demo and Results

Here are some screenshots from the games:

- **Alphabet Game**: 
  ![image](https://github.com/user-attachments/assets/e19f15bb-5c9f-4073-8384-2c95ff181122)

  
- **Vocabulary Game**: 
  ![image](https://github.com/user-attachments/assets/51c076eb-2cc2-4fe9-a2cc-931e09c85a71)


## 🧑‍💻 Contributing
Contributions are welcome! Here's how you can help:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

Please feel free to open issues if you find any bugs or have suggestions for improvements.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
Developed by **Your Name** - [LinkedIn](https://www.linkedin.com/in/nguyen-dinh-hieu-818778303/)

---

_If you found this project helpful, please give it a ⭐ on [GitHub](https://github.com/nguyendinhhieu1309/Mario-Learn-Japanese.git)!_
