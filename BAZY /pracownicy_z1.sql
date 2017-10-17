CREATE TABLE premia (
    id varchar(20) PRIMARY KEY,
	premia  NUMERIC
);


CREATE TABLE dzial (
    id integer(20) PRIMARY KEY,
    nazwa dzialu varchar(20),
    siedziba dzialu varchar(20)
);

CREATE TABLE pracownicy (
    id varchar (6) PRIMARY KEY,
    nazwisko varchar(20),
    imie varchar(20),
    stanowisko varchar(20),
    data_zatrudnienia varchar(23),
    placa NUMERIC,
    id_dzial INTEGER,
    premia NUMERIC DEFAULT 0,
    FOREIGN KEY(stanowisko) REFERENCES premia(id),
    FOREIGN KEY(id_dzial) REFERENCES dzial(id) 
);
