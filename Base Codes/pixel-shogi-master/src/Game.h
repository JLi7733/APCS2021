//
// Created by Anders Thuné on 2018-04-21.
//

#ifndef SHOGI_GAME_H
#define SHOGI_GAME_H

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include "TextureManager.h"
#include <iostream>

class Game {
public:
    bool init(const char *title, int xPos, int yPos, int w, int h, bool fullscreen);
    void handleEvents();
    void render();
    void clean();

    bool running() { return isRunning; };
    static SDL_Renderer *ren;
    static SDL_Window *win;
    static int wscaling, hscaling;

private:
    void updateWindowSize();
    bool isRunning;

};


#endif //SHOGI_GAME_H
