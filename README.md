Mon approche : 

Nous ne pouvons pas modifier la classe Item qui est jalousement surveillée par notre ami le "gobelin" :smiley:

Nous allons créer une classe UpdateItem contenant les diverses containtes pour mettre à jour notre liste de items tout en améliorant le code pour une meilleur lisibilité et une meilleur adaptabilité quant à l'ajout de nouveaux items.

La classe GildedRose, exécute la methode appropriée de la classe UpdateItem pour chaque item en fonction de son nom. 
Ainsi nous pouvons implémenter de nouveaux items spécifiques en ajoutant :

. Une condition elif à la classe GildedRose ;
. Une fonction dans la classe UpdateItem contenant les contraintes de   mise à jour des valeurs sell_in, quality.

Nous avons retravaillé le fichier "texttest_fixture" pour des tests plus poussés. 

