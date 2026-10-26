# Animation du coulissement d'un blade

`Coulissement_Blade.gif` montre l'extraction et la réinsertion du tiroir droit. `Coulissement_Blade.mp4` fournit la même séquence en vidéo. Les maillages viennent des exports CAO ; ces pièces de guidage sont inchangées dans R4.

Le haut du quadrant, de la cloison et de la façade est masqué au-dessus de Z = 24 mm pour exposer les rainures. Cette coupe est uniquement visuelle ; aucune pièce CAO n'est modifiée. Les équipements et la visserie ne sont pas représentés. Les couleurs sont pédagogiques, les pièces sont prévues en noir.

Avant extraction réelle, défaire les fixations de façade et libérer les câbles. Soutenir le tiroir pendant le mouvement et lorsqu'il sort entièrement des rainures. Pour le remettre, engager les deux languettes ensemble, puis pousser sans forcer et refixer la façade.

Le mouvement de 220 mm est imposé pour l'illustration. Ce n'est pas une simulation mécanique ou une vérification de collision sur toute la course. Les jeux et entrées de rail restent à tester sur les pièces imprimées.

Reproduction : exécuter `python3 build_animation.py` avec NumPy et Pillow, puis convertir le GIF avec ffmpeg en H.264/yuv420p.
