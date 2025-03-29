# Defining the system
ifeq ($(OS),Windows_NT)
	SYS := WIN
else
	SYS := LINUX
endif

# Defining the dir paths
ifeq ($SYS,LINUX)
	BIN := ./src/c/bin
	INCLUDE := ./src/c/include
	OBJ := ./src/c/obj
	SRC := ./src/c/src
else
	BIN := src\c\bin
	INCLUDE := src\c\include
	OBJ := src\c\obj
	SRC := src\c\src
endif

# General variables
COMPILER = gcc
CFLAGS = -O2 -Wall -Wextra
