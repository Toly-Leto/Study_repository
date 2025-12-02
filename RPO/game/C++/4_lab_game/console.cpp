// Console.cpp
#include "Console.h"

Console::Console() {
    hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTitleA("Two-Player Paddle Game");
}

Console::~Console() {}

void Console::clearScreen() {
    system("cls");
}

void Console::mvprintw(int y, int x, const char* fmt, ...) {
    gotoXY(x, y);
    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
}

void Console::refreshScreen() {
    // With direct console output, this function is mostly a no-op,
    // as `printf` is direct. We clear the screen each frame for movement.
}

int Console::getchInput() {
    if (_kbhit()) {
        return _getch();
    }
    return -1; // No key pressed
}

void Console::getScreenSize(int& height, int& width) {
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(hConsole, &csbi);
    width = csbi.srWindow.Right - csbi.srWindow.Left + 1;
    height = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;
}

void Console::setNoDelay(bool enable) {
    // No-op for this implementation. _kbhit() handles non-blocking.
}

void Console::hideCursor(bool hide) {
    CONSOLE_CURSOR_INFO cursorInfo;
    GetConsoleCursorInfo(hConsole, &cursorInfo);
    cursorInfo.bVisible = !hide;
    SetConsoleCursorInfo(hConsole, &cursorInfo);
}

void Console::gotoXY(int x, int y) {
    COORD coord = { static_cast<SHORT>(x), static_cast<SHORT>(y) };
    SetConsoleCursorPosition(hConsole, coord);
}

void Console::beep() {
    Beep(1000, 100);
}

void Console::flushInput() {
    // No-op for non-buffered input.
}