# Calibration V7 — 25 octobre 2026

Résultats communiqués par l'utilisateur sur la planche Rack Tolerance, en PETG HF noir : ajustements obtenus sans ponçage ni ébavurage.

| Interface | Valeur retenue |
|---|---:|
| Biscuit rectangulaire J | jeu TOTAL XY 0,2 mm |
| Biscuit central X | jeu TOTAL XY 0,2 mm |
| Passage de vis M3 | diamètre 3,2 mm |
| Passage de vis M4 | diamètre 4,3 mm |
| Logement écrou M3 | 5,7 mm entre plats |
| Logement écrou M4 | 7,2 mm entre plats |

L'orientation des essais d'écrous n'a pas été précisée. Ne pas présenter les deux orientations de la planche comme individuellement validées.

Le jeu des biscuits était déjà de 0,2 mm et reste inchangé. Les 57 esquisses de logements d'écrous héritées comportaient des dimensions numériques : leurs sommets ont été redimensionnés autour de leur centre, en plus des paramètres utilisateur. Les passages de vis codés numériquement ont été raccordés aux paramètres M3/M4.

Aucune conclusion supplémentaire n'est déduite pour les glissières, la profondeur des biscuits, les doigts de jonction ou les passages de filament. Le diamètre de passage du filament reste à 2,1 mm, à qualifier avec le plateau optionnel 11.

`update_source.py` reproduit la révision depuis `V7_avant_calibration.solidcraft`. Le candidat doit être ouvert, recalculé, mesuré et enregistré par SolidCraft avant de devenir le modèle livré. Les réponses MCP sont conservées dans `verification/`.

L'opération historique 909 de dégagement d'entrée échoue après recalibration. Deux variantes de découpe ont aussi échoué et n'ont pas été conservées. L'opération est désactivée, avec contrôle d'interférence sur les corps résultants, puis en extraction. Cette désactivation retire une correction numérique nominale de 0,05 mm ; elle ne constitue pas une nouvelle calibration physique des guides.
