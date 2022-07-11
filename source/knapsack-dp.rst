.. _knapsack-dp.rst:

Le problème du sac à dos
########################

Le problème du sac à dos est un problème algorithmique classique connu pour être
NP-complet :cite:p:`Book1975-BOORMK-2`. Ce problème d'optimisation combinatoire
peut être formulé de très nombreuses manières et il existe de nombreuses
variantes du problème. Cette section présente la variante la plus simple et
classique, le **0-1 Knapsack Problem**. Comme ce problème est NP-complet, on ne
connaît pas d'algorithme efficace pour résoudre de manière exactes de grosses
instances du problème. Il existe de très nombreuses approches possibles pour ce
problème. Parmi les approches exactes, il y a notamment la programmation
dynamique et la programmation en nombres entiers (0-1 Integer Programming) qui
sont capables de résoudre de petites instances du problème. Pour résoudre les
instances plus grandes, il faut recourir à des méthodes par approximation que
nous n'aborderons pas ici.

Présentation du problème
========================

Présentation intuitive
----------------------

..  only:: html

    ..  youtube:: HvAK6HxZ190
        :align: center
        :width: 100%

..
    ..  only:: latex

        ..  raw:: latex

            \marginnote{salut}
            \qrcode[hyperlink,height=0.5in]{https://www.youtube.com/watch?v=HvAK6HxZ190}

La vidéo :cite:p:`parent:intro-sac-à-dos` présente le problème de manière
accessible à des étudiants du niveau gymnase. De manière intuitive, on peut
formuler le problème de la manière suivante:

Supposons que l'on prépare une longue randonnée qui exclut de pouvoir se
ravitailler en route et que l'on dispose d'un sac à dos de contenance limitée
(par exemple 50 litres), quels articles alimentaires faut-il y placer pour
maximiser la valeur nutritive emportée. Les articles considérés sont mentionnés
dans le tableau :ref:`table-knapsack-items-example-1`.

.. _table-knapsack-items-example-1:

..  csv-table:: Articles disponibles dans la réserve alimentaire
    :header-rows: 1
    :class: longtable

    No article, Description, Volume [L], Valeur nutritive [kcal]
    0, Paquet de pâtes, 13, 2600
    1, Paquet de pâtes, 13, 2600
    2, Paquet de pâtes, 13, 2600
    3, Pommes, 10, 500
    4, Riz, 24, 4500
    5, Yogurt, 11, 960

..  admonition:: Remarques

    Pour résoudre le problème, il faut prendre en compte les remarques suivantes:

    *   Pour optimiser les calculs et pour faciliter l'analyse de l'algorithme,
        on impose que tous les volumes et la capacité du sac soient des nombres
        entiers. Si, dans la vraie vie, les nombres ne sont pas entiers, on peut
        toujours transformer le problème en multipliant tous les volumes et la
        capacité par un facteur commun pour que les volumes et la capacité du
        sac à dos soient des nombres entiers.

    *   Chaque paquet de pâtes constitue un article à part entière et est donc
        noté dans une ligne à part entière dans le tableau.

    *   La colonne "Description" du tableau n'a aucune importance dans le
        problème. On ne prend en compte que la volume et la valeur nutritive des
        aliments.

    *   On ne peut pas "ouvrir" un paquet de pâtes pour prendre la moitié du
        paquet. Pour chaque article, soit on le prend complètement, soit on ne
        le prend pas du tout, d'où le nom du problème **0-1**-Knapsack Problem.

Formulation mathématique
------------------------

Mathématiquement, le problème peut se formuler de la manière suivante. Comme
pour tout problème d'optimisation combinatoire, on utilise des **variables de
décisions** pour formuler le problème, ainsi que des **contraintes** et une
**fonction objectif** à optimiser. On considère que :math:`N` est le nombre
d'objets emportés. Les données du problème sont les suivantes:

..  admonition:: Données connues du problème

    On peut représenter le problème à l'aide de trois listes 

    - La liste ``V`` chaque élément ``V[i]`` indiquent le volume de l'objet
      numéro :math:`i`.

    - Liste ``N`` dont chaque élément ``N[i]`` indiquent la valeur nutritive de
      l'objet numéro :math:`i`.

..  admonition:: Variables de décision

    Dans ce problème, les variables de décision sont des variables binaires
    :math:`x_i \in \{0, 1\}` définies de la manière suivante pour tout
    :math:`0 \leq i \leq N`,

    ..  math::

        x_i = \begin{cases}
        1 &\text{si on prend l'objet $i$} \\
        0 &\text{sinon} \\
        \end{cases}

    Pour l'instance considérée en exemple, il y a six variable de décision
    :math:`x_0, \ldots, x_5`, une pour chacun des articles que l'on peut
    potentiellement emporter.


..  admonition:: Contraintes

    Dans un problème d'optimisation combinatoire les contraintes doivent être
    respectées pour qu'une solution soit considéré comme valide (*feasible* en
    anglais). Dans le cas du problème du sac à dos, il n'y a qu'une seule
    contrainte, formulée comme une inéquation linéaire:

    ..  math::

        \sum_{i=0}^{N-1}
        x_i \cdot V[i]
        \leq 
        C

    Pour l'instance considérée en exemple, pour un sac à dos de 5 litres, la
    contrainte s'écrit

    ..  math::
        
        x_0 \cdot 13 + x_1 \cdot 13 + x_2 \cdot 13 + x_3 \cdot 10 + x_4 \cdot 24 + x_5 \cdot 11 \leq 50

..  raw:: latex

    \pagebreak

..  admonition:: Fonction objectif

    La fonction objectif indique la valeur qui doit être optimisée. Dans notre
    cas, il s'agit de la valeur nutritive totale emportée dans le sac à dos. En
    l'occurrence, la valeur objectif à optimiser est donnée par la fonction

    ..  math::

        f(X) = f(x_0, \ldots, x_{N_1}) = \sum_{i=0}^{N-1} x_i \cdot N[i]

    Pour l'instance considérée en exemple, la fonction objectif est donc

    ..  math::

        f(X) &= f(x_0, x_1, x_2, x_3, x_4, x_5) \\
        &= x_0 \cdot 2600 + x_1 \cdot 2600 + x_2
        \cdot 2600 + x_3 \cdot 500 + x_4 \cdot 4500 + x_5 \cdot 960

        
Résoudre le problème du sac à dos consiste à attribuer à chaque variable de
décision :math:`x_i` une valeur dans :math:`\{0, 1\}` de telle manière que
toutes les contraintes soient satisfaites. De plus, il faut trouver une solution
optimale, à savoir une solution qui maximise la fonction objectif :math:`f`.

Représentation du problème en Python
====================================

En Python, le problème peut être représenté comme suit:

..  literalinclude:: scripts/knapsack.py

Formulation de manière récursive
================================

Pour résoudre un problème avec la programmation dynamique, il faut commencer par
réduire le problème à un problème plus simple. Dans le cas du sac à dos, cela
est assez facile à faire. Si l'on sait résoudre le problème pour les :math:`N-1`
premiers articles du tableau, il suffit de considérer 