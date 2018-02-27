CXX=g++
CXXFLAGS=-Wall -I.
OBJS=drzewo.o drzewo_main.o

pomg: drzewo.o drzewo_main.o
	$(CXX) $(CXXFLAGS) $(OBJS) -o drzewo_main.exe
	
.PHONY: clean

clean: 
	rm -f *.o *~ core *~
