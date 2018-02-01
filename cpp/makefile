CXX=g++
CXXFLAGS=-Wall -I.
OBJS=lista.o lista_main.o

pomg: lista.o lista_main.o
	$(CXX) $(CXXFLAGS) $(OBJS) -o lista_main.exe
	
.PHONY: clean

clean: 
	rm -f *.o *~ core *~
