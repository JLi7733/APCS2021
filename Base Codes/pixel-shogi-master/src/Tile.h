//
// Created by Anders Thuné on 2018-04-21.
//

#ifndef SHOGI_TILE_H
#define SHOGI_TILE_H
#include "Piece.h"
#include <cmath>

class Tile {
public:
    Tile(int, int);
    virtual ~Tile();
    virtual Piece *getPiece();
    virtual void setPiece(Piece*);
    std::pair<int, int> getCoords();
    virtual void loadTextures();
    void setMark(bool);
    void setPromoteBox();
    bool isMarked();
    void select();
    virtual void draw();
protected:
    bool selected = false;
    SDL_Texture* selectionMarker;
    int row;
    int col;
private:
    bool marked = false;
    bool promoteBox = false;
    SDL_Texture* moveMarker;
    Piece *piece = nullptr;
};

class HandTile: public Tile{
public:
    HandTile(int, int);
    ~HandTile() override;
    void loadTextures() override;
    Piece *getPiece() override;
    void setPiece(Piece*) override;
    void draw() override;
private:
    std::vector<Piece*> pieces;
};


#endif //SHOGI_TILE_H
