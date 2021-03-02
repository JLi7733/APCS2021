//
// Created by Anders Thuné on 2018-04-21.
//

#include "Board.h"

Board::Board(){
    for (int i = 0; i < h; i++){
        tiles[i][0] = new HandTile(i, 0);
        for (int j = 1; j < w-1; j++){
            tiles[i][j] = new Tile(i, j);
        }
        tiles[i][w-1] = new HandTile(i, w-1);
    }
}

Board::~Board(){
    for (auto &row : tiles){
        for (Tile *tile : row){
            delete tile;
        }
    }
}

void Board::init(){
    for (int j = 1; j < w-1; j++){
        tiles[2][j]-> setPiece(new Fu(0));
        tiles[6][j] -> setPiece(new Fu(1));
    }
    tiles[0][1] ->setPiece(new Kyou(0));
    tiles[0][9] ->setPiece(new Kyou(0));
    tiles[8][1] ->setPiece(new Kyou(1));
    tiles[8][9] ->setPiece(new Kyou(1));
    tiles[0][2] ->setPiece(new Kei(0));
    tiles[0][8] ->setPiece(new Kei(0));
    tiles[8][2] ->setPiece(new Kei(1));
    tiles[8][8] ->setPiece(new Kei(1));
    tiles[0][3] ->setPiece(new Gin(0));
    tiles[0][7] ->setPiece(new Gin(0));
    tiles[8][3] ->setPiece(new Gin(1));
    tiles[8][7] ->setPiece(new Gin(1));
    tiles[0][4] ->setPiece(new Kin(0));
    tiles[0][6] ->setPiece(new Kin(0));
    tiles[8][4] ->setPiece(new Kin(1));
    tiles[8][6] ->setPiece(new Kin(1));
    tiles[0][5] ->setPiece(new Gyoku(0, true));
    tiles[8][5] ->setPiece(new Gyoku(1, false));
    tiles[1][8] ->setPiece(new Kaku(0));
    tiles[7][2] ->setPiece(new Kaku(1));
    tiles[1][2] ->setPiece(new Hisha(0));
    tiles[7][8] ->setPiece(new Hisha(1));

    tex = TextureManager::loadTexture("assets/sprites/board.png");
}
void Board::draw(){
    SDL_RenderCopy(Game::ren, tex, nullptr, nullptr);
    for (auto &row : tiles) {
        for (Tile *tile : row) {
            tile->draw();
        }
    }
}
void Board::select(int row, int col){
    bool outOfBounds = (row >= h || row < 0 || col >= w || col < 0);
    bool handClicked = (col == 0 || col == w-1);
    if (!outOfBounds){
        if (selecting){
            move(selected, tiles[row][col]);
        }
        else if (tiles[row][col] -> getPiece() == nullptr || tiles[row][col] -> getPiece() -> getPlayer() != turn){
            return;
        }
        else{
            selected = tiles[row][col];
            selected->select();
            if (handClicked){
                createHandMarkers(selected);
            } else {
                createMarkers(selected);
            }
            selecting = true;
        }
    }
}
void Board::move(Tile* selected, Tile* target){
    if (target -> isMarked()) {
        if (target->getPiece() == nullptr) {
            target->setPiece(selected ->getPiece());
            selected->setPiece(nullptr);
        } else {
            take(target, selected);
            target->setPiece(selected ->getPiece());
            selected->setPiece(nullptr);
        }
        if(selected -> getCoords().second>0 && selected -> getCoords().second<w-1) {
            promoteCheck(selected, target);
        }
        turn = !turn;
    }
    for (auto &row : tiles) {
        for (Tile *tile : row) {
            tile->setMark(false);
        }
    }
    selecting = false;
    selected -> select();
}

void Board::take(Tile *t, Tile *s){
    Piece *p = t ->getPiece();
    int type = p -> getId();
    int playerIdx = turn ? w-1 : 0;

    p -> swapPlayer();
    if (p -> isPromoted()){
        p -> promote();
    }
    tiles[type][playerIdx] -> setPiece(t -> getPiece());
}

void Board::promoteCheck(Tile *s, Tile *t) {
    Piece *p = t->getPiece();
    if (p->isPromotable() && !(p->isPromoted())) {
        if (!legalTile(t, p)) {
            p->promote();
        } else if ((!turn && (s->getCoords().first >= 6 || t->getCoords().first >= 6)) ||
            (turn && (s->getCoords().first <= 2 || t->getCoords().first <= 2))) {
            if (askPromote(t))
                p -> promote();
        }
    }
}

bool Board::askPromote(Tile *t){
    t -> setPromoteBox();
    t -> draw();
    SDL_RenderPresent(Game::ren);
    int row, col;
    while (true){
        SDL_Event event;
        SDL_PollEvent(&event);
        switch(event.type){
            case SDL_MOUSEBUTTONDOWN:
                row = event.button.y / Game::hscaling;
                col = event.button.x / Game::wscaling - 1;
                if (row == t->getCoords().first && col == t->getCoords().second){
                    return true;
                } else if (row == t->getCoords().first + std::pow(-1, !turn) && col == t->getCoords().second){
                    return false;
                }
                    break;
            default:
                SDL_Delay(5);
                break;
        }
    }
}

void Board::createMarkers(Tile *t){
    Piece *p = t ->getPiece();
    auto plSign = (int)(pow(-1, turn));
    for (auto& move : p ->getMoves()){
        int dr = plSign*move[1];
        int dc = plSign*move[2];
        int r = t->getCoords().first + dr;
        int c = t->getCoords().second + dc;

        while (!(r >= h || r < 0 || c >= w-1 || c < 1)){
            if (tiles[r][c] ->getPiece() != nullptr){
                if (tiles[r][c] ->getPiece()->getPlayer() != turn){
                    tiles[r][c] -> setMark(true);
                }
                break;
            }
            tiles[r][c] ->setMark(true);
            r += dr;
            c += dc;
            if(!move[0]){
                break;
            }
        }
    }
}

void Board::createHandMarkers(Tile *t){
    for (auto& row : tiles){
        for (int j = 1; j < w-1; j++){
            if(row[j] -> getPiece() == nullptr && legalTile(row[j], t->getPiece())){
                row[j] ->setMark(true);
            }
        }
    }
}

bool Board::legalTile(Tile *t, Piece *p){
    int r = t->getCoords().first;
    int type = p->getId();
    if(type == 0){
        for (int j = 0; j < h; j++){
            Piece *p2 = tiles[j][t->getCoords().second] -> getPiece();
            if (p2 != nullptr && p2 -> getId() == 0 && p2 != p && p2 -> getPlayer() == turn){
                return false;
            }
        }
    }
    return !(((type == 0 || type == 1) && ((turn && r <= 0) || (!turn && r >= h-1))) || (type == 2 && ((turn && r <= 1) || (!turn && r >= h-2))));
}

void Board::clean() {
    for (auto &row : tiles){
        for (Tile *tile : row){
            delete tile -> getPiece();
            tile -> setPiece(nullptr);
        }
    }
}
