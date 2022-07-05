Mémoïsation
###########

Un des principes fondamentaux de la programmation dynamique est de décomposer le
problème à résoudre en sous-problèmes et de recombiner les résultats des
sous-problèmes pour résoudre le problème initial.

..  only:: html

    ..  admonition:: Dessiner les arbres d'appels récursifs
        :class: info

        *   Voici un package cool qui permettra de dessiner les arbres d'appels
            récursifs :
            https://dev.to/bishalsarang/visualize-recursion-tree-with-animation-in-python-5357.

        *   https://github.com/mdaines/viz.js qui est un port de Graphviz dans le
            navigateur, à voir si c'est gérable ...

        *   Paraît pas mal non plus pour dessiner des graphes et des arbres :
            https://js.cytoscape.org/. C'est probablement la meilleure que j'ai
            trouvé.

Pour rappel, l'algorithme récursif de calcul du :math:`n`-ième nombre de
Fibonacci s'écrit de la manière suivante en Python:

..  only:: html

    ..  literalinclude:: scripts/fibonacci.py

..  only:: latex

    ..  literalinclude:: scripts/fibonacci.py
        :pyobject: fib

Nous avons déjà vu que cet algorithme est très inefficace, même pour des valeurs
de :math:`n` relativement faibles telles que :math:`n=50`. En considérant
l'arbre des appels récursifs, on comprend vite pourquoi cet algorithme récursif
est de complexité temporelle :math:`\Theta(2^n)`. 

..  only:: html

    En effet, l'appel ``fib(4)`` génère l'arbre d'appels récursifs suivant:

    ..  tab-set::

        ..  tab-item:: Visualisation dynamique

            ..  figure:: scripts/fibonacci-4.gif
                :align: center
                :width: 80%

                Arbre des appels récursifs à la fonction ``fib(n)`` pour :math:`n = 4`

        ..  tab-item:: Visualisation statique

            ..  figure:: scripts/fibonacci-4.png
                :align: center
                :width: 80%

                Arbre des appels récursifs à la fonction ``fib(n)`` pour :math:`n = 4`

..  only:: latex

    En effet, l'appel ``fib(4)`` génère l'arbre d'appels récursifs de la figure
    :ref:`fib-tree-4`

    ..  _fib-tree-4:

    ..  figure:: scripts/fibonacci-4.png
        :align: center
        :width: 50%

        Arbre des appels récursifs à la fonction ``fib(n)`` pour :math:`n = 4`

On constate que l'arbre représentant les appels récursifs est un arbre binaire
(incomplet) de hauteur :math:`n-1 = 3`. Si l'on augmente :math:`n` de 1, le
nombre de nœuds est presque multiplié par 2 comme le montre la figure
:ref:`fib-tree-5`.

..  _fib-tree-5:

..  figure:: scripts/fibonacci-5.png
    :align: center
    :width: 70%

    Arbre des appels récursifs à la fonction ``fib(n)`` pour :math:`n = 5`

Taille de l'arbre des appels récursifs
======================================