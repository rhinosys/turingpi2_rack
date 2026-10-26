[Read in English](../en/prompt.md)

# Prompt initial — texte intégral

Voici le **prompt initial fourni par le créateur du projet**, reproduit intégralement ci-dessous, sans modification. Le bouton de copie du bloc permet de récupérer tout le texte.

[Télécharger le fichier texte original](../assets/initial-prompt-fr.txt)

!!! note "Archive de conception"
    Ce prompt décrit le point de départ du projet. Les choix de ventilation, de cassettes complètes, de tunnels intégrés et les tolérances ont évolué depuis. Pour fabriquer la version actuelle, suivre la [notice V7](assembly.md), les [fichiers calibrés](files.md) et les [supports de rails R3](rails.md). Voir aussi la [chronologie](timeline.md).

## Prompt original

<div class="prompt-original" markdown="1">

```text
PROMPT — Rack 19" 4U « Blade » pour 2× Turing Pi 2 + 2× alim ATX, modélisé avec MCP SolidCraft
Ce fichier est un prompt autonome. Il est à donner tel quel à un agent (Claude Code, Claude Desktop…) qui a accès au serveur MCP SolidCraft. Il contient tout ce qu'il faut pour modéliser, vérifier et exporter le rack sans autre contexte.


0. Rôle et objectif
Tu es un ingénieur CAO. Tu modélises avec SolidCraft (CAO paramétrique open source en Rust, serveur MCP intégré) un châssis rack 19" 4U imprimable en 3D qui contient :

2 cartes Turing Pi 2 (format Mini-ITX), chacune sur un tiroir « blade » qui sort par l'avant ;
2 alimentations Cooler Master MWE Bronze 750 V3 (ATX 3.1, 230 V, 750 W, câbles fixes), une par carte, à l'arrière ;
2 ventilateurs 120 mm (un par carte), en paroi centrale.

Toutes les pièces doivent s'imprimer en PETG sur une Bambu Lab X1C (volume utile retenu : 240 × 240 × 210 mm), s'assembler avec des vis M3/M4 + écrous hexagonaux (pas d'inserts thermiques), et des biscuits imprimés entre quadrants.

Livrables : un design SolidCraft paramétrique, un STEP de l'assemblage, un 3MF par pièce imprimable, un rapport de vérification (section 11).


1. Sources de référence (à consulter si un doute subsiste)
Sujet
Source
Présentation Turing Pi 2
https://docs.turingpi.com/docs/turing-pi2-intro
Specs et ports I/O
https://docs.turingpi.com/docs/turing-pi2-specs-and-io-ports
Boîtier et refroidissement
https://docs.turingpi.com/docs/turing-pi2-specs-and-io-ports-case-and-cooling
Boîtier officiel Turing Mini ITX (référence de conception)
https://turingpi.com/product/turing-mini-itx-case/
MCP SolidCraft (outils, lancement)
https://github.com/bherbruck/solidcraft/blob/main/docs/mcp.md
Liste des commandes SolidCraft
https://github.com/bherbruck/solidcraft/blob/main/docs/features.md


Astuce : sur docs.turingpi.com, ajouter .md à l'URL donne la version markdown.
Faits retenus des docs Turing Pi
Format Mini-ITX, 170 × 170 mm.
Alimentation par connecteur ATX 24 broches standard → chaque carte reçoit le 24 broches de « son » alim.
4 slots M.2 2260/2280 NVMe au DOS de la carte (un par nœud) → il faut un dégagement sous la carte et un accès par le dessous.
2× SATA 3, 2× Ethernet 1 Gb/s, 2× USB 3.0, HDMI, micro-USB BMC, header USB 3.0 façade (20 broches), header Front I/O (Power LED, Status LED, Power, Reset), boutons KEY1 et BMC RESET.
4 headers ventilo JST 1,25 mm 4 broches (un par nœud) + 1 header ventilo boîtier 12 V.
Refroidissement : au moins un ventilateur fortement recommandé ; avec un flux d'air sur les modules, des dissipateurs passifs suffisent.
Le boîtier officiel laisse 15 mm de dégagement sous la carte (on reprend cette valeur pour les entretoises).
Alimentation Cooler Master MWE Bronze 750 V3 (230 V, ATX 3.1)
Format ATX standard, 150 (L) × 140 (P) × 86 (H) mm (revendeurs : « 140 × 150 × 86 mm »). À mesurer sur l'alim réelle avant de figer la pièce.
Ventilateur 120 mm sur une grande face, câbles fixes (non modulaire) → prévoir une zone de lovage des câbles devant l'alim.
Fixation par 4 vis UNC 6-32 sur la face arrière (motif ATX standard). Relever les positions des trous sur l'alim réelle.


2. Démarrage SolidCraft (MCP)
Lancer le serveur, idéalement en mode « bridgé » pour voir l'agent travailler :

solidcraft --control 7878 &

solidcraft-cli mcp --connect 127.0.0.1:7878 --allow-path "~/Documents/Claude/Projects/RAck Blade Turing PI2"

(Selon la version, les binaires peuvent s'appeler solvecraft / solvecraft-cli : la doc MCP utilise les deux noms. Vérifier avec --help.)

Si disponibles, copier les skills solidcraft-modeling, solidcraft-editing, solidcraft-checking du dépôt dans ~/.claude/skills/.
Avant toute modélisation, appeler list_commands (filtres sketch, solid, component, parameters) et relire les paramètres exacts de chaque commande. Les noms de paramètres de ce prompt (p0, p1, distance, operation…) viennent de la doc ; ceux de ta version font foi.
Outils MCP utilisés : set_parameter, batch (rollback automatique au premier échec), execute, inspect_design, measure, body_topology, screenshot, export, save, undo.
Règles de travail avec SolidCraft (projet jeune, à respecter)
Un batch par feature logique (une plaque, une série de trous…), puis measure + screenshot pour vérifier. Ne jamais enchaîner 50 features sans contrôle.
Un composant par pièce imprimable (component.create), plus un composant REF pour les gabarits (cartes, alims, ventilos) qui ne sera jamais exporté.
Tout dimensionner via des paramètres utilisateur (set_parameter), avec expressions (chassis_w / 2 - wall).
Sélection d'arêtes pour congés/chanfreins : récupérer les midpoints avec body_topology. Faire les congés en dernier et préférer les chanfreins (fillets et nommage persistant encore immatures d'après le ROADMAP).
Motifs de réduction de poids : dessiner UN hexagone (sketch.polygon.inscribed), le couper, puis répéter avec solid.pattern.rectangular (≤ ~60 occurrences par feature, découper en plusieurs zones si besoin). Ne PAS dessiner des centaines d'hexagones dans une seule esquisse (leçon tirée de Fusion, où une esquisse de 900 entités a bloqué le solveur).
save après chaque pièce terminée ; export STEP + 3MF à la fin de chaque pièce.


3. Repère et conventions
X = largeur (gauche → droite), 0 au plan médian du châssis. Gauche = X négatif.
Y = profondeur, 0 = face avant, +Y vers l'arrière.
Z = hauteur, 0 = dessous du plancher.
Unités : mm. Toutes les pièces sont symétriques gauche/droite : modéliser le côté droit (X > 0) puis solid.mirror sur le plan YZ.
Découpe en 4 quadrants : plan X = 0 (gauche/droite) et plan Y = 210 (avant/arrière).

(Pour mémoire : l'ancien modèle Fusion utilisait Y vertical et Z profondeur ; ici on passe en Z vertical.)


4. Paramètres (à créer en premier avec set_parameter)
Nom
Valeur
Commentaire
rack_face_w
482.6
Largeur face 19" (oreilles comprises)
rack_hole_x
232.55
½ entraxe trous rack (465,1 / 2)
u
44.45
1U
chassis_h
4*u - 1.3 = 176.5
4U moins jeu (l'ancien 180,81 dépassait 4U)
chassis_w
446
Largeur extérieure du châssis
half_w
chassis_w / 2 = 223


chassis_d
424
Profondeur totale
split_y
210
Plan de coupe avant/arrière
floor_t
4
Épaisseur plancher
top_t
3
Épaisseur capot (5 dans les zones biscuit)
wall_t
4
Parois latérales et arrière
div_t
10
Cloison centrale (X = −5 … +5), rainurée sur ses 2 faces
inner_h
chassis_h - floor_t - top_t = 169.5
Hauteur intérieure
bay_w
half_w - wall_t - div_t/2 = 214
Largeur utile d'une baie (X 5 → 219)
rail_blk
16
Bloc-rail extérieur (X 203 → 219), face rainurée à X = 203
ear_w
30
Largeur oreille (face avant)
ear_t
5
Épaisseur oreille
slot_l / slot_h
12 / 7
Lumières oblongues horizontales des oreilles
tp_board
170
Carte Mini-ITX
tp_pcb_t
1.6


standoff_h
15
Dégagement sous carte (NVMe)
standoff_d
7


tray_t
3
Fond du tiroir
tray_w
203 - 5 - 1 = 197
Corps du tiroir X 5,5 → 202,5 (langues de 2,9 mm en plus de chaque côté)
tray_d
195
Y = 6 … 201
rail_groove
3.4 × 3
Rainure de rail (épaisseur langue 3 + 0,4)
face_t
4
Façade du blade
psu_w / psu_d / psu_h
150 / 140 / 86
MWE Bronze 750 V3 (à mesurer)
fan
120
Ventilo 120 × 120 × 25
fanwall_y
212
Face avant de la paroi ventilos
psu_y0
chassis_d - wall_t - psu_d = 280
Face avant des alims
bay_cx
(5 + 203) / 2 = 104
Axe X d'une baie (droite) : carte, ventilo et alim y sont centrés
bisc_l / bisc_t / bisc_w
22 / 3 / 20
Biscuit standard
bisc_clear
0.2
Jeu biscuit (biscuit imprimé à −0,2)
hole_comp
0.2
Compensation trous PETG X1C
m3_clear / m4_clear
3.4 / 4.5
Passages de vis
m3_nut_af / m3_nut_h
5.8 / 2.6
Logement écrou M3
m4_nut_af / m4_nut_h
7.3 / 3.4
Logement écrou M4
hex_cell / hex_rib
14 / 2.4
Hexagones allègement (sur plats) / nervure



5. Implantation générale (vue de dessus, côté droit ; le gauche est symétrique)
Y=-4   façade blade (I/O Turing Pi + bouton + poignée + aération), devant le cadre

Y=0    cadre avant (montant X 203 → 223)

Y=6    ┌──────── tiroir blade 197 × 195 ────────┐

       │  carte Turing Pi 2 170×170, centrée X=104, Y=16…186

Y=201  └─────────────────────────────────────────┘

Y=210  ===== plan de coupe avant / arrière =====

Y=212  paroi ventilos (1× 120 mm par baie, centre X=104, Z=74)

Y=243  zone câbles 24 broches / lovage alim (~37 mm)

Y=280  alim MWE 750 V3, 150 × 140 × 86, centrée X=104, ventilo vers le HAUT

Y=420  paroi arrière (découpe alim + prise C14 accessible)

Y=424

Flux d'air : entrée façade (aérations autour de l'I/O) → au-dessus des modules → ventilo 120 mm (soufflant vers l'arrière) → zone alim → sortie par la grille arrière. Chaque alim aspire par le capot ajouré au-dessus d'elle et souffle par l'arrière.

Choix : la connectique Turing Pi est en façade (réseau et BMC accessibles devant le rack), les prises secteur à l'arrière. Le tiroir sort par l'avant ; prévoir ~250 mm de mou sur le câble 24 broches.


6. Gabarits de référence (composant REF, non exporté)
Créer ces volumes pour les contrôles d'interférence :

REF_TP2_R : PCB 170 × 170 × 1,6 posé à Z = floor_t + 4 + tray_t + standoff_h = 26, centré (X=104, Y=101). Volume d'encombrement au-dessus : 170 × 170 × 45 (modules + dissipateurs). Volume sous la carte : 170 × 170 × 12 (NVMe 2280 + dissipateur fin).
REF_PSU_R : 150 × 140 × 86, de (X=29, Y=280, Z=4) à (X=179, Y=420, Z=90).
REF_FAN_R : 120 × 120 × 25, derrière la paroi ventilos, centre (X=104, Z=74).
Miroirs gauche de chacun.

Trous de fixation Mini-ITX (repère carte, origine coin avant-gauche de la carte vu de dessus, à vérifier sur la carte réelle) : (6,35 ; 10,16), (6,35 ; 165,10), (163,83 ; 33,02), (163,83 ; 165,10). Entraxes : 157,48 et 154,94 mm, une paire décalée de 22,86 mm. Orienter la carte pour que le bord I/O soit côté façade (Y = 16).


7. Pièces à modéliser (nomenclature)
Toutes les tailles indiquées doivent tenir dans 240 × 240 × 210.

Réf
Pièce
Qté
Encombrement approx.
Q-AV-D / Q-AV-G
Quadrant avant (plancher + paroi latérale + rails + cadre avant)
1+1
223 × 210 × 176,5
Q-AR-D / Q-AR-G
Quadrant arrière (plancher + paroi latérale + paroi arrière + berceau alim)
1+1
223 × 214 × 176,5
CL-AV / CL-AR
Cloison centrale avant (rainurée 2 faces) / arrière
1+1
10 × 210 × 169,5
FW-D / FW-G
Paroi ventilos
1+1
214 × 169,5 × 6
TOP-AV-D/G, TOP-AR-D/G
Capots en L (rabat 15 mm sur paroi latérale)
4
223 × 214 × 18
EAR-D / EAR-G
Oreilles rack
1+1
30 × 176,5 × 5
BT-D / BT-G
Tiroir blade (fond + entretoises + langues de rail)
1+1
203 × 195 × 18
BF-D / BF-G
Façade blade (I/O, bouton, poignée, aération)
1+1
207 × 165 × 25
BIS
Biscuits 21,8 × 3 × 19,8
~20


BIS-X
Biscuit central 4 voies 21,8 × 3 × 21,8
2





8. Détail de construction
8.1 Quadrant avant droit Q-AV-D
Plancher : rectangle X 0 → 223, Y 0 → 210, extrusion floor_t (la cloison centrale se pose dessus entre X 0 et 5).
Paroi latérale : X 219 → 223, Y 0 → 210, Z 4 → 176,5 − 3 (le capot coiffe).
Cadre avant : montant vertical X 203 → 223, Y 0 → 6, Z 4 → 173,5. Il porte l'oreille (3 trous M4 + poches d'écrou, section 8.6) et reçoit les 2 vis moletées de la façade (trous M4 + poches d'écrou à X = 205,5, Z = 20 et 155). L'ouverture avant d'une baie est donc X 5 → 203 (198 mm) : le tiroir (197 mm) y passe.
Bloc-rail extérieur : X 203 → 219, Y 0 → 203, Z 4 → 14, collé à la paroi latérale. Rainure rail_groove dans sa face X = 203 : 3,4 de haut (Z 8 → 11,4) × 3 de profondeur (jusqu'à X = 206). Chanfrein d'entrée 2 × 45° à Y = 0. Allégement possible par évidement du bloc (garder 2,4 mm de paroi).
Butée arrière du tiroir à Y = 203.
Allègement : motif hexagonal traversant sur le plancher, hors zones : bande de 15 mm le long des bords et des coutures, zones biscuit (Ø 40 autour de chaque biscuit), sous les rails. Idem sur la paroi latérale (laisser 15 mm de cadre).
Joints de couture (voir 9).
8.2 Quadrant arrière droit Q-AR-D
Plancher X 0 → 223, Y 210 → 424, épaisseur 4.
Paroi latérale X 219 → 223, Y 210 → 424.
Paroi arrière X 0 → 223, Y 420 → 424, Z 4 → 173,5.
Découpe alim : ouverture 140 × 76 centrée sur la face arrière de l'alim (centre X = 104, Z = 4 + 43 = 47), plus les 4 trous 6-32 (Ø 3,8, positions relevées sur l'alim) avec logements d'écrou 6-32 côté extérieur, ou trous Ø 3,3 pour vis auto-taraudeuses.
Grille d'aération hexagonale au-dessus de l'alim (Z 100 → 165) sur 180 mm de large.
Berceau alim : deux réglettes longitudinales 10 × 140 × 6 au sol (X = 33 et X = 165), une butée avant à Y = 278 de 8 mm de haut, et deux pattes pour une sangle velcro (fente 25 × 3) — l'alim est tenue par ses 4 vis arrière + la sangle.
Sous l'alim : plancher plein (pas de vent par le bas, le ventilo de l'alim est en haut).
Allègement hexagonal du plancher entre la paroi ventilos et l'alim (Y 243 → 275) et sur la paroi latérale.
8.3 Cloisons centrales CL-AV / CL-AR
Plaque X −5 → +5 posée sur le plancher, hauteur 169,5. CL-AV a une rainure rail_groove sur chaque face (Z 8 → 11,4, 3 mm de profondeur, âme restante 4 mm), même chanfrein d'entrée. Fixation au plancher : 4 pattes de 15 × 15 × 4 de chaque côté, vis M4 traversant le plancher, écrou côté pattes. Fixation haute : 2 vis M4 dans le capot. CL-AR : simple cloison avec passe-câbles, sans rails. Allègement hexagonal sur les deux.
8.4 Paroi ventilos FW-D
Plaque 214 × 169,5 × 6 à Y 212 → 218, X 5 → 219.

Trou Ø 116 pour le ventilo, centre (X = 104, Z = 74), 4 trous M4 à 105 mm d'entraxe, écrous côté ventilo.
Encoche passe-câbles 40 × 25 en bas, côté cloison, pour le 24 broches et le câble ventilo.
Fixation : pattes vissées au plancher arrière (M4) et à la paroi latérale.
8.5 Capots TOP (4 pièces)
Plaque top_t = 3 couvrant le quadrant + rabat de 15 mm vers le bas sur l'extérieur de la paroi latérale (profil en L), vissé par 3 vis M4 dans la paroi (écrous dans des poches côté intérieur). Épaississement à 5 mm dans les zones de biscuit. Capots arrière : grille hexagonale Ø 130 au-dessus du ventilo de chaque alim (centre X = 104, Y = 350). Capots avant : allègement hexagonal sur la zone au-dessus des cartes (favorise l'évacuation de chaleur).
8.6 Oreilles EAR-D
Plaque frontale X 211,3 → 241,3 (30 mm), Y −5 → 0, Z 0 → 176,5.
Pas de retour sur l'extérieur de la paroi latérale : l'ouverture d'un rack fait 450 mm (±225), un retour au-delà de X = 223 toucherait les montants. L'oreille recouvre le cadre avant sur X 211,3 → 223 et y est fixée par 3 vis M4 dans l'axe Y (Z = 30, 88, 146), écrous dans des poches au dos du cadre avant.
6 lumières oblongues horizontales 12 × 7 centrées sur X = 232,55, aux hauteurs standard 4U : Z = 6,35 ; 38,1 ; 66,675 ; 111,125 ; 139,7 ; 171,45.
Chanfrein 1 mm sur les arêtes frontales.
8.7 Tiroir blade BT-D
Fond 197 × 195 × 3 à X 5,5 → 202,5, Y 6 → 201, Z 8 → 11.
Langues de rail : sur les deux bords longs, langue de 3 mm d'épaisseur × 2,9 mm de saillie (X 2,6 → 5,5 et X 202,5 → 205,4), à Z 8,2 → 11,2 : 0,2 mm de jeu en hauteur et 0,1 mm en fond de rainure.
4 entretoises Ø 7 × 15 aux trous Mini-ITX (section 6), trou M3 traversant Ø 3,4 + logement d'écrou M3 sous le fond (hexagone 5,8 sur plats, 2,6 de profondeur). Vis M3 × 22 depuis le dessus de la carte.
Fenêtre NVMe dans le fond sous la zone M.2 (≈ 150 × 120, à confirmer sur la carte), bords chanfreinés : accès aux 4 SSD en sortant le blade et en le retournant, sans démonter la carte.
Allègement hexagonal sur le reste du fond.
Nervures de rigidité 3 × 8 le long des bords longs (sous le fond, hors rainures).
Face avant du tiroir : 4 trous M3 pour visser la façade BF.
8.8 Façade blade BF-D
Plaque 207 × 165 × 4 à Y −4 → 0 (en appui sur le cadre avant et le chant avant de la cloison), X 1 → 208, Z 6 → 171. Elle s'arrête à X = 208 pour laisser passer l'oreille (qui commence à X = 211,3) : le blade sort sans démonter les oreilles. Fixée au tiroir par 4 vis M3.
Découpe I/O : ouverture standard Mini-ITX 158,75 × 44,45 alignée sur le bord I/O de la carte (bas de l'ouverture ≈ dessus PCB − 2 mm, soit Z ≈ 25,6). À recaler sur les connecteurs réels ; option : importer le CAD officiel de l'I/O panel Turing (STEP) avec open/file.insert_step.
Bouton power Ø 16 (bouton antivandale à LED, câblé sur le header Front I/O), à Z = 120, X = 180.
Trou BMC RESET Ø 3 (accès à l'aiguille) — position à relever sur la carte.
Grille d'aération hexagonale Z 80 → 160 sur toute la largeur hors bouton.
Poignée : arceau 90 × 25 × 12, à Z ≈ 100, 2 vis M4.
2 vis moletées M4 (tête Ø ≤ 8) à X = 205,5, Z = 20 et 155, vissées dans le cadre avant.
Étiquette gravée 0,6 mm : « NODE A » (droite) / « NODE B » (gauche) avec sketch.text + coupe.


9. Assemblage entre quadrants
9.1 Biscuits
Biscuit 22 × 3 × 20, imprimé à 21,8 × 3 × 19,8 (−0,2 mm, bisc_clear).
Poches de 22 × 20 × 3,2 de profondeur, ouvertes sur la face extérieure (dessous du plancher, dessus du capot), à cheval sur la couture (11 mm de chaque côté).
Plancher épaissi localement à 6 mm (pastille intérieure 40 × 40) au droit de chaque poche pour garder 2,8 mm de matière ; capot épaissi à 5 mm.
Couture X = 0 (longueur 424) : biscuits à Y = 50, 130, 290, 370.
Couture Y = 210 (largeur 446) : biscuits à X = ±60, ±160.
Biscuit central 4 voies à (X = 0, Y = 210) : 4 quarts de poche 11 × 11 (un par quadrant) formant une poche 22 × 22, biscuit carré 21,8 × 3 × 21,8. Même chose sur les capots.
9.2 Vis
Couture Y = 210 : sur chaque paroi latérale, deux pattes de recouvrement 20 × 20 × 4 (Z = 40 et Z = 140), vis M4 × 16 + écrou en poche.
Couture X = 0 : la cloison centrale et ses pattes M4 bridgent les deux planchers ; ajouter 3 pattes M4 sous le plancher (Y = 90, 210, 330) si l'essai montre du jeu.
Toutes les poches d'écrou : hexagone orienté pour s'imprimer sans support (pointe vers le haut quand la pièce est sur le plateau).


10. Règles d'impression (PETG, X1C)
Trous : diamètre nominal + hole_comp (0,2). Passages M3 = 3,4 ; M4 = 4,5.
Épaisseur mini des parois : 2,4 mm (6 lignes de 0,4). Nervures hexagonales : 2,4 mm.
Surplombs ≤ 45° ; lumières horizontales et grandes ouvertures avec un chanfrein ou un toit en losange plutôt qu'un plafond plat.
Orientation conseillée : planchers/quadrants à plat (plancher sur le plateau), capots face extérieure sur le plateau, façades face avant sur le plateau, tiroirs fond sur le plateau, oreilles à plat.
Chanfrein 0,6 mm sur toutes les arêtes au contact du plateau (anti pied d'éléphant).


11. Vérifications obligatoires (rapport à produire)
Pour chaque pièce, puis pour l'ensemble, rapporter les résultats chiffrés :

Bounding box (measure) de chaque pièce ≤ 240 × 240 × 210 dans son orientation d'impression. Lister les valeurs.
Largeur hors tout oreilles comprises = 482,6 ± 0,5 ; largeur châssis = 446 ; hauteur ≤ 177,0 ; profondeur = 424.
Lumières d'oreilles centrées sur X = ±232,55 aux 6 hauteurs listées.
Interférences (inspect.interference) nulles entre : gabarits REF et pièces ; tiroir ↔ rails (jeu 0,2 visé dans les rainures) ; façade ↔ cadre ; alim ↔ berceau ; ventilo ↔ capot.
Dégagement sous carte ≥ 12 mm (NVMe) et fenêtre NVMe couvrant les 4 slots M.2.
Course du tiroir : le blade sort de 195 mm sans toucher la paroi ventilos.
Le connecteur 24 broches de l'alim atteint la carte tiroir sorti (longueur de câble à prévoir indiquée dans le rapport).
Contrôle visuel : screenshot iso, front, top, back de l'assemblage, + un iso par pièce.
Volumes et masse PETG estimée (densité 1,27 g/cm³) par pièce et au total.

Si un contrôle échoue : corriger avec timeline.edit ou set_parameter, recalculer, refaire le contrôle. Ne pas livrer avec un échec non signalé.


12. Export
save : RackTuringPi2_SolidCraft.solidcraft dans le dossier du projet.
export STEP de l'assemblage complet (avec REF dans un fichier séparé ..._with_ref.step).
export 3MF par pièce imprimable dans exports/3mf/, nommé selon la référence (section 7), orientée pour l'impression, en un seul exemplaire (les biscuits : un 3MF avec les 20 + 2).
Fichier BOM.md : pièces imprimées, vis (M3 × 22 ×8, M4 × 12/16 avec écrous, vis moletées M4 ×4, vis 6-32 alim ×8), 2 ventilos 120 mm 12 V, 2 boutons Ø 16 à LED, 2 sangles velcro 25 mm, 2 rallonges 24 broches si nécessaire.


13. Points à confirmer avec l'utilisateur avant de figer
Dimensions exactes et motif des 4 trous arrière de la MWE Bronze 750 V3 (mesure réelle).
Position réelle des connecteurs I/O, du bouton BMC RESET et de la zone M.2 sur la carte Turing Pi 2 (version de carte : 2.4 ou 2.5).
Connectique en façade (choix actuel) ou à l'arrière.
Hauteur des dissipateurs des modules (RK1 / CM4 / Jetson) si elle dépasse 45 mm.
```

</div>
