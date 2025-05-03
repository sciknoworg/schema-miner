## Supplementary Material for 'In Silico Design of a Thermal Atomic Layer Etch Process of Cobalt'

Suresh Kondati Natarajan, 1, a) Michael Nolan, 2, 3 Patrick Theofanis, 4 Charles Mokhtarzadeh, 4 and Scott B. Clendenning 4

1) Department of Electrical Engineering and Automation, Aalto University,

Espoo 02150, Finland

- 2) University College Cork, Tyndall National Institute, Lee Maltings, Dyke Parade, Cork, T12 R5CP, Ireland.

3) Nanotechnology and Integrated Bioengineering Centre, Ulster University,

Shore Road, Co Antrim, BT37 OQB Northern Ireland.

- 4) Intel Corporation, 2501 NE Century Blvd., Hillsboro, Oregon, USA 97124

(Dated: 20 November 2020)

a) Electronic mail: suresh0807@gmail.com

## S1: BADER CHARGE ANALYSIS

A table with computed Bader charges for a variety of Co materials.

TABLE S1. List of Bader valence charges of Co containing materials and molecules.

| Material               | Bader Valence Charge (computed / atom)   |
|------------------------|------------------------------------------|
| Bulk Co                | Co 0 (9.0e / 9.0e)                       |
| Co (2 0 1) surf        | Co 0 (8.9e - 9.1e / 9.0e)                |
| Bulk CoO               | Co 2+ (7.9e / 9.0e) O 2 - (7.1e / 6.0e)  |
| (C 3 H 5 )Co(CO) 3     | Co 1+ (8.45e / 9.0e)                     |
| (C 4 H 6 )Co(CO) 6     | Co 1+ (8.5e / 9.0e)                      |
| (SiH 3 )Co(CO) 4       | Co 1+ (8.38e / 9.0e)                     |
| (Si(CH 3 ) 3 )CO(CO) 4 | Co 1+ (8.32e / 9.0e)                     |

The computed valence electronic charge on the target Co adatom before adsorption of propene is 8.92. The higher coordinated surface Co atom neighbouring this atom is mildly reduced to compensate the above and has a computed Bader charge of 9.11 (see Figure S1). Table S2 shows the valence electronic charges on the target cobalt atom and the atoms of the propene molecule in the first and second pulse.

| Atom   | Structures   | Structures   | Structures   | Structures   | Structures   | Structures   |
|--------|--------------|--------------|--------------|--------------|--------------|--------------|
|        | Non-int      | A            | B            | C            | Vol.         | sp.          |
| Co T   | 8.92         | 8.79         | 8.74         | 8.47         | 8.46         |              |
| C1     | 4.04         | 4.15         | 4.20         | 4.24         | 4.21         |              |
| C2     | 3.97         | 4.13         | 4.19         | 4.12         | 4.16         |              |
| C3     | 4.23         | 4.24         | 4.17         | 4.31         | 4.13         |              |
| H1     | 0.97         | 0.99         | 1.24         | 1.25         |              |              |
| H2     | 0.96         | 0.92         | 0.89         | 0.88         | 0.90         |              |
| H3     | 0.98         | 0.90         | 0.94         | 0.87         | 0.91         |              |
| H4     | 0.95         | 0.92         | 0.90         | 0.88         | 0.90         |              |
| H5     | 0.91         | 0.91         | 0.90         | 0.84         | 0.95         |              |
| H6     | 0.99         | 0.90         | 0.95         | 0.87         | 0.89         |              |
| C4     | 2.89         |              |              | 3.55         | 3.08         |              |
| O1     | 7.11         |              |              | 7.06         | 7.09         |              |
| C5     | 2.89         |              |              | 3.65         | 3.07         |              |
| O2     | 7.11         |              |              | 7.06         | 7.11         |              |
| C6     | 2.89         |              |              | 3.57         | 3.06         |              |
| O3     | 7.11         |              |              | 7.08         | 7.09         |              |

TABLE S2. Bader valence charge of the atoms in the minimum energy geometries. The C (1-3) and H atoms are indexed according to Figure 7 of main text. The C (4-6) and O (1-3) correspond to the CO molecules. The Non-interacting geometries refer to isolated Co surface with target Co adatom and isolated propene/ CO molecules in vacuum. Structure A refers to the structure in which the propene molecule is adsorbed non-dissociatively on the Co surface and structure B refers to the case where Cl-H1 bond is broken. The Bader charges of the atoms in the volatile species are also given. Structure C refers to the case where the CO molecules are adsorbed on the surface.

A) Clean Co surface

<!-- image -->

- C) Propene adsorbed on adatom

## B) Co surface with adatom

<!-- image -->

- D) Propene dissociated on adatom

<!-- image -->

<!-- image -->

FIG. S1. The atoms in the simulation box are color coded according to the valence charge computed with Bader charge partitioning scheme. The bare surface is given in A) while the surface with adatom is given in B). In C) a propene molecule is adsorbed on the surface (note that the propene molecule is intact and we have not shown the periodic images) and a H atom is dissociated from the propene molecule in D). The color bar values show the variation in valence charge in which the positive value means oxidation (blue) and negative value means reduction (red).

## S2: CO BULK AND SURFACE MODELS

Figure S2a shows the HCP symmetry of bulk Co. The total DOS of bulk Co is also given in Figure S2b and a clear distinction between the spin up and spin down electrons is possible due to the spin polarized treatment of the electronic structure of cobalt which is ferromagnetic. Figure S2c and S2d shows the top and side view of the 5 layered Co (2 0 1) surface chosen for this study. From the side view it is clear that this surface has height corrugations that make it more reactive to the reactant molecules as compared to the ideal flat (1 1 1) surface.

FIG. S2. Geometry of Bulk Co is shown in a). The computed total density of states of bulk Co is shown in b) and a spin-polarized treatment of the electronic structure is necessary to observe the ferromagnetic properties of Co. Top and side views of bare Co(2 0 1) surface are shown in c) and d), respectively. The blue region indicates the atoms used in the DFPT calculation.

<!-- image -->

## S3: REACTION ENERGIES WITHOUT CO RESIDUE

TABLE S3. Reaction free energies (∆ G ) of the postulated overall ALE reactions at 0 K and 500 K. The energy values are given in eV and are given per Co removed. ∆ G a and ∆ G s refer to free energies when an adatom (Co ) and surface atom (Co ) are etched, respectively. a s ∆ G s -∆ G a is the free energy difference between removing a Co s and the Co . Co a surf refers to the clean (0 0 1) surface of Co and Co surf -x refers to the same surface with x atoms removed from the top layer. Reactant pressure used is 0.2 Torr and product pressure used is 0.01 Torr.

|    | Reactions                                                               | at 0 K   | at 0 K   | (∆ G s -   | at 500 K   | at 500 K   | (∆ G s -   |
|----|-------------------------------------------------------------------------|----------|----------|------------|------------|------------|------------|
|    |                                                                         | ∆ G a    | ∆ G s    | ∆ G a )    | ∆ G a      | ∆ G s      | ∆ G a )    |
| R1 | Co (surf) +C 3 H 6(g) +3CO (g)                                          |          |          |            |            |            |            |
|    | Co (surf - 1) + (C 3 H 5 )Co(CO) 3(g) +0.5H 2(g)                        | -3.07    | -1.11    | 1.96       | -0.63      | 1.37       | 2.0        |
| R2 | Co (surf) +C 4 H 6(g) +6CO (g) Co (surf - 2) + (C 4 H 6 )Co 2 (CO) 6(g) | -3.79    | -2.09    | 1.70       | -0.69      | 0.98       | 1.67       |
| R3 | Co (surf) +SiH 4(g) +4CO (g)                                            |          |          |            |            |            |            |
|    | Co (surf - 1) + (SiH 3 )Co(CO) 4(g) +0.5H 2(g)                          | -4.51    | -2.56    | 1.95       | -1.16      | 0.85       | 2.01       |
| R4 | Co (surf) +SiH(CH 3 ) 3(g) +4CO (g)                                     |          |          |            |            |            |            |
|    | Co (surf - 1) + (Si(CH 3 ) 3 )CO(CO) 4(g) +0.5H 2(g)                    | -4.69    | -2.74    | 1.95       | -1.16      | 0.85       | 2.01       |

FIG. S3. Free energy profiles of the overall etch reactions given in Table S3. Dotted lines correspond to the etch of surface atoms and the solid lines correspond to the etch of adatom.

<!-- image -->

## S4: PROPOSED ALE CYCLE FOR BUTYNE+CO, SILANE+CO AND TMS+CO

Butyne + CO

<!-- image -->

CO

FIG. S4. The Proposed full ALE cycle with Butyne and CO as first and second pulse reactants respectively.

a)

4

b)

2

0

-2

-4

-6

-8

Temperature limit due to CO decomposition on Co

G [ eV / Co ]

D

0

Preactants

200

= 0.2 Torr

1

-

2

-

3

-

4

-

Butyne adsorption

Purge (not shown)

Adsorption of CO

Material removal

5

-

Total ALE cycle

Pproducts

= 0.01 Torr

400

600

Temperature  [K]

800

1000

Realistic range of reactant and product

partial pressures

(C H )Co(CO)

CoT

4

6

6

dissociation + by-product

TABLE S4. Reaction free energies of the individual reactions of Co ALE cycle with butyne and CO as reactants. Unreacted Butyne CO

| Reaction   | Reaction       | ∆ G [eV/Co T ] T 1.2 Å   | ∆ G [eV/Co T ] T 1.2 Å   | ∆ G [eV/Co T ] T 1.2 Å   | ∆ G [eV/Co T ] T 1.2 Å         | ∆ G [eV/Co T ] T 1.2 Å   |
|------------|----------------|--------------------------|--------------------------|--------------------------|--------------------------------|--------------------------|
|            | T              | = 0 K =                  | T = ∆ G                  | 500 K ∆ G cum 1          | T = ∆ G                        | 800 K ∆ G cum Butyne     |
|            | ∆ G 4          | ∆ G cum .                |                          | .                        |                                | .                        |
| 1:         | Pulse 1 -1.06  | Co ALE (Butyne           | -0.46 cycle +CO)         |                          | -0.11                          |                          |
| 2:         | Purge 1 0.00   | -1.06                    | 0.00                     | -0.46                    | 0.00                           | -0.11                    |
| 3:         | Pulse 2 -5.93  | -6.99                    | -2.30                    | -2.76                    | -0.11                          | -0.22                    |
| 4:         | Purge 2 3.20 3 | -3.79                    | 2.06                     | -0.70 2                  | 1.40 No dissociation formation | 1.18 spontaneous +       |

Pressure-Temperature Process Window

FIG. S5. Panel a) shows free energy profiles of the individual reaction steps given in Figure S4 per etched Co atom. panel b) shows the pressure-temperature process window of the complete ALE cycle per etched Co atom.

<!-- image -->

## Silane/ TMS + CO

FIG. S6. The Proposed full ALE cycle with Silane/TMS and CO as first and second pulse reactants respectively. The energies are evaluated at 0 K.

<!-- image -->

<!-- image -->

Reaction

1:

Pulse 1

2:

3:

Purge 1

Pulse 2

∆

G

[eV/Co

T

]

T = 0 K T = 500 K T = 800 K

∆

G

∆

G

cum

.

∆

G

∆

G

cum

.

∆

G

∆

G

cum

-0.76

0.00

-7.95

-0.76

-8.71

0.41

0.00

-3.26

0.41

-2.85

1.12

0.00

-0.43

1.12

0.69

4:

Purge 2

3.69

-5.02

1.74

-1.11

0.52

1.21

TABLE S5. Reaction free energies of the individual reactions of Co ALE cycle with Silane and CO as reactants.

Reaction

∆

G

[eV/Co

T

]

T = 0 K

∆

G

∆

G

cum

-0.88

0.00

-8.18

1:

Pulse 1

2:

3:

Purge 1

Pulse 2

-0.88

-9.06

T = 500 K

∆

G

∆

G

cum

0.47

0.00

-3.44

0.47

-2.97

T = 800 K

∆

G

∆

G

cum

1.27

0.00

-0.60

1.27

0.67

4:

Purge 2

3.85

-5.21

1.86

-1.11

0.64

1.31

TABLE S6. Reaction free energies of the individual reactions of Co ALE cycle with TMS and CO as reactants.

.

.

.

.

FIG. S7. Panels a) and c) show the free energy profiles of the individual reaction steps when silane and TMS are used as the first pulse chemical, respectively. b) and d) show the pressure-temperature process window of the corresponding complete ALE cycle.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## S5: MD AND CI-NEB ANALYSIS OF PROPENE DISSOCIATION

FIG. S8. a) MD snapshots showing the H dissociation pathway from propene adsorbed Co(2 0 1) surface. b) Distance of the dissociated H atom from the target Co atom and the closest C atom. c) Correlation between the distances of the dissociated H from the target Co atom and the closest C atom. d) Energy change with respect to increase in the C-H distance. 'TS' refers to the transition state structure verified with CI-NEB method.

<!-- image -->

The dissociated H atom briefly binds to the target Co atom (TS and structure 2 in Figure S8a) for about 55 fs with a minimum Co T -H distance of 1.52 ˚ and diffuses towards A the neighbouring surface Co atoms (increasing Co T -H distance in Figure S8b and S8c). H atom diffusing from Co T to a surface Co is energetically favourable as can be seen from the lowest potential energy recorded for geometry 3 in Figure S8d.

FIG. S9. CI-NEB energies and geometries along the minimum energy pathway of propene dissociation. The calculation is performed by freezing all the surface atoms to avoid surface atom geometry changes contributing to the activation barrier like in the MD study in the main text. The transition state corresponds to geometry 2 in Figure 8 of the main text.

<!-- image -->