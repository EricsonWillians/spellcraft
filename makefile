CXX?=c++
SDL2FLAGS=$(shell pkg-config sdl2 --cflags --libs)
CXXFLAGS?=-std=c++11 -Wall -pedantic -Werror -Wshadow -Wstrict-aliasing -Wstrict-overflow

.PHONY: all msg clean fullclean

all: msg spellcraft

msg:
	@echo '--- C++11 ---'

spellcraft: src/spellcraft.cpp
	${CXX} ${CXXFLAGS} -O2 -o $@ $< ${SDL2FLAGS}

small: src/spellcraft.cpp
	${CXX} ${CXXFLAGS} -Os -o spellcraft $< ${SDL2FLAGS}
	-strip spellcraft
	-sstrip spellcraft

debug: src/spellcraft.cpp
	${CXX} ${CXXFLAGS} -O0 -g -o spellcraft $< ${SDL2FLAGS}

asm: spellcraft.asm

spellcraft.asm: src/spellcraft.cpp
	${CXX} ${CFLAGS} -S -o spellcraft.asm $< ${SDL2FLAGS}

run: msg spellcraft
	time ./spellcraft

clean:
	rm -f spellcraft *.o spellcraft.asm

fullclean: clean