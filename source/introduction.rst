.. _introduction.rst:

Introduction
############

..
    Ce tutoriel présente le programmation dynamique, qui est une stratégie générale
    de résolution de problèmes du type "diviser pour régner". Elle est souvent
    utilisée pour résoudre de manière exacte des problèmes d'optimisation tels que
    le problème du sac à dos.

Qu'est-ce que la programmation dynamique?
=========================================

La programmation dynamique est une technique de résolution de problèmes
d'optimisation développée par Richard Bellman dès les années 1940. Elle revêt
une importance capitale en optimisation et en théorie du contrôle. Comme
l'explique Moshe Sniedovich dans l'introduction à son ouvrage
:cite:p:`DPFoundationsAndPrinciples` sur la programmation dynamique, tout le
monde n'est pas d'accord sur ce que recouvre vraiment la programmation dynamique
et il n'est pas aisé de donner une définition universellement acceptée du
concept de programmation dynamique:

..  epigraph:: 

    I started entertaining the idea of writing a book on dynamic programming
    when I first realized that in contrast to, say, linear programming, there
    seems to be a gentlemen’s disagreement as to what exactly dynamic
    programming is. Obviously, I envisioned a text that would offer a conclusive
    and incontestable formulation of dynamic programming. But I soon discovered
    that dynamic programming actually invites a certain amount of disagreement
    with respect to its definition because, by its very nature, it can be
    approached from a variety of angles depending on one’s approach to modeling,
    analysis and problem solving. We thus find the intuitionist at one end, the
    formalist at the other, and the rest somewhere in between. So, in this book
    I examine the question what is dynamic programming? knowing full well that
    whatever answer one formulates, by necessity it will be subjective in
    nature.

    --Moshe Sniedovich, Dynamic Programming: Foundations and Principles


Quoi qu'il en soit, on peut constater en parcourant la table des matières
d'ouvrages tels que :cite:p:`Bellman+2021` ou
:cite:p:`DPFoundationsAndPrinciples` que la programmation dynamique dépasse
largement le cadre de l'algorithmique et est davantage à rattacher aux
mathématiques. Le mot "programmation" dans "programmation dynamique" ne se
réfère à l'origine pas à la "programmation informatique", dans le sens de
contrôler un ordinateur pour résoudre un problème algorithmique. La
programmation dynamique, tout comme la programmation mathématique, ou
programmation linéaire, a vu le jour avant même l'existence des ordinateurs.
Dans ce contexte, il faut davantage comprendre le mot "programmation" au sens de
la "programmation d'un festival de musique" ou de la "programmation des cours
dans une école", à savoir de la résolution d'un problème d'optimisation.

Par la suite, les informaticiens ont constaté que les concepts et les méthodes
de cette discipline issue du domaine de l'optimisation pouvaient être adaptés à
la résolution de problèmes algorithmiques présentant une certaine structure.
C'est plutôt dans ce sens, restreint aux problèmes algorithmiques, que la
programmation dynamique est abordée dans ce travail. 


..
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

Problèmes typiques de la programmation dynamique
================================================

Pour qu'un problème puisse être avantageusement résolu par programmation
dynamique, il faut qu'il présente deux propriétés importantes. Il doit présenter
des **sous-structures optimales** (*optimal substructures* en anglais) et être
décomposables en sous-problèmes non disjoints (*overlapping subproblems* en
anglais).

..  admonition:: Sous-structures optimales

    De manière informelle, un problème d'optimisation présente des
    sous-structures optimales s'il est possible de construire une solution
    optimale pour le problème original à partir de solutions optimales de ses
    sous-problèmes.

..  admonition:: Sous-problèmes non disjoints

    Un problème possède des sous-problèmes non disjoints si, parmi les
    sous-problèmes, il y a des sous-sous-problèmes communs. C'est à ce niveau
    que la programmation dynamique apporte un gain de performance important
    puisqu'elle mémorise le résultat de tous les sous-problèmes résolus afin de
    pouvoir les réutiliser.

Différences avec l'approche "diviser pour régner"
=================================================

Le **diviser pour régner** (*Divide and Conquer* en anglais) est une stratégie
très utilisée en informatique pour résoudre des problèmes épineux. De manière
générale, cette stratégie procède de la manière suivante:

* Décomposer le problème à résoudre en sous-problèmes plus faciles à résoudre
* Continuer à décomposer les sous-problèmes en sous-sous-problèmes, jusqu'à ce que le problème soit trivial à résoudre
* Combiner les solutions des sous-problèmes pour résoudre le problème initial.

La stratégie du diviser pour régner fonctionne bien lorsque les sous-problèmes
sont disjoints, comme dans le cas du tri fusion ou de la recherche dichotomique. 

Lorsque les sous-problèmes sont non disjoints, l'application naïve d'une
stratégie de diviser pour régner débouche sur un algorithme très inefficace dont
la complexité est :math:`\Theta(2^n)` si :math:`n` est la taille de l'entrée.
C'est par exemple le cas si l'on calcule les nombres de Fibonacci de manière

Différences avec la stratégie gloutonne
=======================================

Certains problèmes d'optimisation peuvent être résolus par une approche
gloutonne. C'est notamment le cas de la recherche du plus court chemin
(single-source shortest path) dans un graphe pondéré positivement. L'algorithme
de Dijkstra constitue une telle méthode gloutonne.

Au contraire de la stratégie gloutonne qui, à chaque étape fait systématiquement
le choix localement optimal, la programmation dynamique envisage et explore
toutes les possibilités. À ce titre, la programmation dynamique se rapproche
fortement de la stratégie par "force brute". Il s'agit toutefois d'une stratégie
de force brute intelligente et efficace.

Au contraire de la méthode gloutonne qui ne garantit souvent pas une solution
optimale au problème d'optimisation global, la programmation dynamique vise et
garantit une solution globalement optimale.

Difficulté de la programmation dynamique
========================================

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

Pour comprendre au mieux la programmation dynamique, il faut avoir à l'esprit
qu'il s'agit d'une sorte de "motif de conception" d'algorithmes, d'une démarche
de résolution de problèmes. À ce titre, il faut absolument maîtriser et
comprendre parfaitement les mécanismes de la programmation récursive, en
particulier le modèle d'exécution des fonctions récursives. Un rappel détaillé
de ce modèle d'exécution est donné dans le chapitre
:ref:`fibonacci`. 

D'autre part, il ne faut pas s'arrêter ni s'intéresser à l'implémentation d'un
algorithme de programmation dynamique pour un problème particulier, mais tenter
de saisir les principes généraux de la programmation dynamique qui est un mode
de pensée. Le plus difficile en programmation dynamique est souvent d'identifier
les problèmes pouvant être résolus avec cette approche et de les reformuler de
manière adaptée à la programmation dynamique. Tout ceci doit être entraîné sur
de nombreux problèmes différents pour se faire la main.

En définitive, comme le dit le prof. Erik Demaine à ses étudiants du MIT
:cite:p:`mitocw:6.006:website, mitocw:6.006:lecture-19`, la programmation
dynamique est facile une fois qu'on en a compris les rouages.


Pour faciliter la compréhension du sujet, ce rapport par du calcul récursif des
nombres de Fibonacci dans le chapitre :ref:`fibonacci` et explique pourquoi cet
algorithme récursif est tellement inefficace en rappelant le modèe d'exécution
des fonctions récursives. Il présente également les outils de base de la
programmation dynamique pour améliorer la situation à l'aide de la mémoïsation
et l'approche duale ascendante (bottom-up) qui construit la solution
itérativement. Ces principes sont ensuite utilisés dans le chapitre
:ref:`knapsack-dp.rst` pour développer un algorithme de programmation dynamique
résolvent des instances et petite moyenne taille du sac à dos.

