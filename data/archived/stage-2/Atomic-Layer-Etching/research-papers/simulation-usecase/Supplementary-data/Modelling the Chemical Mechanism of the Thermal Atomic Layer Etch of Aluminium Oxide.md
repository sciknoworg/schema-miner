Supporting Information for "Modelling the Chemical Mechanism of the Thermal Atomic Layer Etch of Aluminium Oxide: A Density Functional Theory Study of Reactions During HF Exposure"

Suresh Kondati Natarajan † and Simon D. Elliott ∗ † ‡ , ,

† Tyndall National Institute, University College Cork, Lee Maltings, Dyke Parade, Cork, T12 R5CP, Ireland.

‡ Currently at Schrödinger Inc., 120 West 45 th Street, 17 th Floor, New York, NY 10036-4041, USA.

E-mail: simon.elliott@schrodinger.com

## S1. Convergence Studies

A convergence test to obtain optimized K-point mesh for bulk θ -Al O 2 3 calculations is performed at an energy cutoff of 550 eV and the results are listed in Table 1. For each K-point setting, a lattice optimization is performed as given in the method section of the main paper to obtain the energy and optimized lattice parameters. It is evident that 2 × × 4 4 Monkhorstpack K-point mesh is sufficient to obtain converged lattice parameters.

Convergence studies to obtain optimized Monkhorst-pack K-point mesh, thickness of vacuum separating the slabs and plane wave energy cutoff for the slab calculation of θ -

Table 1: K-point convergence results for bulk θ -Al O 2 3 at an energy cutoff of 550 eV.

| K-points   |   a [Å] |   b [Å] |   c [Å] |   β [ ◦ ] |   E/Al 2 O 3 [eV] |
|------------|---------|---------|---------|-----------|-------------------|
| 2 × 4 × 4  | 11.935  |  2.9375 |  5.6664 |   103.999 |           37.3608 |
| 3 × 6 × 6  | 11.9352 |  2.9398 |  5.668  |   104.009 |           37.3649 |
| 4 × 8 × 8  | 11.9351 |  2.9399 |  5.668  |   104.01  |           37.3607 |

Al O ( 2 3 ¯ 2 01) are conducted and the results are given in Table 2. Here, the surface energy of Al O ( 2 3 ¯ 2 01) is chosen as the target. Several single point calculations are performed on an Al O ( 2 3 ¯ 2 01) slab with frozen atoms at the bottom face and vacuum along the 'z' direction. The atomic positions were pre-optimized with a 1 × × 1 1 K-point mesh, 400 eV energy cutoff and 16 Å of vacuum thickness. For the variable K-point calculations, the energy cutoff and the vacuum thickness are fixed at 400 eV and 16 Å, respectively. For the variation of vacuum thickness, the K-points and the energy cutoff are fixed at 1 × × 1 1 and 400 eV, respectively. For the variable energy cutoff calculations, the K-points and the vacuum thickness are fixed at 1 × × 1 1 and 16 Å, respectively. The largest variation in the surface energy is observed in the energy cutoff test. However, the difference is only about 0.05 eV/nm 2 between 400 and 450 eV. Therefore, 400 eV is chosen as the energy cutoff for the production calculations. The setting with K-point mesh = 1 × × 1 1, vacuum thickness = 14 Å and energy cutoff = 400 eV is found to be sufficient to reliably describe the surface of Al O ( 2 3 ¯ 2 01). However, we have used 16 Å of vacuum in all production calculations to accommodate the adsorption of HF molecules.

Table 2: Convergence of surface energy of Al O ( 2 3 ¯ 2 01) with respect to varying Monkhorstpack K-point mesh, thickness of vacuum separating the slabs and plane wave energy cutoff.

| K-points   |   surf [eV/nm |   Vacuum [Å] |   E surf [eV/nm |   E cutoff [eV] |   E surf [eV/nm |
|------------|---------------|--------------|-----------------|-----------------|-----------------|
| 1 × 1 × 1  |         12.56 |           14 |           12.57 |             350 |           12.6  |
| 2 × 2 × 1  |         12.55 |           16 |           12.56 |             400 |           12.56 |
| 3 × 3 × 1  |         12.55 |           18 |           12.59 |             450 |           12.51 |

## S2. Density of States and Band Structure of Bulk Alumina

From the optimized bulk θ -Al O 2 3 geometry, total density of states (DOS) and band structure are computed as shown in Fig. 1. The plot is exported using the p4v program from VASP. The band gap is found to be about 5 eV.

b)

Figure 1: Total electronic density of states and band structure of bulk θ -alumina.

<!-- image -->

The partial DOS contributed by Al and O atoms to the total DOS is shown in Fig. 2. This plot is also generated with the help of p4v program from VASP. The region between -20 eV and -15 eV is dominated by oxygen '2s' orbital states and the region between -7 eV and 0 eV is dominated by oxygen '2p' states. The valence electronic states of Al are very low since Al and O forms ionic bonds in θ -alumina and most of the valence electrons are concentrated around the O atoms.

Figure 2: Partial DOS contribution of Al and O to the total DOS of bulk θ -alumina.

<!-- image -->

## S3. Computed Properties

The binding/ adsorption energies, E bind / ads , of the adsorbate molecules on the substrate reported in this paper are computed as

$$E _ { \text{bind/ads} } = E _ { \text{int} } - ( E _ { \text{ads} } + E _ { \text{sub} } )$$

where, E int is the total energy of the optimized interacting system where the adsorbate is bound to the substrate, E ads is the total energy of the optimized adsorbate molecule in vacuum and E sub is the total energy of the optimized clean substrate slab. If the E bind / ads is negative, that is an indication of a favourable interaction and vice-versa.

Charge density difference

$$\Delta \rho = \rho _ { \text{IS} } - ( \rho _ { \text{S} } + \rho _ { \text{A} } ),$$

is computed by subtracting the combined charge densities of non-interacting systems (surface (S) without the adsorbate and adsorbate (A) without the surface) from the interacting system (IS). The geometries for non-interacting systems are created from the interacting system by just removing the atoms of either the adsorbate molecule or the surface. The charge difference plot is generated using the free tool VESTA. 1

## S4. Detailed Surface Geometry

Fig. 3 gives a detailed account on the geometry of the optimized (1x4) supercell of θ -Al O ( 2 3 ¯ 2 01) surface.

̅

Figure 3: a) Full side view of the optimized (1x4) supercell of θ -Al O ( 2 3 ¯ 2 01), b) A perspective view of the optimized supercell, c) Side and top view of the surface atoms in the optimized supercell and d) Side and top view of the first layer of optimized supercell. In panels c) and d) the alphabets A, B and C refer to the top most, second and third Al atoms from the surface. In panel d) the alphabet A' refer to the Al atom that belong to the first layer but buried in the surface below the top most Al atom A.

<!-- image -->

## S5. M X Y Notation

The M X Y notation used in the main text is explained below.

Figure 4: Illustration explaining the M X Y notation used in the main text.

<!-- image -->

## S6. Bader Charge Analysis

A charge analysis based on Bader's 'atoms in molecules' concept is performed on 1 HF Adsorbed alumina surface and the results are given in Fig. 5. This analysis is performed according to the methodology described in [http://theory.cm.utexas.edu/henkelman/code/bader/].

Figure 5: Results of the Bader charge analysis performed on 1 HF adsorbed ( ¯ 2 0 1) surface. The figure in the left shows the atoms in the supercell color coded according to their corresponding Bader charge. The table in the right lists Bader charges associated with selected atoms in the supercell.

<!-- image -->

The graphic in the figure shows the optimized geometry of dissociatively adsorbed HF molecule on alumina ( ¯ 2 0 1) surface. The Al atoms do not retain their valence electronic charge due to the ionic bonding between Al and O atoms. The surface O atoms seem to have slightly lower charge when compared to those in the bulk. The F bound Al atom (Al') has a bader charge of +2.45, which means it retains only an electronic charge of 0.55 in its valence bands. The F atom has a charge of -0.83, which means it managed to gain electrons possibly from the surface O atoms. The H atom has a charge of +0.67 and it must be sharing electrons with O' since the O'-H combined charge is about -0.85. The H bound O atom (O') has a charge of -1.52, which is considerably lower than that of the other surface O atoms despite sharing electrons with the H atom. Therefore, the F atom must have gained a significant amount of charge density from O'.

## S7. Desorption of AlF 3 and Al F 2 6

The below figure shows the relative energy change involved in the desorption of AlF 3 and Al F 2 6 molecules from the fluorinated surface of alumina. The desorption of an AlF 3 molecule requires an energy of 5.08 eV, while an Al F 2 6 molecule requires 5.24 eV. Al F 2 6 requires more energy than AlF 3 since the desorption of the former involves breaking of comparatively more bonds than that of the latter.

Figure 6: Geometries describing the desorption of AlF 3 and Al F 2 6 from an AlF x layer on alumina surface along with the corresponding desorption energies.

<!-- image -->

## References

- (1) Momma, K.; Izumi, F. VESTA 3 for Three-Dimensional Visualization of Crystal, Volumetric and Morphology Data. J. Appl. Crystallogr. 2011 , 44 , 1272-1276.
