// Console.h
#ifndef CONSOLE_H
#define CONSOLE_H

#include <windows.h>
#include <conio.h>
#include <iostream>
#include <vector>

class Console {
public:
    Console();
    ~Console();

    void clearScreen();
    void mvprintw(int y, int x, const char* fmt, ...);
    void refreshScreen();
    int getchInput();
    void getScreenSize(int& height, int& width);
    void setNoDelay(bool enable);
    void hideCursor(bool hide);
    void beep();
    void flushInput();

private:
    HANDLE hConsole;
    int inputKey;
    int currentY, currentX;

    void gotoXY(int x, int y);
};

#endif