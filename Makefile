# Defining the system
ifeq ($(OS),Windows_NT)
	SYS := WIN
else
	SYS := LINUX
endif


# Defining the dir paths to both systems
ifeq ($(SYS),LINUX)
	BIN = ./src/C/bin
	INCLUDE = ./src/C/include
	OBJ = ./src/C/obj
	SRC = ./src/C/src
	RUN = $(BIN)/main
	DOT = ""
else
	BIN = .\src\C\bin
	INCLUDE = .\src\C\include
	OBJ = .\src\C\obj
	SRC = .\src\C\src
	RUN = $(BIN)\\main.exe
	DOT = .

endif

# General variables
C_COMP = gcc
CFLAGS = -O2 -Wall -Wextra


# Ignore these file names
.PHONY: \
		all \
		libed \
		linux \
		run \
		clean \
		windows \
		libed_windows \
		myapps_windows \
		help \
		docs


# Will compile to linux
all: linux


# Compile libs linux
libed:	\
		$(OBJ)/benchmark.o \
		$(OBJ)/bubble_sort.o

	
# Compile to linux
linux: libed
	$(C_COMP) $(SRC)/main.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/main


# Generic flag to object.o files linux
$(OBJ)/%.o: $(SRC)/%.c $(INCLUDE)/%.h
	$(C_COMP) -c $< -I $(INCLUDE) -o $@


# Generic flag to object.o files windows
$(OBJ)\\%.o: $(SRC)\\%.c $(INCLUDE)\\%.h
	$(C_COMP) -c $< -I $(INCLUDE) -o $@


# Compile libs Windows
libed_windows:	\
	$(OBJ)\\benchmark.o \
	$(OBJ)\\bubble_sort.o


# Compile to windows
windows: libed_windows
	$(C_COMP) $(SRC)\\main.c $(OBJ)\\*.o -I $(INCLUDE) -o $(BIN)\\main.exe $(CFLAGS)


# Run application
run:
	$(RUN)


# Clean all object files and bin files
clean:
ifeq ($(SYS),LINUX)
	rm -rf $(OBJ)/*.o
	find $(BIN)/* -type f ! -name ".gitkeep" -delete
else
	del /Q /F $(OBJ)\\*.o $(BIN)\\*.exe
endif


# Makefile documentation
help:
	@echo =================================================== Docs ===================================================
	@echo Commands:
	@echo$(DOT)
	@echo - make                      Compile all project to Linux systems
	@echo$(DOT)
	@echo - make all                  Compile all project to Linux systems
	@echo$(DOT)
	@echo - make linux                Compile all project to Linux systems
	@echo$(DOT)
	@echo - make windows              Compile all project to Windows system
	@echo$(DOT)
	@echo - make run                  Will run the main on both systems
	@echo$(DOT)
	@echo - make clean                Will clean all src/C/obj files and all src/C/bin files on both systems
	@echo$(DOT)
	@echo - make libed                Compile libs to Linux systems
	@echo$(DOT)
	@echo - make libed_windows        Compile libs to Windows system
	@echo$(DOT)
	@echo - make help                 Show the help guide
	@echo$(DOT)
	@echo - make docs                 Show the help guide
	@echo$(DOT)
	@echo Autors:
	@echo$(DOT)
	@echo - Arthur Negrão
	@echo - Francisco Braga
	@echo$(DOT)
	@echo Github repository of the project:
	@echo$(DOT)
	@echo - https://github.com/Arthur-Negrao-Smith/Projeto-Benchmark-Prog1.git
	@echo ============================================================================================================


# Makefile documentation
docs: help
