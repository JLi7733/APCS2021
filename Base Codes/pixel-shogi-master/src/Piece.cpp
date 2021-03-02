//
// Created by Anders Thuné on 2018-04-21.
//
#include "Piece.h"

Piece::Piece(int player) {
        this->player = player;
        promoted = false;
};

SDL_Texture* Piece::getTex() {
    if (promoted)
        return promotedTex;
    else
        return tex;
};

std::vector<std::array<int, 3>> Piece::getMoves() {
    if (promoted)
        return promotedMoves;
    else
        return moves;
};

bool Piece::isPromotable(){
    return promotable;
}

bool Piece::isPromoted() {
    return promoted;
}

void Piece::promote(){
    promoted = !promoted;
}

int Piece::getPlayer() {
    return player;
}

int Piece::getId(){
    return id;
}

void Piece::swapPlayer() {
    player = !player;
}

Fu::Fu(int player): Piece(player) {
    id = 0;
    moves.push_back({0, 1, 0});
    promotedMoves.push_back({0, 1, 0});
    promotedMoves.push_back({0, 1, 1});
    promotedMoves.push_back({0, 1, -1});
    promotedMoves.push_back({0, 0, -1});
    promotedMoves.push_back({0, 0, 1});
    promotedMoves.push_back({0, -1, 0});
    tex = TextureManager::loadTexture("assets/sprites/fu.png");
    promotedTex = TextureManager::loadTexture("assets/sprites/to.png");
}

Kyou::Kyou(int player): Piece(player){
    id = 1;
    moves.push_back({1, 1, 0});
    promotedMoves.push_back({0, 1, 0});
    promotedMoves.push_back({0, 1, 1});
    promotedMoves.push_back({0, 1, -1});
    promotedMoves.push_back({0, 0, -1});
    promotedMoves.push_back({0, 0, 1});
    promotedMoves.push_back({0, -1, 0});
    tex = TextureManager::loadTexture("assets/sprites/kyou.png");
    promotedTex = TextureManager::loadTexture("assets/sprites/narikyou.png");
}

Kei::Kei(int player): Piece(player){
    id = 2;
    moves.push_back({0, 2, 1});
    moves.push_back({0, 2, -1});
    promotedMoves.push_back({0, 1, 0});
    promotedMoves.push_back({0, 1, 1});
    promotedMoves.push_back({0, 1, -1});
    promotedMoves.push_back({0, 0, -1});
    promotedMoves.push_back({0, 0, 1});
    promotedMoves.push_back({0, -1, 0});
    tex = TextureManager::loadTexture("assets/sprites/kei.png");
    promotedTex = TextureManager::loadTexture("assets/sprites/narikei.png");
}

Gin::Gin(int player): Piece(player){
    id = 3;
    moves.push_back({0, 1, 0});
    moves.push_back({0, 1, 1});
    moves.push_back({0, 1, -1});
    moves.push_back({0, -1, -1});
    moves.push_back({0, -1, 1});
    promotedMoves.push_back({0, 1, 0});
    promotedMoves.push_back({0, 1, 1});
    promotedMoves.push_back({0, 1, -1});
    promotedMoves.push_back({0, 0, -1});
    promotedMoves.push_back({0, 0, 1});
    promotedMoves.push_back({0, -1, 0});
    tex = TextureManager::loadTexture("assets/sprites/gin.png");
    promotedTex = TextureManager::loadTexture("assets/sprites/narigin.png");
}
Kin::Kin(int player): Piece(player){
    id = 4;
    moves.push_back({0, 1, 0});
    moves.push_back({0, 1, 1});
    moves.push_back({0, 1, -1});
    moves.push_back({0, 0, -1});
    moves.push_back({0, 0, 1});
    moves.push_back({0, -1, 0});
    tex = TextureManager::loadTexture("assets/sprites/kin.png");
    promotable = false;
}

Kaku::Kaku(int player): Piece(player){
    id = 5;
    moves.push_back({1, 1, 1});
    moves.push_back({1, -1, 1});
    moves.push_back({1, -1, -1});
    moves.push_back({1, 1, -1});
    promotedMoves.push_back({0, 1, 0});
    promotedMoves.push_back({1, 1, 1});
    promotedMoves.push_back({1, 1, -1});
    promotedMoves.push_back({0, 0, -1});
    promotedMoves.push_back({0, 0, 1});
    promotedMoves.push_back({0, -1, 0});
    promotedMoves.push_back({1, -1, -1});
    promotedMoves.push_back({1, -1, 1});
    tex = TextureManager::loadTexture("assets/sprites/kaku.png");
    promotedTex = TextureManager::loadTexture("assets/sprites/uma.png");
}

Hisha::Hisha(int player): Piece(player){
    id = 6;
    moves.push_back({1, 0, 1});
    moves.push_back({1, 1, 0});
    moves.push_back({1, -1, 0});
    moves.push_back({1, 0, -1});
    promotedMoves.push_back({1, 1, 0});
    promotedMoves.push_back({0, 1, 1});
    promotedMoves.push_back({0, 1, -1});
    promotedMoves.push_back({1, 0, -1});
    promotedMoves.push_back({1, 0, 1});
    promotedMoves.push_back({1, -1, 0});
    promotedMoves.push_back({0, -1, -1});
    promotedMoves.push_back({0, -1, 1});
    tex = TextureManager::loadTexture("assets/sprites/hisha.png");
    promotedTex = TextureManager::loadTexture("assets/sprites/ryuu.png");
}

Gyoku::Gyoku(int player, bool ou): Piece(player){
    id = 7;
    moves.push_back({0, 1, 0});
    moves.push_back({0, 1, 1});
    moves.push_back({0, 1, -1});
    moves.push_back({0, 0, -1});
    moves.push_back({0, 0, 1});
    moves.push_back({0, -1, 0});
    moves.push_back({0, -1, -1});
    moves.push_back({0, -1, 1});
    if (ou){
        tex = TextureManager::loadTexture("assets/sprites/ou.png");
    } else{
        tex = TextureManager::loadTexture("assets/sprites/gyoku.png");
    }
    promotable = false;
}
