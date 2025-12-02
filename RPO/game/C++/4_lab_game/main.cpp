#include "Console.h"
#include <iostream>



// Global constants
const int PADDLE_WIDTH = 12;
const int BALL_DELAY_MS = 10;

class Paddle {
public:
    Paddle(int x, int y, int screenWidth, int screenHeight, int upKey, int downKey)
        : x(x), y(y), screenWidth(screenWidth), screenHeight(screenHeight), upKey(upKey), downKey(downKey) {
    }

    void draw(Console& console) const {
        for (int i = 0; i < PADDLE_WIDTH; ++i) {
            console.mvprintw(y + i - (PADDLE_WIDTH / 2), x, "|");
        }
    }

    void move(int key) {
        if (key == upKey && y > PADDLE_WIDTH / 2 + 1) {
            y -= 1;
        }
        if (key == downKey && y < screenHeight - PADDLE_WIDTH / 2 - 2) {
            y += 1;
        }
    }

    int getY() const { return y; }
    int getX() const { return x; }

protected:
    int x, y;
    int screenWidth, screenHeight;
    int upKey, downKey;
};

class Ball {
public:
    Ball(int x, int y, int dirX, int dirY, int screenWidth, int screenHeight)
        : x(x), y(y), dirX(dirX), dirY(dirY), screenWidth(screenWidth), screenHeight(screenHeight) {
    }

    void draw(Console& console) const {
        console.mvprintw(y, x, "(@)");
    }

    void update() {
        x += dirX * 2;
        y += dirY;
    }

    void handleWallCollision() {
        if (y <= 1 || y >= screenHeight - 2) {
            dirY *= -1;
        }
    }

    bool handlePaddleCollision(const Paddle& paddle, int paddleSide) {
        if (x == paddle.getX() + paddleSide && y >= paddle.getY() - (PADDLE_WIDTH / 2) && y <= paddle.getY() + (PADDLE_WIDTH / 2)) {
            dirX *= -1;
            return true;
        }
        return false;
    }

    bool checkScoring(int& score1, int& score2) {
        if (x <= 0) {
            score2++;
            reset();
            dirX *= -1;
            return true;
        }
        if (x >= screenWidth - 1) {
            score1++;
            reset();
            dirX *= -1;
            return true;
        }
        return false;
    }

protected:
    void reset() {
        x = screenWidth / 2;
        y = screenHeight / 2;
    }

    int x, y;
    int dirX, dirY;
    int screenWidth, screenHeight;
};

class Game {
public:
    Game() :
        gameOver(false),
        score1(0),
        score2(0),
        screenWidth(0),
        screenHeight(0),
        player1(0, 0, 0, 0, 'w', 's'),
        player2(0, 0, 0, 0, 72, 80), // Using arrow key codes
        ball(0, 0, 0, 0, 0, 0)
    {
        // Initialize console properties
        console.hideCursor(true);
        console.getScreenSize(screenHeight, screenWidth);

        // Re-initialize objects after getting screen dimensions
        player1 = Paddle(PADDLE_WIDTH / 2 + 1, screenHeight / 2, screenWidth, screenHeight, 'w', 's');
        player2 = Paddle(screenWidth - PADDLE_WIDTH / 2 - 2, screenHeight / 2, screenWidth, screenHeight, 72, 80);
        ball = Ball(screenWidth / 2, screenHeight / 2, -1, -1, screenWidth, screenHeight);
    }

    ~Game() {
        console.hideCursor(false);
        console.clearScreen();
        std::cout << "Game Over! Final Score: Player 1: " << score1 << ", Player 2: " << score2 << std::endl;
    }

    void run() {
        while (!gameOver) {
            draw();
            input();
            logic();
            Sleep(BALL_DELAY_MS);
        }
    }

protected:
    void draw() {
        console.clearScreen();
        drawBorders();
        player1.draw(console);
        player2.draw(console);
        ball.draw(console);
        drawScores();
        console.refreshScreen();
    }

    void drawBorders() {
        for (int i = 0; i < screenWidth; ++i) {
            console.mvprintw(0, i, "#");
            console.mvprintw(screenHeight - 1, i, "_");
        }
        for (int i = 0; i < screenHeight; ++i) {
            console.mvprintw(i, 0, "#");
            console.mvprintw(i, screenWidth - 1, "#");
        }
    }

    void drawScores() {
        console.mvprintw(screenHeight - 1, screenWidth / 4, "Score 1: %d", score1);
        console.mvprintw(screenHeight - 1, screenWidth / 4 * 3, "Score 2: %d", score2);
    }

    void input() {
        int key = console.getchInput();
        if (key == 'q' || key == 'Q') {
            gameOver = true;
        }
        player1.move(key);
        player2.move(key);
    }

    void logic() {
        ball.update();
        ball.handleWallCollision();
        ball.handlePaddleCollision(player1, 1);
        ball.handlePaddleCollision(player2, -2);
        ball.checkScoring(score1, score2);
    }

    bool gameOver;
    int score1, score2;
    int screenWidth, screenHeight;
    Paddle player1;
    Paddle player2;
    Ball ball;
    Console console;
};

int main() {
    Game game;
    game.run();
    return 0;
}