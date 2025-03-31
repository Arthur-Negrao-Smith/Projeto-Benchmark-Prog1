# Defining the system
ifeq ($(OS),Windows_NT)
	SYS := WIN
else
	SYS := LINUX
endif


# Defining the dir paths to both systems
ifeq ($(SYS),LINUX)
	BIN = ./src/c/bin
	INCLUDE = ./src/c/include
	OBJ = ./src/c/obj
	SRC = ./src/c/src
	RUN = $(BIN)/main
else
	BIN = .\src\c\bin
	INCLUDE = .\src\c\include
	OBJ = .\src\c\obj
	SRC = .\src\c\src
	RUN = $(BIN)\\main.exe

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
		$(OBJ)/benchmark.o

	
# Compile to linux
linux: libed
	$(C_COMP) $(SRC)/main.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/main


# Generic flag to object.o files linux
$(OBJ)/%.o: $(SRC)/%.c $(INCLUDE)/%.h
	$(C_COMP) -c $< -I $(INCLUDE) -o $(OBJ)/$@


# Generic flag to object.o files windows
$(OBJ)\\%.o: $(SRC)\\%.c $(INCLUDE)\\%.h
	$(C_COMP) -c $< -I $(INCLUDE) -o $@


# Compile libs Windows
libed_windows:	\
	$(OBJ)\\benchmark.o \


# Compile to windows
windows: libed_windows
	$(C_COMP) $(SRC)\\main.c $(OBJ)\\*.o -I $(INCLUDE) -o $(BIN)\\main.exe $(CFLAGS)


# Run application
run:
	$(RUN)


# Clean all object files and bin files
clean:
ifeq ($SYS,LINUX)
	rm -rf $(OBJ)/*.o
	find $(SRC)/* -type f ! -name ".gitkeep" -delete
else
	del /Q /F $(OBJ)\\*.o $(BIN)\\*.exe
endif


help:
	@echo =================================================== Docs ===================================================
	@echo Commands:
	@echo.
	@echo - make                      Compile all project to Linux systems
	@echo.
	@echo - make all                  Compile all project to Linux systems
	@echo.
	@echo - make linux                Compile all project to Linux systems
	@echo.
	@echo - make windows              Compile all project to Windows system
	@echo.
	@echo - make run                  Will run the main on both systems
	@echo.
	@echo - make clean                Will clean all src/C/object.o files and all src/C/bin.o files on both systems
	@echo.
	@echo - make libed                Compile libs to Linux systems
	@echo.
	@echo - make libed_windows        Compile libs to Windows system
	@echo.
	@echo - make help                 Show the help guide
	@echo.
	@echo - make docs                 Show the help guide
	@echo.
	@echo Autors:
	@echo.
	@echo - Arthur Negrão
	@echo - Francisco Braga
	@echo.
	@echo Github of the project:
	@echo.
	@echo - https://github.com/Arthur-Negrao-Smith/Projeto-Benchmark-Prog1.git
	@echo ============================================================================================================


docs: help