# Defining the system
ifeq ($(OS),Windows_NT)
	SYS := WIN
else
	SYS := LINUX
endif

# Defining the dir paths
ifeq ($SYS,LINUX)
	BIN := ./src/C/bin
	INCLUDE := ./src/C/include
	OBJ := ./src/C/obj
	SRC := ./src/C/src
else
	BIN := src\C\bin
	INCLUDE := src\C\include
	OBJ := src\C\obj
	SRC := src\C\src
endif

# General variables
COMPILER = gcc
CFLAGS = -O2 -Wall -Wextra
