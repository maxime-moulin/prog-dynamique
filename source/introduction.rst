.. _introduction.rst:

Introduction
############

..  only:: html

    ..  danger::

        * installer l'extension https://sphinxcontrib-spelling.readthedocs.io/en/latest/install.html pour vérifier l'orthographe.

Ce tutoriel présente le programmation dynamique, qui est une stratégie générale
de résolution de problèmes du type "diviser pour régner". Elle est souvent
utilisée pour résoudre de manière exacte des problèmes d'optimisation tels que
le problème du sac à dos.

..  tip::

    La programmation dynamique est généralement perçue comme un sujet difficile.
    En réalité, cela vient du fait que les gens ont souvent tendance à vouloir
    appliquer une recette de cuisine toute faite, sans trop réfléchir à son
    fonctionnement. 

    Ce travail a pour objectif de présenter les principes de la programmation
    dynamique de manière compréhensible et progressive, pour que le lecteur
    puisse en comprendre les rouages et pour qu'il soit capable d'identifier les
    problèmes susceptibles d'être résolus par cette stratégie et de la mettre en
    œuvre concrètement dans différents contextes nouveaux.

Stratégie de diviser pour régner
================================

Le **diviser pour régner** (*Divide and Conquer* en anglais) est une stratégie
très utilisée en informatique pour résoudre des problèmes épineux. En effet, de
très nombreux problèmes peuvent être résolus en commençant par résoudre une
variante plus simple du problème en question.

De manière générale, cette stratégie procède de la manière suivante:

* Décomposer le problème à résoudre en sous-problèmes plus faciles à résoudre
* Continuer à décomposer les sous-problèmes en sous-sous-problèmes, jusqu'à ce que le problème soit trivial à résoudre
* Combiner les solutions des sous-problèmes pour résoudre le problème initial.

..  danger:: 

    Il faudrait ici restreindre les exemples à des cas qui sont typiquement
    résolus avec la programmation dynamique. On pourrait par exemple évoquer
    Bellman-Ford pour la recherche du plus court chemin.

Les algorithmes suivants, fort connus, utilisent par exemple cette stratégie:

* Le tri rapide
* La recherche dichotomique
* Le calcul récursif des termes de la suite de Fibonacci

Il arrive cependant assez souvent que l'application naïve d'une stratégie de
diviser pour régner débouche sur un algorithme très inefficace dont la
complexité est :math:`\Theta(2^n)` si :math:`n` est la taille de l'entrée. C'est
par exemple le cas si l'on calcule le :math:`n`-ième terme de la suite de
Fibonacci de manière récursive.

Pour rappel, le :math:`n`-ième terme de la suite de Fibonacci est défini
récursivement comme suit pour :math:`n \in \mathbb{N}`:

..  math:: 

    F(n) = \begin{cases}
    0 &\text{si $n = 0$} \\
    1 &\text{si $n = 1$} \\
    F(n-2) + F(n-1) &\text{sinon}
    \end{cases}

Le programme ci-dessous lance la fonction ``fib(n)`` pour :math:`n=5, 10, 20,
30, 40, 50` et chronomètre le temps d'exécution de l'appel.

..  literalinclude:: scripts/fib_timeit.py
    :linenos:

L'exécution de ce programme produit la sortie suivante:

::

    fib(5) -> 8, exécuté en 0.002 ms
    fib(10) -> 89, exécuté en 0.011 ms
    fib(20) -> 10946, exécuté en 1.121 ms
    fib(30) -> 1346269, exécuté en 132.518 ms
    fib(40) -> 165580141, exécuté en 16060.584 ms

On voit bien que l'algorithme n'est pas efficace, même pour des valeurs
relativement petites de :math:`n`. L'exécution de l'appel pour :math:`n=50` est
même tellement lente que le programme ne produit aucune sortie en temps
raisonnable. De nombreux problèmes intéressants tels que le problème du rendu de
pièces de monnaies ou du sac à dos présentent une structure permettant une
résolution par décomposition, qui est toutefois inefficace si l'on procède de
manière naïve.

La section :ref:`fibonacci-memoisation` explique pourquoi cet algorithme
récursif est tellement inefficace et comment utiliser la **mémoïsation**, une
technique fondamentale en programmation dynamique, pour rendre une telle
stratégie beaucoup plus efficace, en évitant de refaire plusieurs fois des
calculs déjà effectués au préalable.

La programmation dynamique sera ensuite appliquée à la résolution de plusieurs
problèmes simples qui permettront de dégager les traits généraux
d'implémentation de programmation dynamique. Nous terminerons par une
application à de petites instances du problème du sac à dos.
