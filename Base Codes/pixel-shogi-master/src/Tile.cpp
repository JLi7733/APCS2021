//
// Created by Anders Thuné on 2018-04-21.
//

#include "Tile.h"

Tile::Tile(int r, int c){
    row = r;
    col = c;
    loadTextures();
}
Tile::~Tile(){
    delete piece;
}
void Tile::loadTextures() {
    selectionMarker = TextureManager::loadTexture("assets/sprites/selectionMarker.png");
    moveMarker = TextureManager::loadTexture("assets/sprites/moveMarker.png");
}
Piece *Tile::getPiece() { return piece; };
void Tile::setPiece(Piece *p) { piece = p; };
void Tile::setPromoteBox() { promoteBox = true; }
std::pair<int, int> Tile::getCoords() {
    return {row, col};
}
void Tile::setMark(bool m){
    marked = m;
}
bool Tile::isMarked(){
    return marked;
}
void Tile::select(){
    selected = !selected;
}
void Tile::draw(){
    SDL_Rect destR;
    SDL_RendererFlip flip;
    SDL_Texture *tex;

    destR.w = Game::wscaling;
    destR.h = Game::hscaling;
    destR.x = (col + 1) * Game::wscaling;
    destR.y = row * Game::hscaling;

    if (piece != nullptr) {
        tex = piece->getTex();
        flip = piece->getPlayer() ? SDL_FLIP_NONE : SDL_RendererFlip(SDL_FLIP_VERTICAL | SDL_FLIP_HORIZONTAL);
        SDL_RenderCopyEx(Game::ren, tex, nullptr, &destR, 0.0, nullptr, flip);
    }

    if (selected) {
        SDL_RenderCopy(Game::ren, selectionMarker, nullptr,
                       &destR);
    }
    if (marked) {
        SDL_RenderCopy(Game::ren, moveMarker, nullptr, &destR);
    }
    if (promoteBox){
        destR.h *= 2;
        if (!piece -> getPlayer())
            destR.y -= Game::hscaling;
        flip = piece->getPlayer() ? SDL_FLIP_NONE : SDL_RendererFlip(SDL_FLIP_VERTICAL | SDL_FLIP_HORIZONTAL);
        SDL_RenderCopyEx(Game::ren, TextureManager::loadTexture("assets/sprites/promoteBox.png"), nullptr, &destR, 0.0,
                         nullptr, flip);
        promoteBox = false;
    }
}
HandTile::HandTile(int r, int c): Tile(r, c){}
HandTile::~HandTile(){
    for (auto &piece : pieces){
        delete piece;
    }
}

void HandTile::loadTextures() {
    selectionMarker = TextureManager::loadTexture("assets/sprites/selectionMarker.png");
}

Piece* HandTile::getPiece() {
    if (pieces.empty()){
        return nullptr;
    }
    return pieces.back();
}

void HandTile::setPiece(Piece *p) {
    if(p == nullptr){
        if (getPiece() != nullptr) {
            pieces.pop_back();
        }
    } else {
        pieces.push_back(p);
    }
}

void HandTile::draw(){
    SDL_Rect srcR;
    SDL_Rect destR;
    SDL_RendererFlip flip;
    SDL_Texture *tex, *number;

    srcR.w = srcR.h = 32;
    srcR.x = srcR.y = 0;
    destR.w = Game::wscaling;
    destR.h = Game::hscaling;
    destR.x = (col + 1) * Game::wscaling;
    destR.y = row * Game::hscaling;

    if (selected) {
        SDL_RenderCopy(Game::ren, selectionMarker, &srcR,
                       &destR);
    }

    for (auto& piece : pieces){
        tex = piece->getTex();
        flip = piece->getPlayer() ? SDL_FLIP_NONE : SDL_RendererFlip(SDL_FLIP_VERTICAL | SDL_FLIP_HORIZONTAL);
        SDL_RenderCopyEx(Game::ren, tex, &srcR, &destR, 0.0, nullptr, flip);
        destR.x += std::pow(-1, !(piece -> getPlayer())) * Game::wscaling/5;
    }
}
