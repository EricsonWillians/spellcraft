#include <SDL2/SDL.h>
#include <cstdlib>
#include <iostream>

using std::cerr;
using std::endl;

SDL_Window *win;
SDL_Renderer *ren;

int init()
{

    if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
    {
        cerr << "SDL_Init Error: " << SDL_GetError() << endl;
        return EXIT_FAILURE;
    }

    win = SDL_CreateWindow("Spellcraft", 100, 100, 620, 387, SDL_WINDOW_SHOWN);
    if (win == nullptr)
    {
        cerr << "SDL_CreateWindow Error: " << SDL_GetError() << endl;
        return EXIT_FAILURE;
    }

    ren = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (ren == nullptr)
    {
        cerr << "SDL_CreateRenderer Error" << SDL_GetError() << endl;
        if (win != nullptr)
        {
            SDL_DestroyWindow(win);
        }
        SDL_Quit();
        return EXIT_FAILURE;
    }

    return 0;
}