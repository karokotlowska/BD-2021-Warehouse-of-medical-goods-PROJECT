CREATE SCHEMA magazyn;

CREATE TABLE magazyn.Rodzaj_operacji (
                rodzaj_operacji VARCHAR NOT NULL,
                opis VARCHAR NOT NULL,
                CONSTRAINT rodzaj_operacji_pk PRIMARY KEY (rodzaj_operacji)
);


CREATE SEQUENCE magazyn.kontrahent_id_firmy_seq;

CREATE TABLE magazyn.Kontrahent (
                id_firmy VARCHAR NOT NULL DEFAULT nextval('magazyn.kontrahent_id_firmy_seq'),
                nazwa VARCHAR NOT NULL,
                nip VARCHAR NOT NULL,
                numer_rachunku VARCHAR NOT NULL,
                CONSTRAINT kontrahent_pk PRIMARY KEY (id_firmy)
);


ALTER SEQUENCE magazyn.kontrahent_id_firmy_seq OWNED BY magazyn.Kontrahent.id_firmy;

CREATE TABLE magazyn.Pracownik_stanowisko (
                id_stanowisko VARCHAR NOT NULL,
                opis VARCHAR NOT NULL,
                CONSTRAINT pracownik_stanowisko_pk PRIMARY KEY (id_stanowisko)
);


CREATE SEQUENCE magazyn.pracownik_id_pracownik_seq;

CREATE TABLE magazyn.Pracownik (
                id_pracownik INTEGER NOT NULL DEFAULT nextval('magazyn.pracownik_id_pracownik_seq'),
                imie VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                nazwisko VARCHAR NOT NULL,
                CONSTRAINT pracownik_pk PRIMARY KEY (id_pracownik)
);


ALTER SEQUENCE magazyn.pracownik_id_pracownik_seq OWNED BY magazyn.Pracownik.id_pracownik;

CREATE TABLE magazyn.Weryfikacja (
                id_pracownik INTEGER NOT NULL,
                login VARCHAR NOT NULL,
                haslo VARCHAR NOT NULL,
                CONSTRAINT weryfikacja_pk PRIMARY KEY (id_pracownik)
);


CREATE TABLE magazyn.Pracownik_role (
                id_pracownik INTEGER NOT NULL,
                id_stanowisko VARCHAR NOT NULL,
                CONSTRAINT pracownik_role_pk PRIMARY KEY (id_pracownik, id_stanowisko)
);


CREATE SEQUENCE magazyn.zamowienie_numer_kolejny_seq;

CREATE SEQUENCE magazyn.zamowienie_id_firmy_seq;

CREATE TABLE magazyn.Zamowienie (
                numer_kolejny_zamowienia INTEGER NOT NULL DEFAULT nextval('magazyn.zamowienie_numer_kolejny_seq'),
                id_zamowienia VARCHAR NOT NULL,
                id_magazyn INTEGER NOT NULL,
                data_stworzenia VARCHAR NOT NULL,
                status VARCHAR NOT NULL,
                id_pracownik INTEGER NOT NULL,
                kwota NUMERIC(10,2),
                waluta_zamowienia VARCHAR NOT NULL,
                id_firmy VARCHAR NOT NULL DEFAULT nextval('magazyn.zamowienie_id_firmy_seq'),
                CONSTRAINT zamowienie_pk PRIMARY KEY (numer_kolejny_zamowienia)
);


ALTER SEQUENCE magazyn.zamowienie_numer_kolejny_seq OWNED BY magazyn.Zamowienie.numer_kolejny_zamowienia;

ALTER SEQUENCE magazyn.zamowienie_id_firmy_seq OWNED BY magazyn.Zamowienie.id_firmy;

CREATE SEQUENCE magazyn.zamowienie_szczegoly_id_zamowienie_seq_1;

CREATE TABLE magazyn.Platnosc (
                numer_kolejny_platnosci INTEGER NOT NULL DEFAULT nextval('magazyn.zamowienie_szczegoly_id_zamowienie_seq_1'),
                numer_kolejny_zamowienia INTEGER NOT NULL,
                status VARCHAR NOT NULL,
                sposob VARCHAR NOT NULL,
                data_zrealizowania DATE NOT NULL,
                kwota_platnosci NUMERIC NOT NULL,
                waluta_platnosci VARCHAR NOT NULL,
                CONSTRAINT platnosc_pk PRIMARY KEY (numer_kolejny_platnosci)
);


ALTER SEQUENCE magazyn.zamowienie_szczegoly_id_zamowienie_seq_1 OWNED BY magazyn.Platnosc.numer_kolejny_platnosci;

CREATE TABLE magazyn.Magazyn_lokalizacje (
                id_magazyn INTEGER NOT NULL,
                nr_magazynu INTEGER NOT NULL,
                ulica VARCHAR NOT NULL,
                kod_pocztowy VARCHAR(6) NOT NULL,
                miasto VARCHAR NOT NULL,
                CONSTRAINT magazyn_lokalizacje_pk PRIMARY KEY (id_magazyn)
);


CREATE TABLE magazyn.Kategoria (
                id_kategoria INTEGER NOT NULL,
                nazwa VARCHAR NOT NULL,
                CONSTRAINT kategoria_pk PRIMARY KEY (id_kategoria)
);


CREATE SEQUENCE magazyn.produkt_id_produkt_seq;

CREATE TABLE magazyn.Produkt (
                id_produkt INTEGER NOT NULL DEFAULT nextval('magazyn.produkt_id_produkt_seq'),
                opis VARCHAR NOT NULL,
                id_kategoria INTEGER NOT NULL,
                CONSTRAINT produkt_pk PRIMARY KEY (id_produkt)
);


ALTER SEQUENCE magazyn.produkt_id_produkt_seq OWNED BY magazyn.Produkt.id_produkt;

CREATE TABLE magazyn.Zamowienie_szczegoly (
                numer_kolejny_zamowienia INTEGER NOT NULL,
                id_produkt INTEGER NOT NULL,
                ilosc INTEGER NOT NULL,
                waluta VARCHAR(10) NOT NULL,
                cena NUMERIC(10,2) NOT NULL,
                CONSTRAINT zamowienie_szczegoly_pk PRIMARY KEY (numer_kolejny_zamowienia, id_produkt)
);


CREATE TABLE magazyn.Magazyn_stan (
                id_produkt INTEGER NOT NULL,
                id_magazyn INTEGER NOT NULL,
                ilosc INTEGER NOT NULL,
                CONSTRAINT magazyn_stan_pk PRIMARY KEY (id_produkt, id_magazyn)
);


CREATE SEQUENCE magazyn.magazyn_operacje_id_operacji_seq;

CREATE TABLE magazyn.Magazyn_operacje (
                id_operacji INTEGER NOT NULL DEFAULT nextval('magazyn.magazyn_operacje_id_operacji_seq'),
                id_produkt INTEGER NOT NULL,
                numer_kolejny_zamowienia INTEGER,
                data_operacji DATE NOT NULL,
                ilosc INTEGER NOT NULL,
                rodzaj_operacji VARCHAR NOT NULL,
                id_magazyn INTEGER NOT NULL,
                id_pracownik INTEGER NOT NULL,
                CONSTRAINT magazyn_operacje_pk PRIMARY KEY (id_operacji)
);


ALTER SEQUENCE magazyn.magazyn_operacje_id_operacji_seq OWNED BY magazyn.Magazyn_operacje.id_operacji;

ALTER TABLE magazyn.Magazyn_operacje ADD CONSTRAINT rodzaj_operacji_magazyn_operacje_fk
FOREIGN KEY (rodzaj_operacji)
REFERENCES magazyn.Rodzaj_operacji (rodzaj_operacji)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Zamowienie ADD CONSTRAINT kontrahent_zamowienie_fk
FOREIGN KEY (id_firmy)
REFERENCES magazyn.Kontrahent (id_firmy)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Pracownik_role ADD CONSTRAINT pracownik_stanowisko_pracownik_role_fk
FOREIGN KEY (id_stanowisko)
REFERENCES magazyn.Pracownik_stanowisko (id_stanowisko)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Zamowienie ADD CONSTRAINT pracownik_zamowienie_fk
FOREIGN KEY (id_pracownik)
REFERENCES magazyn.Pracownik (id_pracownik)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Pracownik_role ADD CONSTRAINT pracownik_pracownik_role_fk
FOREIGN KEY (id_pracownik)
REFERENCES magazyn.Pracownik (id_pracownik)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Weryfikacja ADD CONSTRAINT pracownik_weryfikacja_fk
FOREIGN KEY (id_pracownik)
REFERENCES magazyn.Pracownik (id_pracownik)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Magazyn_operacje ADD CONSTRAINT pracownik_magazyn_operacje_fk
FOREIGN KEY (id_pracownik)
REFERENCES magazyn.Pracownik (id_pracownik)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Zamowienie_szczegoly ADD CONSTRAINT zamowienie_zamowienie_szczegoly_fk
FOREIGN KEY (numer_kolejny_zamowienia)
REFERENCES magazyn.Zamowienie (numer_kolejny_zamowienia)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Platnosc ADD CONSTRAINT zamowienie_platnosc_fk
FOREIGN KEY (numer_kolejny_zamowienia)
REFERENCES magazyn.Zamowienie (numer_kolejny_zamowienia)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Magazyn_operacje ADD CONSTRAINT zamowienie_magazyn_operacje_fk
FOREIGN KEY (numer_kolejny_zamowienia)
REFERENCES magazyn.Zamowienie (numer_kolejny_zamowienia)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Magazyn_stan ADD CONSTRAINT magazyn_magazyn_stan_fk
FOREIGN KEY (id_magazyn)
REFERENCES magazyn.Magazyn_lokalizacje (id_magazyn)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Produkt ADD CONSTRAINT new_tablekategoria_produkt_fk
FOREIGN KEY (id_kategoria)
REFERENCES magazyn.Kategoria (id_kategoria)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Magazyn_stan ADD CONSTRAINT produkt_magazyn_stan_fk
FOREIGN KEY (id_produkt)
REFERENCES magazyn.Produkt (id_produkt)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Zamowienie_szczegoly ADD CONSTRAINT produkt_zamowienie_szczegoly_fk
FOREIGN KEY (id_produkt)
REFERENCES magazyn.Produkt (id_produkt)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE magazyn.Magazyn_operacje ADD CONSTRAINT magazyn_stan_magazyn_operacje_fk
FOREIGN KEY (id_produkt, id_magazyn)
REFERENCES magazyn.Magazyn_stan (id_produkt, id_magazyn)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;