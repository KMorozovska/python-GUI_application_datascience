import pandas as pd
from Constants import DATA_PATH


class ProduceData:

    def __init__(self):

        # importujemy zbior danych, a dokladniej pierwsze 50000 rekordow - kto odwazny moze zmienic na wiecej
        data = pd.read_csv('/home/kasia/PycharmProjects/lead-it/sources/paragony_ms.csv', sep=";", header=None,
                           decimal=",", nrows=50000).reset_index(drop=True)

        # drobne porzadki
        data.columns = ['ID_LOKALIZACJI', 'MIASTO', 'ID_PRODUKTU', 'NAZWA_PRODUKTU', 'HIER_MATERIAL_GR0_ID',
                        'HIER_MATERIAL_GR0_OPIS', 'HIER_MATERIAL_GR1_ID', 'HIER_MATERIAL_GR1_OPIS',
                        'HIER_MATERIAL_GR2_ID', 'HIER_MATERIAL_GR2_OPIS', 'HIER_MATERIAL_GR3_ID', 'ID_KLIENT', 'DATA',
                        'GODZ', 'NR_PARAGONU', 'POZ_PARAGONU', 'KASA', 'WARTOSC_BRUTTO', 'VAT', 'ILOSC']
        self.data = data.drop(["KASA", "POZ_PARAGONU"], axis=1)

    def list_of_products(self,datasource):

        if datasource=="all":
            # przygotowanie listy wszystkich produktow
            lista_produktow = self.data.loc[:, ["ID_PRODUKTU"]].drop_duplicates()
            lista_produktow = lista_produktow['ID_PRODUKTU'].tolist()
            lista_produktow = sorted(lista_produktow, key=str.lower)
            return lista_produktow

        else:
            # datasource == wybrany lokal
            wybrany_lokal = self.data.loc[self.data["ID_LOKALIZACJI"] == datasource]
            # przygotowanie listy produktow danego lokalu
            lista_produktow = wybrany_lokal.loc[:, ["ID_PRODUKTU"]].drop_duplicates()
            lista_produktow = lista_produktow['ID_PRODUKTU'].tolist()
            lista_produktow = sorted(lista_produktow, key=str.lower)
            return lista_produktow


    def analyse_corelated_products(self, datasource, wanted_product):

        if datasource == "all":
            datasource = self.data

        # wyszukanie wszystkich paragonow gdzie pojawily sie szukany produkt

        zawartosc_query = "ID_PRODUKTU == \"" + wanted_product + "\""

        lista_paragonow = datasource.query(zawartosc_query)["NR_PARAGONU"].drop_duplicates().tolist()

        zawartosc_query = 'NR_PARAGONU in ' + "[" + ", ".join(str(x) for x in lista_paragonow) + "]"

        # wszystkie obiekty kupione razem z Batony impulsowe 50
        datasource.query(zawartosc_query)[["ID_PRODUKTU", "NR_PARAGONU"]].sort_values(by="NR_PARAGONU")

        # pytamy ile bylo rzeczy na paragonie i zostawiamy tylko te gdzie paragon nie zawiera tylko i wylacznie jednego produktu
        paragony_z_wiecej_niz_jednym_produktem = \
            datasource.query(zawartosc_query)[["ID_PRODUKTU", "NR_PARAGONU"]].sort_values(by="NR_PARAGONU").groupby(
            ["NR_PARAGONU"])["NR_PARAGONU"].count().rename("Ilosc_rzeczy_na_paragonie").reset_index().query(
            'Ilosc_rzeczy_na_paragonie > 1')
        # paragony_z_wiecej_niz_jednym_produktem

        lista_roznorodnych_paragonow = paragony_z_wiecej_niz_jednym_produktem["NR_PARAGONU"].tolist()
        zawartosc_query = 'NR_PARAGONU in ' + "[" + ", ".join(str(x) for x in lista_roznorodnych_paragonow) + "]"

        interesujace_obiekty = datasource.query(zawartosc_query)[["ID_PRODUKTU", "NR_PARAGONU"]].sort_values(by="NR_PARAGONU")

        # wyswietlamy wszystkie obiekty kupione razem z Batony impulsowe 50 w takiej kolejnosci jak sie najczesciej powtarzaly
        interesujace_obiekty = interesujace_obiekty.groupby(['ID_PRODUKTU'])['ID_PRODUKTU'].count().rename(
            "Ilosc").reset_index().sort_values(by="Ilosc", ascending=False)


