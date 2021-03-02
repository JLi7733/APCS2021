//
// Created by Anders Thuné on 2018-04-21.
//
#ifndef SHOGI_TEXTUREMANAGER_H
#define SHOGI_TEXTUREMANAGER_H

#include "Game.h"

class TextureManager {
public:
    static SDL_Texture* loadTexture(const char *filename);
};


#endif //SHOGI_TEXTUREMANAGER_H
