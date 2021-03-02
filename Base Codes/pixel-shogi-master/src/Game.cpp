//
// Created by Anders Thuné on 2018-04-21.
//

#include "Game.h"
#include "Board.h"

Board *board;
SDL_Renderer *Game::ren = nullptr;
SDL_Window *Game::win = nullptr;
int Game::wscaling, Game::hscaling;

bool Game::init(const char *title, int xPos, int yPos, int w, int h, bool fullscreen) {
    if (SDL_Init(SDL_INIT_EVERYTHING) == 0){
        std::cout << "Successfully initialized!" << std::endl;

        Uint32 flags = SDL_WINDOW_RESIZABLE;
        if (fullscreen){
            flags |= SDL_WINDOW_FULLSCREEN;
        }

        win = SDL_CreateWindow(title, xPos, yPos, w, h, flags);
        if (win){
            std::cout << "Window created!" << std::endl;
        }

        ren = SDL_CreateRenderer(win, -1, 0);
        if (ren){
            std::cout << "Renderer created!" << std::endl;
        }

	updateWindowSize();

        isRunning = true;
        board = new Board();
        board -> init();

    } else {
        isRunning = false;
    }
    return isRunning;
}

void Game::updateWindowSize() {
    int w, h;

    SDL_GetWindowSize(Game::win, &w, &h);
    wscaling = w / 13;
    hscaling = h / 9;
}

void Game::handleEvents() {
    SDL_Event event;
    SDL_PollEvent(&event);

    switch (event.type) {
    case SDL_QUIT:
	isRunning = false;
	break;
    case SDL_MOUSEBUTTONDOWN:
    case SDL_BUTTON_LEFT:
	board->select(event.button.y / hscaling, event.button.x / wscaling - 1);
	render();
	break;
    case SDL_WINDOWEVENT:
	if (event.window.event == SDL_WINDOWEVENT_RESIZED)
	    updateWindowSize();
    default:
	break;
    }
}

void Game::render() {
    SDL_RenderClear(ren);
    board -> draw();
    SDL_RenderPresent(ren);
}

void Game::clean() {
    SDL_DestroyWindow(win);
    SDL_DestroyRenderer(ren);
    delete board;
    SDL_Quit();
    std::cout << "Game cleaned!" << std::endl;
}
