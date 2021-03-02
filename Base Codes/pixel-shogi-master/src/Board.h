//
// Created by Anders Thuné on 2018-04-21.
//

#ifndef SHOGI_BOARD_H
#define SHOGI_BOARD_H


#include "Game.h"
#include "Tile.h"
#include <vector>

class Board {
public:
    Board();
    ~Board();
    void init();
    void draw();
    void select(int row, int col);
    void clean();

private:
    void move(Tile* selected, Tile* target);
    void take(Tile* t, Tile* s);
    void promoteCheck(Tile *s, Tile *t);
    bool askPromote(Tile *t);
    void createMarkers (Tile *t);
    void createHandMarkers (Tile *t);
    bool legalTile(Tile *t, Piece *p);
    static const int w = 11;
    static const int h = 9;
    Tile *tiles[h][w];
    Tile *selected;
    int turn = 1;
    bool selecting = false;
    SDL_Texture* tex;
};


#endif //SHOGI_BOARD_H
