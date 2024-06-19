from typing import Any
from django.core.management.base import BaseCommand
from ...models import Province

import pandas as pd
from sqlalchemy import create_engine
import os

#Importation des données excel de la nomenclature des secteurs d'activités 

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args: Any, **options: Any) -> str | None:
        #Lecture données excel de nomenclature des secteurs d'activités
        repertoire_script = os.path.dirname(os.path.abspath(__file__))
        file_name = "provinces_drc.xlsx"
        path_file = os.path.join(repertoire_script, file_name)
        # data = pd.read_csv(path_file, encoding="ISO-8859-1", delimiter=";")
        data = pd.read_excel(path_file)

        for index, row in data.iterrows():
            province = Province(
                name = row['name'],
                chef_lieu = row['chef_lieu'],
                superficie= row['superficie'],
                population = row['population'],
                rank = row['rank'])
            province.save()

        self.stdout.write(self.style.SUCCESS('Données importées avec succès depuis Excel vers la base de données'))


