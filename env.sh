#!/bin/bash















# Définir et exporter la variable d'environnement USER_NAME
export DB_HOST='localhost'
export DB_USER='root'
export DB_PASSWORD='uimm'
export DB_NAME='test_db'
export TABLE_NAME='membres'

echo "La variable d'environnement est définie avec la valeur : $DB_HOST"
echo "La variable d'environnement est définie avec la valeur : $DB_USER"
echo "La variable d'environnement est définie avec la valeur : $DB_PASSWORD"
echo "La variable d'environnement est définie avec la valeur : $DB_NAME"
echo "La variable d'environnement est définie avec la valeur : $TABLE_NAME"