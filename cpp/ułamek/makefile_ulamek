CXX=g++
CXXFLAGS=-Wall -I.
OBJS=ul_ulamek.o ul_main.o

pomg: ul_ulamek.o ul_main.o
	$(CXX) $(CXXFLAGS) $(OBJS) -o ul_main.exe
	
.PHONY: clean

clean: 
	rm -f *.o *~ core *~
