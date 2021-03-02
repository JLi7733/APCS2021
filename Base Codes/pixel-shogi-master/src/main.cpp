#include <iostream>
#include "Game.h"

Game *game = nullptr;

int main(){
    const int FPS = 200;
    const int frameDelay = 1000/FPS;

    Uint32 frameStart;
    int frameTime;

    game = new Game();
    if(game->init("PixelShogi", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 64*13, 64*9, false)){
        game -> render();
    }


    while(game->running()){
        frameStart = SDL_GetTicks();
        game->handleEvents();
        frameTime = SDL_GetTicks() - frameStart;

        if(frameDelay > frameTime){
            SDL_Delay(frameDelay - frameTime);
        }
    }

    game->clean();
    delete game;
    return 0;
}