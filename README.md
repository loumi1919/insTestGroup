Mon approche : 

Nous ne pouvons pas modifier la classe Item qui est jalousement surveillée par notre ami le "gobelin" :smiley:

J'ai crée une classe UpdateItem contenant les diverses containtes pour mettre à jour notre liste de items tout en améliorant le code pour une meilleur lisibilité et une meilleur adaptabilité quant à l'ajout de nouveaux items.

La classe GildedRose, exécute la methode appropriée de la classe UpdateItem pour chaque item en fonction de son nom. 
Ainsi il devient facile d'implémenter de nouveaux items spécifiques en ajoutant :

1. Une condition elif à la classe GildedRose.

2. Une fonction dans la classe UpdateItem contenant les contraintes de   mise à jour des valeurs sell_in, quality.

J'ai retravaillé le fichier "texttest_fixture" pour des tests unitaires plus poussés. 

