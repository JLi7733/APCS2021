cmake_minimum_required(VERSION 3.10)
project(shogi)

set(CMAKE_CXX_STANDARD 11)

find_package(SDL2 REQUIRED)

add_executable(shogi
        src/main.cpp src/Game.cpp src/Game.h src/TextureManager.cpp src/TextureManager.h src/Board.cpp src/Board.h src/Piece.h src/Piece.cpp src/Tile.cpp src/Tile.h)

target_link_libraries(shogi SDL2 SDL2_image)
