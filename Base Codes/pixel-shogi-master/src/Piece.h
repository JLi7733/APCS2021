//
// Created by Anders Thuné on 2018-04-21.
//

#ifndef SHOGI_PIECE_H
#define SHOGI_PIECE_H

#include "Game.h"
#include <vector>
#include <array>

class Piece {
public:
    explicit Piece(int player);
    SDL_Texture* getTex();
    std::vector<std::array<int, 3>> getMoves();
    bool isPromotable();
    bool isPromoted();
    void promote();
    int getPlayer();
    int getId();
    void swapPlayer();
protected:
    SDL_Texture* tex;
    SDL_Texture* promotedTex;
    int player;
    int id;
    bool promoted;
    bool promotable = true;
    std::vector<std::array<int, 3>> moves;
    std::vector<std::array<int, 3>> promotedMoves;
};

class Fu: public Piece{
public:
    explicit Fu(int player);
};

class Kyou: public Piece{
public:
    explicit Kyou(int player);
};

class Kei: public Piece{
public:
    explicit Kei(int player);
};

class Gin: public Piece{
public:
    explicit Gin(int player);
};

class Kin: public Piece{
public:
    explicit Kin(int player);
};

class Gyoku: public Piece{
public:
    explicit Gyoku(int player, bool ou);
};

class Hisha: public Piece{
public:
    explicit Hisha(int player);
};

class Kaku: public Piece{
public:
    explicit Kaku(int player);
};


#endif //SHOGI_PIECE_H
