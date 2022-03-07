CREATE OR REPLACE FUNCTION magazyn.ListaProduktow()
RETURNS TABLE(id_produkt text , opis text)
LANGUAGE SQL AS
'
    SELECT id_produkt, opis FROM magazyn.produkt 
';



CREATE OR REPLACE FUNCTION magazyn.ListaProduktowMagazyn(id_magazynu integer)
RETURNS TABLE(id_produkt text , opis text)
LANGUAGE SQL AS
'
    SELECT p.id_produkt, p.opis FROM magazyn.magazyn_stan MS JOIN magazyn.produkt P  USING (id_produkt) WHERE id_magazyn = id_magazynu
';









CREATE OR REPLACE FUNCTION magazyn.kwota_za_produkt(kwota decimal, ilosc integer)
RETURNS decimal AS
$$
BEGIN
	RETURN kwota*ilosc;
END
$$
LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION magazyn.PobierzMaxKwoteZamowienia(kolumna text)
RETURNS TABLE(maks text)
LANGUAGE SQL AS
'
    SELECT MAX(kolumna) FROM magazyn.zamowienie 
';

CREATE OR REPLACE FUNCTION PobierzMinKwoteZamowienia(kolumna text)
RETURNS text
LANGUAGE SQL AS
'
    SELECT MIN(kolumna) FROM magazyn.zamowienie 
';

----------------------------------------------



CREATE VIEW magazyn.pracownik_view
as
select p.imie, p.nazwisko, p.email, ps.opis from magazyn.pracownik p join magazyn.weryfikacja w USING (id_pracownik) join magazyn.pracownik_role R USING (id_pracownik) JOIN magazyn.pracownik_stanowisko PS USING (id_stanowisko);



CREATE VIEW magazyn.magazyn_view
as
select ms.id_magazyn, ms.ilosc, p.opis, k.nazwa, l.nr_magazynu, l.ulica, l.miasto, l.kod_pocztowy FROM magazyn.magazyn_stan ms JOIN magazyn.produkt p USING (id_produkt)  JOIN magazyn.magazyn_lokalizacje l USING (id_magazyn) JOIN magazyn.kategoria k USING (id_kategoria);


CREATE VIEW magazyn.produkty_view
as
select p.opis, k.nazwa from magazyn.produkt p join magazyn.kategoria k USING (id_kategoria);


----------------------------------------------

CREATE OR REPLACE FUNCTION magazyn.magazyn_operacje_data() RETURNS TRIGGER AS $$
    BEGIN
        
        NEW.data_operacji=current_date;
		RETURN NEW;
    END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER magazyn_operacje_date
    BEFORE INSERT OR UPDATE ON magazyn.magazyn_operacje
    FOR EACH ROW EXECUTE PROCEDURE magazyn.magazyn_operacje_data();




CREATE OR REPLACE FUNCTION magazyn.zam_insert() RETURNS TRIGGER AS $$
    BEGIN
        IF EXISTS(SELECT 1 FROM magazyn.zamowienie z WHERE z.id_zamowienia = New.id_zamowienia ) THEN
            RAISE EXCEPTION 'Takie zamowienie już istnieje! Sprawdź poprawność danych';
        ELSE
            RETURN NEW;
        END IF;
    END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER zamowienie_insert
    BEFORE INSERT ON magazyn.zamowienie
    FOR EACH ROW EXECUTE PROCEDURE magazyn.zam_insert();




CREATE OR REPLACE FUNCTION magazyn.update_kwota() RETURNS TRIGGER AS $$
    DECLARE
		tmp decimal;
	BEGIN
		tmp=NEW.ilosc*NEW.cena;
		
		UPDATE magazyn.zamowienie SET kwota = kwota + tmp WHERE numer_kolejny_zamowienia=NEW.numer_kolejny_zamowienia;
		RETURN NEW;
    END;
$$ LANGUAGE 'plpgsql';


CREATE TRIGGER kwota_trigger
    AFTER INSERT OR UPDATE ON magazyn.zamowienie_szczegoly 
    FOR EACH ROW EXECUTE PROCEDURE magazyn.update_kwota();







CREATE OR REPLACE FUNCTION magazyn.default_kwota() RETURNS TRIGGER AS $$
    DECLARE
		tmp decimal;
	BEGIN
		NEW.kwota=0;
		RETURN NEW;
    END;
$$ LANGUAGE 'plpgsql';


CREATE TRIGGER kwota_trigger
    BEFORE INSERT ON magazyn.zamowienie
    FOR EACH ROW EXECUTE PROCEDURE magazyn.default_kwota();


----------------------------------------------


CREATE INDEX id_zamowienia ON magazyn.zamowienie 
(
    id_zamowienia
);




---------------------------

CREATE OR REPLACE FUNCTION magazyn.SzczegolyZamowienia(numer_kolejny integer)
RETURNS TABLE(opis text, ilosc integer, cena decimal, kwota decimal)
LANGUAGE SQL AS
'
SELECT  p.opis, ilosc, cena, magazyn.kwota_za_produkt(cena,ilosc) FROM magazyn.zamowienie_szczegoly JOIN magazyn.produkt P USING (id_produkt) JOIN magazyn.zamowienie Z USING (numer_kolejny_zamowienia) WHERE numer_kolejny_zamowienia = numer_kolejny
';





CREATE OR REPLACE FUNCTION magazyn.default_waluta_platnosc() RETURNS TRIGGER AS $$
	BEGIN
		NEW.waluta_platnosci='pln';
		RETURN NEW;
    END;
$$ LANGUAGE 'plpgsql';


CREATE TRIGGER waluta_platnosci_trigger
    BEFORE INSERT ON magazyn.platnosc
    FOR EACH ROW EXECUTE PROCEDURE magazyn.default_waluta_platnosc();





CREATE OR REPLACE FUNCTION magazyn.default_waluta_zamowienia() RETURNS TRIGGER AS $$
	BEGIN
		NEW.waluta_zamowienia='pln';
		RETURN NEW;
    END;
$$ LANGUAGE 'plpgsql';


CREATE TRIGGER waluta_zamowienia_trigger
    BEFORE INSERT ON magazyn.zamowienie
    FOR EACH ROW EXECUTE PROCEDURE magazyn.default_waluta_zamowienia();






CREATE OR REPLACE FUNCTION magazyn.default_waluta() RETURNS TRIGGER AS $$
	BEGIN
		NEW.waluta='pln';
		RETURN NEW;
    END;
$$ LANGUAGE 'plpgsql';


CREATE TRIGGER waluta_trigger
    BEFORE INSERT ON magazyn.zamowienie_szczegoly
    FOR EACH ROW EXECUTE PROCEDURE magazyn.default_waluta();




