//
// Created by Anders Thuné on 2018-04-21.
//

#include "TextureManager.h"

SDL_Texture* TextureManager::loadTexture(const char *filename) {
    SDL_Surface *tempSurf = IMG_Load(filename);
    SDL_Texture *tex = SDL_CreateTextureFromSurface(Game::ren, tempSurf);
    SDL_FreeSurface(tempSurf);
    return tex;
}

