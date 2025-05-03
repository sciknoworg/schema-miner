<!-- image -->

Contents lists available at ScienceDirect

## Computers and Chemical Engineering

journal homepage: www.elsevier.com/locate/compchemeng

## Multiscale computational fluid dynamics modeling of spatial thermal atomic layer etching

Sungil Yun a , Matthew Tom a , Gerassimos Orkoulas c , Panagiotis D. Christofides a,b, ∗

- a Department of Chemical and Biomolecular Engineering, University of California, Los Angeles, CA 90095-1592, USA
- b Department of Electrical and Computer Engineering, University of California, Los Angeles, CA 90095-1592, USA
- c Department of Chemical Engineering, Widener University, Chester, PA 19013, USA

## a r t i c l e i n f o

## a b s t r a c t

Article history:

Received 8 May 2022

Revised 24 May 2022

Accepted 26 May 2022

Available online 28 May 2022

## Keywords:

Semiconductor manufacturing

Spatial thermal atomic layer etching Multiscale modeling Computational fluid dynamics modeling Kinetic Monte Carlo modeling

Process operation

Spatial atomic layer deposition and etching processes have emerged to reduce the overall process time while maintaining the conformity of thin films by functioning continuously. This research constructs an multiscale computational fluid dynamics (CFD) model with a dynamic mesh that combines a microscopic kinetic Monte Carlo algorithm of the film etching with a CFD simulation of the gas phase for the spatial thermal atomic layer etching of Al2O3. Using this model, we evaluate the effect that design and operation variables including the gap distance, purge and precursor gas flow rates, substrate velocity, and vacuum pressure have on the substrate film etching per cycle and uniformity. Numerical results suggest that small gap distances with sufficiently high N2 flow are desired to accomplish effective precursor separation for reactor configuration and the process operation requires low substrate velocities and low vacuum pressures to achieve optimal film quality and conformance.

© 2022 Elsevier Ltd. All rights reserved.

## 1. Introduction

As a consequence of the growing dependence on semiconductors from the rise of technological advancements and innovation made on smart phones, autonomous vehicles, and gaming devices, for example, semiconductor shortages are becoming more common. Hence, manufacturing industries are unable to meet this increase in demand. This growing dependency is forcing technology giants to experience sales losses (Voas et al., 2021) due to the decreasing production rate of their products. Prior to the Covid-19 pandemic, semiconductor manufacturing facilities had already been struggling to maintain a steady supply of these devices due to time-consuming processes. The difficulty is involved in time-intensive fabrication and stricter quality specifications on their dimensions as the semiconductor devices, specifically transistors, continue to decrease in size as predicted by Moore's Law (Moore, 1998). In particular, one of the most essential components of the semiconductor fabrication process involves the modification of semiconductor surfaces by atomic layer deposition (ALD) and atomic layer etching (ALE) to produce highly conformal thin films that serve to insulate the semiconductor and have precise dimensions below 1 nm . ALE and ALD processes are able to de-

∗ Corresponding author at: Department of Chemical and Biomolecular Engineering, University of California, Los Angeles, CA 90095-1592, USA.

E-mail address:

pdc@seas.ucla.edu (P.D. Christofides).

liver more precise control of monolayer thicknesses in the atomic scale (Ritala et al., 1999); however, these aforementioned processes are time-consuming and lack controllability. Thus, it is imperative to optimize the efficiency of the semiconductor fabrication process while maintaining process control and product conformance.

Among the diverse types of semiconductors, fin field-effect transistors (FinFETs) have been recognized for facilitating the process to engrave three-dimensional (3D) patterns on circuit boards leading to an increase in computing speed and reduction of current losses (Jurczak et al., 2009). However, with the miniaturization in the size of transistors, industries have encountered challenges associated with fabricating the fin width to 5 nm or lower, resulting in mobility loss and short-channel effects for FinFETs (Razavieh et al., 2019). To overcome this performance degradation, the development of gate-all-around (GAA) transistors has recently been investigated (Lee et al., 2020) and has been found to provide greater power efficiency, electrostatic properties, and resistance to short-channel effects (Guerfi and Larrieu, 2016). The aforementioned properties are attributed to the design of the GAA transistor such that vertically stacked channels called nanowires are enclosed on all sides of the transistor gate. A diagram comparing conventional FinFET and GAA transistors is presented in Fig. 1, which demonstrates the versatility of the GAA design that permits nanowire thicknesses of 5 nm or lower. The design of the GAA transistor is structured on precise measurements to achieve optimal design properties and maintain quality conformance; thus, the

<!-- image -->

<!-- image -->

## Nomenclature

## Constants

- → g

gravitational acceleration constant, 9.80665 · Planck's constant, 6.62607015 × 10 - 34 m 2 · kg · s - 1

m s

-

2

h

kB

Boltzmann constant, 1.380649

×

10

-

23

m

2

·

kg

·

s

-

2

· K - 1

R universal gas constant, 8.314463, m Pa 3 · · K - 1 · mole - 1

## Reaction Kinetics

ν

pre-exponential factor for reaction, j

σ

sticking coefficient

Asite

surface area of an active site

EA

activation energy

k

reaction rate constant

k i

reaction rate constant for reaction, i

k d abs ,

reaction rate constant for adsorption reactions de-

rived from Collision Theory

k total

sum of reaction rate constants

m

mass of the adsorption species

N

number of reaction pathways

P

partial pressure of the adsorption species

Q

quantum partition function for the reactant species quantum partition function for the transition state

Q ‡

species

Z

coordination number

/Delta1 t

time evolution

γ , γ 1 2

coefficient for reaction selection and time evolution where γ , γ 1 2 ∈ ( 0 1] ,

## Transport Phenomena

τ

stress tensor

- →

F

external body force

ρ

density of the precursor species

/vector v

velocity of the mixture

E

internal energy

h j

sensible enthalpy of the species, j

J j

diffusion flux of the species, j

p

static pressure of the species

S h

heat transfer source

Sm

mass transfer source term

T

operating temperature of the reactor

t

process time of the reaction

## Meshing Parameters

α

diffusion parameter

γ

diffusion coefficient

∇ /vector u

mesh displacement velocity

d

normalized boundary distance

## Abbreviations

ALD

atomic layer deposition

ALE

atomic layer etching

CFD

computational fluid dynamics

EPC

etching per cycle ( ˚ /cycle) A

SALD

spatial thermal atomic layer deposition

SALE

spatial thermal atomic layer etching

kMC

kinetic Monte Carlo

Al CH3 3 ( )

Trimethylaluminum, TMA

## Reaction Species

Al 2 O3

aluminum oxide

AlF3

aluminum fluoride

H2O

water

HF

hydrogen fluoride

N2

nitrogen gas

AlF CH3 ( ) 2

dimethylaluminum fluoride, DMAF

fabrication of these devices raises challenges for commercialization and integration in industry. However, ALD and ALE processes are widely recognized for their ability to control the thickness through selective reactions, which raises the prospects of commercializing GAA transistors in the semiconductor industry.

Recently, there has been a transition in research on amorphous hydrogenated silicon and polycrystalline silicon as active layers in thin film transistors to metal oxide thin films. The metal oxide films have better uniformity, require lower process temperatures, and are inexpensive to fabricate (Ding and Wu, 2020; Ye et al., 2017), making these materials superior to silicon-based wafers. The desirability of metal oxide thin films is attributed to the lack of delocalization of electron movement between metal atoms, which increases the reactive tendency to surface layer modification (Sang and Chang, 2020). Among the many oxide films discussed by Fortunato et al. (2012), Faraz et al. (2015), Sheng et al., 2018, aluminum oxide (Al 2 O3) exemplifies the aforementioned properties of oxide films due to the reaction system described in Section 2.1. Aluminum, which possesses a low electronegativity and hence lesser desirability to attract electrons, can form stronger ionic bonds with a highly electronegative atom such as fluorine (Lee et al., 2016) during the ALD and ALE adsorption half-cycle reactions. As a result, adopting these opposing atoms requires less energy input to produce substantial reaction progress, facilitating the ALD and ALE processes to semiconductor fabrication from an economics perspective. Therefore, this research aims to study and characterize Al 2 O 3 as a thin film substrate for nanowires.

Thermal atomic layer deposition (ALD) is a premature process that is gradually being integrated into the semiconductor production industry and is known to be effective at depositing layers of material on the surfaces of semiconductor substrates. Thermal ALD uses gaseous reactants called precursors that are introduced in sequential pulses. The precursors make modifications to the surface of the substrate and introduce a depositing film to generate the thin film layer (Kanarik et al., 2015). Meanwhile, thermal atomic layer etching (ALE), a bifurcation of ALD, is a process that etches the substrate material by integrating gaseous reactant pulses. The reactant pulses convert the surface of the substrate into an active reaction layer and etch the modified surface layer (Kanarik et al., 2015). For the thermal ALD and ALE processes, the precursor pulses are separated by purging steps with a purge gas to flush the residual products from the reaction chamber. The applicability of ALD and ALE to semiconductor fabrication is based on the notion that these processes exhibit self-limiting behavior. This characteristic behavior prevents precursor adsorption beyond the substrate surface where the surface layer exemplifies a transportlimited barrier. In other words, the processes are restricted to a single atomic layer (monolayer) of the substrate material that can be deposited or etched for each cycle (Kanarik et al., 2018); thus providing substantial controllability over the thickness of the substrate in the Angstrom scale. ˚

Despite the capabilities of ALD and ALE in precise substrate thickness control, conventional ALD and ALE processes are timeconsuming and counterproductive, making these processes undesirable for some applications that require high productivity. Conventional ALD and ALE require long purging steps to ensure selflimiting behavior is achieved. To overcome this obstacle, rapid atomic layer (Zywotko et al., 2018) and spatial atomic layer processes for ALD (Poodt et al., 2012; Faraz et al., 2015) have recently emerged as alternative methods for achieving high deposition or etching rate, compared to conventional ALD and ALE, in a reduced

Fig. 1. Schematic diagrams of a fin field-effect transistor (FinFET) and a gate all-around (GAA) transistor in (a) and (b), respectively. FinFETs are limited in thickness size due to the design of the transistor while the nanowires in GAA transistors are capable of narrowing to sub-5 nm thicknesses. The exterior surface of the fin and nanowires represents the metal oxide insulator.

<!-- image -->

<!-- image -->

Fig. 2. Schematic diagrams of a conventional ALD/ALE reactor (a) and a spatial ALD/ALE reactor (b). Conventional ALD/ALE processes feed precursors in sequential steps while the substrate remains stationary in contrast to spatial ALD/ALE processes, which feed precursors continuously in separate zones while the substrate sheet moves at a constant velocity through each region.

<!-- image -->

cycle time. However, for rapid atomic layer etching, researchers observed a degradation in the film roughness (Zywotko et al., 2018); thus spatial atomic layer processes are considered in this work as they are more reliable in maintaining thin film conformance (Levy et al., 2009). In spatial atomic layer deposition processes, the precursors are continuously dosed in physically separated reaction zones between the purging regions (Mu ` noz-Rojas et al., 2019) in order to permit precursor reactions in sequential steps. For the purposes of this paper, spatial atomic layer deposition (SALD) and spatial atomic layer etching (SALE) are referred to as spatial thermal ALD and spatial thermal ALE, respectively. The substrate is transferred through each region at a constant velocity and maintains a presence in the precursor regions that optimize the amount of material that is deposited onto the surface of the substrate. A schematic interpretation of the differences between conventional and spatial ALD/ALE processes are presented in Fig. 2. Fig. 2(a) resembles a conventional type ALD/ALE reactor where the substrate is stationary and consists of a single inlet and outlet. In a typical reactor for ALD/ALE, precursors are introduced separately into the reactor chamber, which is purged after each precursor injection. Fig. 2(b) shows the patented sheet-to-sheet (S2S) SALD/SALE reactor where the substrate moves between adjacent zones that are injected with inert gases or precursor species. There have been developments in SALD and SALE reactor design. The original design of the spatial ALD was developed by Suntola and Antson (1977), which was classified as a roll-to-roll type. Afterwards, rotating (Sharma et al., 2015; Aghaee et al., 2015; Sun et al., 2017) and sheet-to-sheet models (Freeman et al., 2010) have been developed.

Although ALD and ALE processes are practical for the fabrication of thin-film wafers, these processes have not been fully investigated and characterized for integration into industry. To conduct experiments in a laboratory setting is costly, time-consuming, and difficult to study under controlled environments due to the spontaneous nature of the reactions, which occur semi-instantaneously. Thus, a computational simulation approach can be conducted to reflect laboratory-setting experiments to collect a diverse data set that can improve the characterization of these ALD and ALE processes in a cost-effective and timely manner. For instance, Pan et al., 2014 and Shaeri et al., 2015 have accomplished computational fluid dynamics (CFD) modeling of ALD processes. To improve upon the CFD modeling, adopting a combined microscopic simulation using density functional theory (DFT) and kinetic theory with a macroscopic computational fluid dynamics (CFD) simulation, a 'Multiscale' model of a laboratory-setting experiment can be conducted. Previous research has already been conducted on multiscale CFD simulation for chemical vapor deposition (CVD) and ALD processes. For example, Crose et al. (2018) and Zhang et al. (2020) have performed a 3D multiscale CFD simulation for plasma-enhanced chemical vapor deposition (PECVD) and plasma-enhanced atomic layer deposition (PEALD), respectively, but their research is limited in the integration of the microscopic surface domain and the macroscopic gas-phase domain. Prior multiscale simulation was conducted in a two-step process such that CFD simulation of the macroscopic gas phase was run to the final flow time to extract the steady-state process parameters, which were later imported into the microscopic model to calculate the deposition rates. This method unreliably connects the microscopic and macroscopic domains but was previously adopted due to the complexity of the numerical simulation for a complete multiscale simulation, resulting in increased computation time. Also, prior research from Yun et al. (2022b) on the thermal ALE of aluminum oxide thin films adopted a method to include constant species consumption and generation terms in the CFD model to produce a stronger connection between the macroscopic and microscopic domains. However, this prior research was limited in computational efficiency due to the number of nodes specified in the surface substrate mesh, which prevented the development of a fully autonomous multiscale CFD model that updates the source generation and consumption terms through each multiscale loop. Thus, this work makes enhancements to the previously developed mul-

tiscale CFD model by simplifying the number of nodal regions on the surface of the substrate to allow this connection between the microscopic and macroscopic domains to exist.

Several control and quality parameters are used to determine the optimality of the reactor configuration and process operation. Several studies (Pan et al., 2016; Cong et al., 2020; Li et al., 2021) have been conducted on the gap distance between the top surface of the substrate to the bottom surface of the injection dividers, the purge gas flow rate, the precursor flow rates, the substrate velocity, and the vacuum pump pressure. The role of the gap distance serves to generate a finite boundary layer to prevent the intermixing of the precursor species, while the remaining parameters are crucial to the kinetics of the half-cycle reactions and to the selflimiting behavior of the half-cycle reactions. The aforementioned properties will be used to determine their impact on the quality of the substrate, which is determined by the amount of etching per cycle (EPC) and the surface uniformity of the substrate after the etching process. Thus, this research aims to advance from a previously developed microscopic model for the ALE of aluminum oxide (Al 2 O 3 ) thin films (Yun et al., 2022a) and to develop a multiscale CFD model of a SALE reactor using an multiscale computing method that improves the algorithms from Crose et al. (2018), Zhang et al. (2020), Yun et al. (2022b) and optimize the process operation by studying the effects of the aforementioned parameters on the quality of the substrate film.

## 2. Multiscale CFD modeling of SALE

Prior research on computational fluid dynamics (CFD) modeling of spatial atomic layer deposition (SALD) has been conducted to discuss the features of SALD and to optimize the process (Cong et al., 2020; De la Huerta et al., 2018; Deng et al., 2016; Li et al., 2021; Pan, 2021; Pan et al., 2016). The aforementioned projects have investigated the design of SALD reactors by examining the effects of the substrate velocity (De la Huerta et al., 2018; Pan, 2021), the gap distance (De la Huerta et al., 2018; Pan et al., 2016), the pitch distance between adjacent injectors (Cong et al., 2020), the precursor flow rate (Deng et al., 2016; Pan et al., 2016; Cong et al., 2020), and the purge gas flow rate (Deng et al., 2016). These investigations provide invaluable information for SALD; however, they do not discuss the surface kinetics from the microscopic perspective. In addition, the relationship of the dynamic effects of the moving substrate on the film uniformity has not been investigated as conformity is an essential parameter to discuss the quality of the finished product. Thus, a complete survey of a spatial reactor configuration is required to include all technical information while accounting for the multiscale point of view to provide theoretical guidance toward further operation and control of a SALD/SALE reactor and process. Therefore, this research aims to build a multiscale CFD model by integrating a microscopic model for the surface kinetics and a macroscopic model for the transport phenomena effects to offer a comprehensive understanding and to investigate key parameters to optimize the reactor configuration and operation.

The combination of the microscopic surface domain and the macroscopic gas-phase domain generates the so-called multiscale computational fluid dynamics (CFD) model. For the microscopic surface domain, aluminum oxide thin films are modeled on the basis of a kinetic Monte Carlo (kMC) algorithm that is initiated using a Python script code. For the macroscopic gas phase domain, Ansys Fluent 2021R2 is used to simulate the two-dimensional (2D) CFD of the gaseous species. The schematic concept of the multiscale CFD model is illustrated in Fig. 3 where input parameters including the substrate velocity, precursor (HF and TMA) flow rates, and vacuum pressure are specified to the macroscopic CFD simulation to calculate the etching per cycle. In the multiscale CFD model, Fluent

Fig. 3. A process diagram of the multiscale computational fluid dynamics (CFD) workflow. The macroscopic model using Ansys Fluent runs with a time step size of 0.0005 s and transfers precursor partial pressure and temperature data on 18 nodes of the substrate to the microscopic model. The microscopic model simulates the surface kinetics on the substrate using the kMC algorithm. The kMC code calculates the source terms (consumption and generation of species), which enables the macroscopic model to consume or generate the corresponding amount of species on a surface area-average on 18 nodal regions of the substrate. Also, the kMC script calculates the time evolution, /Delta1 t , which allows the macroscopic model to compute the exact number of time steps to run the CFD simulation. Lastly, the macroscopic and microscopic simulations are connected by a Linux shell script, resulting in an multiscale CFD simulation, which is halted until the substrate reaches the end of the reactor.

<!-- image -->

first simulates the gas-phase domain at every time step to generate the process data (surface pressure and temperature) on the substrate surface. Then, the process data is transferred to the microscopic model, which simulates the surface reactions with a lattice model defined as a 300 × 300 grid and updates the surface boundary conditions in Fluent based from the result of the kMC simulation. This cyclical operation is executed in a Linux shell script such that the macroscopic and microscopic simulations are carried out consecutively using 36 compute cores with 192 GB memory through a computer cluster network with each computation of the multiscale CFD simulation taking 6 h on average.

## 2.1. Microscopic surface domain

In the spatial atomic layer etching (SALE) of aluminum oxide thin films, two half-cycle reactions occur at different locations where the precursor species, hydrogen fluoride (HF) and trimethylaluminum [Al(CH3 ) 3 , TMA], are injected continuously at constant flow rates. First, the top surface of the substrate is fluorinated when the substrate is transported through the hydrogen fluoride reaction zone. The HF half-cycle produces a modified surface layer composed of aluminum fluoride (AlF3 ). It is assumed that the adsorption occurs in a self-limiting behavior such that the HF precursor cannot permeate beyond the surface of the substrate. Next, an adjacent vacuum port exhausts the remaining HF and the byproduct, H2O, via a vacuum pump. An inert zone using a barrier gas, N2, is also integrated into the reactor configuration to remove the residual HF on the surface of the substrate. Following the purging step, a volatile species, dimethylaluminum fluoride [DMAF, AlF(CH3 ) 2 ], is produced following a ligand-exchange reaction between the second precursor, TMA, and the AlF3 surface layer. In the next vacuum line, the residual TMA and DMAF are withdrawn from the reaction chamber to prevent further reactions of TMA. Finally, an adjacent inert zone containing N2 gas pushes the trace TMA to the vacuum port to maintain self-limiting behavior. Unlike conventional thermal atomic layer etching (ALE), SALE achieves a cyclical operation of thermal ALE as the substrate moves under an injec-

Table 1

Activation energies for rate-determining intermediate reactions for the thermal ALE of Al3O2 using HF and TMA precursors, which were calculated from Density Functional Theory via Quantum Espresso by Yun et al. (2022a).

| Reaction pathway                                                    | Activation energy (eV)   |
|---------------------------------------------------------------------|--------------------------|
| -O-O-AlF x - + HF ( g ) → -O-OH-AlF x + 1 -                         | NA †                     |
| -O-OH-AlF x + 1 - → -O-O-AlF x - + HF ( g )                         | 2.02                     |
| -O-OH-AlF x - → -OH-O-AlF x -                                       | 0.98                     |
| -OH-O-AlF y - → -O-OH-AlF y -                                       | 0.71                     |
| -OH-OH-AlF y - → -O-H 2 O-AlF y -                                   | 1.28                     |
| -O-H 2 O-AlF y - → -OH-OH-AlF y -                                   | 0.76                     |
| -H 2 O-AlF y - → -AlF y - + H 2 O ( g )                             | 0.88                     |
| -AlF 2 - + Al(CH 3 ) 3 ( g ) → -AF-FAl(CH 3 ) 3 -                   | NA †                     |
| -AlF-FAl(CH 3 ) 3 - → -AlF 2 - + Al(CH 3 ) 3 ( g )                  | 42.27                    |
| -AlF-FAl(CH 3 ) 3 - → -AlF(CH 3 ) + AlF(CH 3 ) 2 ( g )              | 1.45                     |
| -AlF(CH 3 )- + Al(CH 3 ) 3 ( g ) → -Al(CH 3 ) 2 - + AlF(CH 3 ) 2    | NA †                     |
| -AlF 3 - + Al(CH 3 ) 3 ( g ) → -AlF 2 -FAl(CH 3 ) 3                 | NA †                     |
| -AlF 2 -FAl(CH 3 ) 3 - → -AlF 3 - + Al(CH 3 ) 3 ( g )               | 21.29                    |
| -AlF 2 -FAl(CH 3 ) 3 - → -AlF 2 (CH 3 ) 2 - + AlF 2 (CH 3 ) 2 ( g ) | 0.82                     |
| -AlF 2 (CH 3 ) 2 - → AlF 2 (CH 3 ) 2 ( g )                          | 1.12                     |

† The rate constant is calculated by Collision Theory. ‡ x can be 0 through 2 and y can be 1 through 3.

Fig. 4. The schematic reaction mechanism of the thermal atomic layer etching cyclical process for Al2O3 where Step A represents the HF fluorination half-cycle and Step B represents the TMA ligand-exchange half-cycle.

<!-- image -->

tion assembly. The schematic diagram of the thermal ALE process is summarized in Fig. 4 while the overall ALE reaction is described by

$$\text{Al} _ { 2 } O _ { 3 } \ ( s ) + 6 \text{HF } ( g ) + 4 \text{Al} ( \text{CH} _ { 3 } ) _ { 3 } \ ( g ) \to 6 \text{Al} \text{F} ( \text{CH} _ { 3 } ) _ { 2 } \ ( g ) + 3 \text{H} _ { 2 } O \ ( g ) \quad \text{depen} \ \text{(Q^{\frac{1}{2})} \ a l }$$

The overall reaction is divided into two half-reactions or halfcycles, which are referred to as the HF (Fluorination) and the TMA ligand-exchange half-cycles.

$$\text{Al} _ { 2 } O _ { 3 } \ ( s ) + 6 H F \ ( g ) \to 2 \text{Al} F _ { 3 } \ ( s ) + 3 H _ { 2 } O \ ( g )$$

$$\text{AlF} _ { 3 } \ ( s ) + 2 \text{Al} ( \text{CH} _ { 3 } ) _ { 3 } \ ( g ) \to 3 \text{AlF} ( \text{CH} _ { 3 } ) _ { 2 } \ ( g ) \\ \cdots \cdots \cdots$$

The kinetic Monte Carlo (kMC) method is a stochastic computer algorithm that calculates numerical results of surface reactions through random sampling of the surface active sites to mimic the naturality of the real world. The practical usage of the kMC method serves to bridge the microscopic and macroscopic regimes. Kinetic Monte Carlo (kMC) simulations for atomic layer processes have been widely used (Lou and Christofides, 2003; Fu et al., 2008; Shirazi and Elliott, 2014; Ding et al., 2019, 2020; Yun et al., 2022a) for surface reaction kinetics. In this research, the developed kMCbased microscopic model by Yun et al. (2022a), validated with the experimental work from Lee et al. (2016), is adopted to characterize the surface reactions on Al 2 O 3 thin films. Table 1 shows the kinetic mechanism and the activation energies for ALE of Al2 O 3 and a detailed discussion of the kinetic mechanism is further examined in Yun et al. (2022a). In this research, the coverage and etching fractions are used to express the progression of the first and second half-cycle reactions, respectively, of the ALE process are calcu- lated by the kMC simulation, which assumes that the half-cycle reactions occur in self-limiting behavior such that the surface of the substrate, which is modeled as a 3D lattice. As an output of the kMC simulation, the etching per cycle (EPC) is computed by multiplying the etching fraction by the EPC of 0.46 A/cycle, which has ˚ been reported by Lee et al. (2016) whose experimental conditions were similar to the boundary conditions that would be defined in the macroscopic CFD model.

Kinetic parameters are an integral part of the input of the kMC simulation. A common approach to compute the reaction rate constant is through transition-state theory (TST), which is defined as follows:

$$\underset { \text{all-cycle} } { r } \text{ etching} \quad k = \nu \exp \left ( \frac { - E _ { A } } { R T } \right )$$

The reaction rate constant, k , is dependent on the pre-exponential factor, ν , the activation energy, EA , the universal gas constant, R , and the temperature, T , of the reaction. The activation energies are calculated by the nudged elastic band (NEB) method, which was previously performed (Yun et al., 2022a). The pre-exponential term depends on the quantum partition functions for the transition state ( Q ‡ ) and reactant ( Q ) species and is calculated from the following expression:

$$\nu = \frac { k _ { B } T } { h } \frac { Q ^ { \dagger } } { Q }$$

where kB is the Boltzmann constant, T is the temperature of the reaction, and h is the Planck constant. For simplicity, the ratio of the transition state and reactant partition functions can be approximated to unity (Jansen, 2012). Desorption, surface reaction, and diffusion rates are computed by Eqs. (1) and (2). However, for the adsorption process, collision theory (CT) is used, which is based on Maxwell-Boltzmann statistics.

$$\text{egimes}. \quad & \text{sides} \quad k _ { d, a d s } = \frac { 2 P A _ { s i t e } \sigma } { Z \sqrt { 2 \pi m k _ { B } T } } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sines} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sines } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sizes} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sizes } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{siles} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{siles } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sids} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sids } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sities} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sities } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{side} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{side } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sidy} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sidy } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sIDES} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sIDES } \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{samples} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides} \quad \text{sides}$$

where P is the partial pressure of the adsorption species, Asite is the area of a single surface active site, σ is the sticking coefficient, Z is the coordination number, m is the mass of the adsorption species, and kB is the Boltzmann constant. Based on the aforementioned reaction theories, the total rate constant, as a fundamental element of the kMC algorithm, is calculated as follows:

$$\begin{smallmatrix} \Phi _ { \text{etching} } \\ \text{nd sec-} \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i }
 \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i} \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { \nu } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { j } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } {i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } {  \nu } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m} \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { \nu } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { \nu } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\  \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } \\ \mathbb { m } { i } \\ \mathbb { m } { i } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \nu \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathpp { i } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } { i } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m | i } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb { m } \\ \mathbb {$$

Table 2 Minimum to maximum mesh quality parameter ranges for various sheet-to-sheet reactor configurations with the overall quality determined by criteria from ANSYS (2021).

| No.   |   Gap ( mm ) | Skewness   | Orthogonal quality   | Aspect ratio   | Overall quality ∗   |
|-------|--------------|------------|----------------------|----------------|---------------------|
| † R1  |        10    | 0 ∼ 0.528  | 0.682 ∼ 0.964        | 1 ∼ 2.297      | Very good           |
| † R2  |         1    | 0 ∼ 0.674  | 0.565 ∼ 1.000        | 1 ∼ 2.899      | Very good           |
| † R3  |         0.5  | 0 ∼ 0.660  | 0.588 ∼ 1.000        | 1 ∼ 2.747      | Very good           |
| † R4  |         0.25 | 0 ∼ 0.682  | 0.553 ∼ 1.000        | 1 ∼ 2.991      | Very good           |
| ‡ R5  |         0.25 | 0 ∼ 0.525  | 0.671 ∼ 1.000        | 1 ∼ 2.316      | Very good           |

- ∗ Determined by ANSYS (2021). † No substrate to investigate the effects of precursor intermixing. ‡ Optimized reactor design with a substrate.

Fig. 5. A 2D side view of the dynamic mesh for the spatial reactor design with 0.25 mm gap distance.

<!-- image -->

Fig. 6. Line plots illustrating the effects of the gap distance on precursor separation, of which operating condition is (a) Case 1, (b) Case 2, (c) Case 3, and (d) Case 4 as described in Table 3. The shaded area indicates the precursor intermixing zone.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

where k i is the reaction rate constant of reaction i and N is the number of reaction pathways. The kMC computation is performed as follows, which is repeated until the termination condition is achieved.

- 1. The sum of the rate constant, k total , is computed from the list of all possible reaction paths across the lattice model.
- 2. An event is chosen to fulfill the following equation.

$$\int _ { i = 1 } ^ { \int _ { i } } & k _ { i } \leq \gamma _ { 1 } k _ { t \alpha t a l } \leq \sum _ { i = 1 } ^ { m } k _ { i } \\ \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \int _ { i = 1 } ^ { \int _ { i } } & \end{cases}$$

where m is the reaction m and γ 1 ∈ ( 0 1] is , the first random number for the event selection.

<!-- image -->

(a) Nz flow rate of 100 sccm

<!-- image -->

<!-- image -->

(b) Nz flow rate of 500 sccm

<!-- image -->

- (c) Nz flow rate of 1,000 sccm

(d Nz flow rate of 2,000 sccm

Fig. 7. Line plots illustrating the effects of the N2 flow rate on precursor separation, of which operating condition is (a) Case 1, (b) Case 5, (c) Case 6, and (d) Case 7 as described in Table 3. The shaded area indicates the precursor intermixing zone.

Table 3 Various operating conditions for multiple sheet-to-sheet reactor configurations to examine their effects on precursor separation and thin film quality.

| Case   | Temperature   | Pressure (Pa)   | Pressure (Pa)   | Gap distance   | Flow rate ( sccm )   | Flow rate ( sccm )   | Flow rate ( sccm )   |
|--------|---------------|-----------------|-----------------|----------------|----------------------|----------------------|----------------------|
| (No.)  | (K)           | Operating       | Vacuum          | ( mm )         | N 2                  | HF/N 2               | TMA/N 2              |
| 1      | 573           | 300             | - 100           | 10.00          | 100                  | 100/50               | 60/100               |
| 2      | 573           | 300             | - 100           | 1.00           | 100                  | 100/50               | 60/100               |
| 3      | 573           | 300             | - 100           | 0.50           | 100                  | 100/50               | 60/100               |
| 4      | 573           | 300             | - 100           | 0.25           | 100                  | 100/50               | 60/100               |
| 5      | 573           | 300             | - 100           | 10.00          | 500                  | 100/50               | 60/100               |
| 6      | 573           | 300             | - 100           | 10.00          | 1,000                | 100/50               | 60/100               |
| 7      | 573           | 300             | - 100           | 10.00          | 2,000                | 100/50               | 60/100               |
| 8      | 573           | 300             | - 100           | 10.00          | 100                  | 200/50               | 120/100              |
| 9      | 573           | 300             | - 100           | 10.00          | 100                  | 400/50               | 240/100              |
| 10     | 573           | 300             | - 100           | 10.00          | 100                  | 800/50               | 480/100              |

- 3. The secondary random number, γ 2 ∈ ( 0 1], is selected to evolve , the system clock with a time interval defined as follows:

$$\Delta t & = \frac { - \ln \gamma _ { 2 } } { k _ { t \alpha t a l } } & ( 6 ) & \quad \text{lim} \, \text{qu} \\ & & \text{Ansys}$$

## 2.2. Macroscopic CFD domain

The effects of transport phenomena within the spatial reactor are investigated through computational fluid dynamics (CFD) software to compute spatial and time-dependent variables within the reactor. Spatial atomic layer etching (SALE) reactors with different gap distances are developed to investigate the intermixing of the precursors and the effect of the velocity of the substrate on thin film quality based on a two-dimensional (2D) multiscale CFD simulation with a dynamic mesh. First, WorkBench 2021R2, one of the Ansys packages, is used to construct the mesh with triangular elements for five reactors (denoted as R1 through R5) whose mesh quality is quantified in Table 2. The mesh quality plays a significant role in the convergence, numerical solution accuracy, and stability of the CFD computation. As shown in Table 2, the mesh quality of all reactor designs built in this research is considered acceptable by the criteria defined by ANSYS (2021). A more detailed discussion of the mesh quality parameters is given in Yun et al. (2022b).

<!-- image -->

HF 100 sccm TMA 60 sccm and

<!-- image -->

<!-- image -->

HF 200 sccm and TMA 120 sccm

<!-- image -->

HF 400 sccm and TMA 240 sccm

HF 800 sccm and TMA 480 sccm

Fig. 8. Line plots illustrating the effects of the precursor flow rate on precursor separation, of which operating condition is (a) Case 1, (b) Case 8, (c) Case 9, and (d) Case 10 as described in Table 3. The shaded area indicates the precursor intermixing zone.

In order to simulate the moving substrate, a dynamic mesh is employed, in which two dynamic mesh update methods are used: diffusion-based smoothing and remeshing. The diffusionbased smoothing method adjusts the mesh through each time step as the substrate moves, which is defined by the following equation:

$$\nabla \cdot ( \gamma \nabla \vec { l } ) = 0 & ( 7 ) & \quad \text{long su} \\ \text{when} \, \cdot \, \text{is the difference coefficient and } \nabla \vec { r } \, \text{is the much distance} \quad \text{cases}$$

where γ is the diffusion coefficient and ∇ /vector u is the mesh displacement velocity. The diffusion coefficient is calculated as a function of the boundary distance.

$$\gamma = \frac { 1 } { d ^ { \alpha } } & & ( 8 ) & & \text{study t} \\ & & & \text{pressure} \\ & & & \text{In } t$$

10 mm width are located at the top of the reactor. Each port has a 20 mm height and 20 mm pitch (that is, the distance between the centers of two adjacent ports). The injection assembly can be modularized and extended by adding extra injection assemblies as needed. For R5, the substrate is placed in the leftmost purge (N 2 ) zone as illustrated in Fig. 5. For simplicity, in this work, a 5 mm long substrate is employed; however, the length of the substrate can be enlarged. The multiscale CFD simulation is performed using reactor configurations R1 through R4 to investigate the effects of the gap distance, the N 2 flow rate, and the precursor (HF and TMA) flow rates on precursor separation. Then, the reactor, R5, is used to study the effects of a moving substrate and of the outflow vacuum pressure on the film quality.

where d is the normalized boundary distance and α is the diffusion parameter. The boundary-distance-based diffusion method allows the absorption of the mesh motion and preserves the mesh quality around the boundary of the motion. For α , a range of 0 through 2 is practical and 1.5 is chosen in this work. As another mesh update method, the remeshing method is adopted, which is modeled on local cells and allows the mesh to be updated locally with an acceptable skewness criterion so that the mesh quality is maintained through each time step. In the local cell remeshing mode, the maximum cell skewness is set to 0.7, which is recommended for 2D simulations by ANSYS (2021).

Each reactor is designed with a length of 160 mm , in which 9 injection or vacuum ports (denoted as an injection assembly) of

In the CFD simulation, the mass, momentum, and energy conservation equations are solved on the basis of the coupled pressure-based solver in Ansys Fluent, which are described by:

$$\inf _ { \text{which is} } \quad \frac { \partial \rho } { \partial t } + \nabla \cdot ( \rho \bar { \nu } ) = S _ { m }$$

$$\stackrel { \dots } { \text{quality} } \\ \text{being} \\ \text{recom-} }$$

$$\text{$rhich $9$} _ { \text{bly of} } \quad \frac { \partial } { \partial t } ( \rho E ) + \nabla ( \vec { \nu } ( \rho E + p ) ) = - \nabla ( \Sigma h _ { j } J _ { j } ) + S _ { h } \quad \quad ( 1 1 )$$

Fig. 9. Pressure contours of HF (a) and H2O (b) in the HF injection region for a substrate velocity of 80 mm s / and vacuum pressure of - 100 Pa after 0.5 s of process time.

<!-- image -->

<!-- image -->

where ρ is the density of the mixture, - → v is the velocity of the mixture, Sm is the mass transfer source term, p is the static pressure, τ is a symmetric rank two stress tensor, ρ - → g is the gravitational body force, - → F is the external body force, E is the internal energy, h j is the sensible enthalpy of the species j , J j is the diffusion flux of species j , and S h is the heat transfer source term. To solve these partial differential equations, the finite volume method is employed in the discretized time domain. To specify the consumption of HF and TMA and the generation of H2O and DMAF from the surface kinetics, the source term ( Sm ) for each species is defined in a user-defined function (UDF) and the source terms are updated every time step, which are computed from the microscopic kMC simulation. The operating conditions, temperature and pressure, and boundary conditions, precursor and purge flow rates, are also defined in the UDF.

## 3. Simulation results and discussion

The combination of the microscopic kMC model and the macroscopic CFD model is made possible by defining convergence criteria and iteration conditions during the numerical simulation for the macroscopic gas-phase domain. Default convergence thresholds and a time step size of 0.0005 s are defined to prevent the risk of divergent solutions in order to maintain the connection between the microscopic kMC model and the macroscopic CFD model. The number of time steps is determined by the microscopic kMC model, which updates the flow time as well as the mass source generation and consumption terms for each species in the half-cycle reactions. At time t = 0, the SALE reactor will be in steady-state conditions such that all gaseous species will have reached equilibrium conditions, which is determined by initially simulating the reactor with the steady-state solver. Once the steady-state conditions are obtained, the transient solver is used to propagate the movement of the substrate through the reaction chamber.

The effects of parameters (gap distance, purge gas flow, precursor flow, substrate velocity, and vacuum pressure) are studied for the optimization and operation of the sheet-to-sheet (S2S) spatial reactor design. Table 3 summarizes the list of case studies that are carried out by adjusting the aforementioned parameters. First of all, the steady-state simulation mode in Fluent is used to run the computational fluid dynamics (CFD) simulation to analyze the effects of the gap distance, the N 2 flow rate, precursor (HF and TMA) flow rates by using reactor configurations R1 through R4 without a substrate in Table 2. The effects of those parameters on precursor separation are discussed in the following sections. Then, on the basis of the results of the aforementioned simulation, the optimal reactor parameters are selected and used to investigate the effects of the substrate velocity and vacuum pressure on the film quality, which are simulated using the transient simulation mode in Fluent. In this paper, the term, 'cycle,' is used even if the spatial atomic layer etching reactor is not operating in a cyclical operation. Thus, 'a cycle' by definition occurs when a substrate passes through the 9 ports of the injection assembly. There are several assumptions that underlie the simulations: (1) there are manifolds in the upstream facility so the precursors and N2 are well-mixed and injected through the injection ports, (2) the temperature of the substrate surface is maintained by a PID (proportional-integralderivative) controller at 573 K, (3) the velocity of the substrate is constant in each simulation, (4) a vacuum pump, which is not constructed in the reactor configuration, is implemented to exhaust gases through the vacuum ports, and (5) a physical conveyor belt that moves the substrate is ignored, since the research focuses on the fluid regime between a substrate surface and the bottom of an injection assembly.

Fig. 10. Pressure contours of TMA (a) and DMAF (b) in the TMA injection region for a substrate velocity of 80 mm s / and vacuum pressure of - 100 Pa after 1.5 s of process time.

<!-- image -->

<!-- image -->

## 3.1. Effect of the gap distance

The separation of precursors is highly dependent on the gap distance between the top of the substrate surface and the bottom of the divider walls enclosing the injection assembly, as exemplified in Fig. 2(b). Thus, the separation of the precursors is primarily determined by a gap distance, which serves to generate effective N2 zones so that precursor species are not able to intermix. Unsuccessful precursor separation would result in undesirable etching and spontaneous etching (Pan et al., 2016); therefore, an effective gas barrier design is needed. In this research, reactor configurations R1 through R4 with 10.00 mm , 1.00 mm , 0.50 mm , and 0.25 mm gap distances (shown in Table 5) are used to investigate the effect of the gap distance on precursor separation. Simulations are carried out under the operating conditions defined as Case 1 through Case 4 in Table 3. As shown in Fig. 6, precursor separation improves with decreasing gap distance, which is visualized by decreasing the shaded area under the mole fraction curves of HF and TMA and is consistent with the findings of the results of Pan et al. (2016), De la Huerta et al., 2018. An insignificant difference is observed between reactors with a gap distance of less than 1 mm . Fig. 6(a) and (b) reveal that a smaller gap distance also marginally increases the mole fraction of the precursors in the half-reaction zones, resulting in a higher adsorption rate and an effective etching reaction.

The pressure difference is a driving force for gases to flow from a high pressure field to a low pressure field. For the reactor configuration, R1, of 10.00 mm gap distance, no pressure gradient is observed around the gap. Therefore, due to the lack of a strong driving force, most of the precursors are exhausted through the vacuum outlet when the precursors pass through the gap, but some of the precursors are able to cross over to the N2 enriched zone and intermix with one another. However, in the reactor, R4, with a gap distance of 0.25 mm , reasonably large pressure gradients of 75 ∼ 113 Pa are observed between the gap and a vacuum outlet, resulting in the strong suction of the precursor through the vacuum outlet. Consequently, no trace of the precursor is allowed to pass through a vacuum outlet. Furthermore, the compression associated with a smaller gap distance increases the etch rate as the precursor adsorption is proportional to the precursor partial pressure according to collision theory in Eq. (3).

## 3.2. Effect of the purge gas flow

The separation of the two half-reaction zones is also controlled by the amount of purge gas flow (N2 ); thus, enough purge gas is required to prevent the precursors from intermixing in the N2 enriched zones. As discussed in Section 3.1, the SALE reactor with a gap distance less than 1.00 mm shows effective precursor separation. Thus, computational fluid dynamics (CFD) simulations are performed with reactor, R1, which has a gap distance of 10.00 mm to show the noticeable differences with varying N 2 flow rates. The operating conditions of the simulations are Case 1 and Cases 5 through 7 in Table 3. The results of the simulations are presented in Fig. 7. The precursor intermixing improves as the N2 flow rate increases. Due to the higher velocity of N2 flow, additional precursor is carried out through a vacuum outlet. However, one of the drawbacks of increasing the N2 flow is that it dilutes the halfreaction zones, leading to lower mole fractions of the precursors in the half-reaction zones and thus, reducing the half-cycle reac-

tion rates. Consequently, if enough purge gas flow rate is integrated with a small gap distance, the effective precursor separation is obtained.

## 3.3. Effect of the precursor flow

The precursor flow rate is a crucial parameter in the design and optimization of SALD or SALE reactors. The CFD simulations with 4 different precursor flow rates (Cases 1, 8, 9, and 10 shown in Table 3) are performed to study the effect of precursor flow rates on precursor separation. When the flow rates of the precursors increase, the mole fractions of the precursors increase in the half-reaction zones, which accelerate the HF adsorption and TMA ligand-exchange reactions on the surface, as presented in Fig. 8. Also, Fig. 8 illustrates that the precursor intermixing in the halfreaction zones is marginally affected by changes in the precursor flow rate. However, in the N 2 zone, precursor intermixing increases with increasing precursor flow rate. Compared to Section 3.2, increasing the N2 flow rate is a more efficient method than decreasing the precursor (HF and TMA) flow rates to enhance precursor separation.

## 3.4. Effect of the substrate velocity

The effect of substrate velocity is explored using the R5 reactor configuration with a moving substrate, which is built on the basis of previous sections. As described in Section 3.1, a gap distance less than 1.00 mm ensures effective precursor separation; however, 0.25 mm is chosen to maximize precursor separation in the multiscale computational fluid dynamics (CFD) simulation. As described in Case 4, a N 2 flow rate of 500 sccm , a HF/N2 flow rate of 100/50 sccm , and a TMA/N2 flow rate of 60/100 sccm are selected for the multiscale CFD simulation. Taking into account the typical thickness of the substrate, the height of the reactor chamber is set as 1.00 mm ; however, a gap distance of 0.25 mm is preserved when the substrate moves under an injection assembly. Figs. 9 and 10 illustrate the pressure contours of the species on a moving substrate. As pictured in Figs. 9b and 10b, H2O and DMAF are generated on the surface by the collaboration of the kMC-based microscopic model and the CFD-based macroscopic model.

The substrate velocity is an important factor to control the film quality as the exposure time of the precursors to the substrate surface is directly related to the substrate velocity. Fig. 11(a) shows the etching per cycle (EPC) versus the substrate velocity. Greater EPC is observed at lower substrate velocities, which is accordant with the experiment by Sharma et al. (2015) and the CFD results by De la Huerta et al., 2018, Pan (2021). The reported etching rate of 0.46 ˚ A/cycle is obtained at velocities less than 40 mm s / . The Al2 O3 etching rate linearly reduces with increasing velocity for substrate velocities greater than 40 mm s / . This behavior can be used to determine the optimal velocity for etching Al 2 O 3 films. Film uniformity is highly required to produce conformal thin films in the semiconductor industry. Thus, a multiscale CFD simulation is performed on each node of the mesh of the surface to explore the film uniformity; therefore, 18 kinetic Monte Carlo (kMC) simulations are performed. As seen in Fig. 11(b), the uniform etch rate on the surface is observed with velocities of 80, 120, and 160 mm s / . The film conformance is quantitatively indicated by the highly low standard deviations of etched thickness for each cycle on 18 nodes of the surface mesh, which are 0.010, 0.007, and 0.002 A/cycle for ˚ 80, 120, and 160 mm s / substrate velocities, respectively. In particular, the substrate has the desired uniformity at 80 mm s / while a substrate velocity of 160 mm s / has marginal degradation of the uniformity of the film. The results imply that the short exposure time attributed to higher velocities has some surface roughness that is able to disrupt conformal etching reactions on the surface.

Fig. 11. (a) The effect of the substrate velocity on the etching per cycle. (b) The effect of the moving substrate on etching per cycle to illustrate the uniformity of the etch.

<!-- image -->

<!-- image -->

## 3.5. Effect of vacuum pumping

The vacuum pressure is another factor that is considered in this discussion since the vacuum pressure directly affects the distribution of gaseous species within the reactor and is also responsible for preventing overaccumulation of feed into the reactor. The vacuum pressure is defined as an outflow pressure boundary condition in Ansys Fluent, which is varied to determine its effects on the EPC of the substrate. The relationship between EPC and vacuum pressure for variable substrate velocities is further examined in Fig. 12, which indicates that high vacuum pressure magnitudes lead to a decrease in EPC and the vacuum pressure effects on EPC for lower substrate velocities are insignificant. Several factors contribute to the aforementioned results, including increased vacuum pressure, which decreases the partial pressure of precursors within the reaction injection zones and increasing substrate velocity results in decreased substrate exposure time to the precursors and ultimately decreased coverage and etching fractions on the substrate.

Fig. 12. The vacuum pressure versus etching per cycle relationship for several substrate velocities.

<!-- image -->

## 4. Conclusion

An optimal spatial atomic layer etching (SALE) reactor configuration was developed for thermal atomic layer etching (ALE) of Al 2 O3, which was determined by analyzing the fundamental parameters that are directly related to the conformance of the quality of the substrate film. The quality of the substrate film is based on an etch rate and substrate film uniformity obtained from the reactor configuration. An multiscale computational fluid dynamics (CFD) model was used to fabricate the relationship between the fundamental characteristics of the SALE reactor design. The multiscale CFD model was constructed by integrating a kMC-based microscopic model with a CFD-based macroscopic model. The multiscale CFD simulation revealed that the lower gap distances ensure effective separation of the precursors. Furthermore, an increase in N2 flow rate and reduction of the HF/TMA flow rate also prevent the intermixing of the precursors. However, when a sufficiently small gap distance is determined, the effects of the flow rates of the precursors and N2 are minimized. Therefore, a gap distance is the main factor in reducing N2 and precursor flow rates while preserving effective separation of the precursors. To investigate the effects of the moving substrate on Al 2 O 3 film quality, the dynamic mesh method was used to simulate the moving substrate in the optimized SALE reactor. Implementing a higher substrate velocity to the reactor configuration revealed a lower etching rate due to the reduced exposure time of the substrate. In addition, the larger vacuum pump resulted in a lower etching rate due to its strong precursor suction. As a result, the developed SALE reactor design and operating conditions were able to produce conformal ultrathin films.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT authorship contribution statement

Sungil Yun: Conceptualization, Methodology, Software, Writing - original draft. Matthew Tom: Conceptualization, Methodology, Software, Writing - original draft. Gerassimos Orkoulas: Writing - review &amp; editing. Panagiotis D. Christofides: Writing - review &amp; editing.

## Acknowledgments

Financial support from the National Science Foundation is gratefully acknowledged. The authors would like to thank Feiyang Ou and Henrik Wang for their collaboration and assistance during this project. This work used computational and storage services associated with the Hoffman2 Shared Cluster provided by the UCLA Institute of Digital Research and Educations Research Technology Group.

## References

Aghaee, M., Maydannik, P.S., Johansson, P., Kuusipalo, J., Creatore, M., Homola, T., Cameron, D.C., 2015. Low temperature temporal and spatial atomic layer deposition of TiO2 films. J. Vac. Sci. Technol. A 33 (4), 041512.

ANSYS, 2021. Ansys Fluent Theory Guide. ANSYS Inc., Canonsburg, PA.

- Cong, W., Li, Z., Cao, K., Feng, G., Chen, R., 2020. Transient analysis and process optimization of the spatial atomic layer deposition using the dynamic mesh method. Chem. Eng. Sci. 217, 115513.
- Crose, M., Zhang, W., Tran, A., Christofides, P.D., 2018. Multiscale three-dimensional CFD modeling for PECVD of amorphous silicon thin films. Comput. Chem. Eng. 113, 184-195.
- De la Huerta, C.M., Nguyen, V.H., Dedulle, J.M., Bellet, D., Jiménez, C., Mu` noz-Rojas, D., 2018. Influence of the geometric parameters on the deposition mode in spatial atomic layer deposition: a novel approach to area-selective deposition. Coatings 9, 5.
- Deng, Z., He, W., Duan, C., Chen, R., Shan, B., 2016. Mechanistic modeling study on process optimization and precursor utilization with atmospheric spatial atomic layer deposition. J. Vac. Sci. Technol. A 34 (1), 01A108.
- Ding, S.J., Wu, X., 2020. Superior atomic layer deposition technology for amorphous oxide semiconductor thin-film transistor memory devices. Chem. Mater. 32, 1343-1357.
- Ding, Y., Zhang, Y., Kim, K., Tran, A., Wu, Z., Christofides, P.D., 2019. Microscopic modeling and optimal operation of thermal atomic layer deposition. Chem. Eng. Res. Des. 145, 159-172.
- Ding, Y., Zhang, Y., Orkoulas, G., Christofides, P.D., 2020. Microscopic modeling and optimal operation of plasma enhanced atomic layer deposition. Chem. Eng. Res. Des. 159, 439-454.
- Faraz, T., Roozeboom, F., Knoops, H.C.M., Kessels, W.M.M., 2015. Atomic layer etching: what can we learn from atomic layer deposition? ECS J. Solid State Sci.Technol. 4 (6), N5023-N5032.
- Fortunato, E., Barquinha, P., Martins, R., 2012. Oxide semiconductor thin-film transistors: a review of recent advances. Adv. Mater. 24, 2945-2986.
- Freeman, D.C., Levy, D.H., Cowdery-Corvan, P.J., 2010. Method for Producing Compound Thin Films. US Patent 7,858,144 B2.
- Fu, K., Fu, Y., Han, P., Zhang, Y., Zhang, R., 2008. Kinetic Monte Carlo study of metal organic chemical vapor deposition growth dynamics of GaN thin film at microscopic level. J. Appl. Phys. 103 (10), 103524.
- Guerfi, Y., Larrieu, G., 2016. Vertical silicon nanowire field effect transistors with nanoscale gate-all-around. Nanoscale Res. Lett. 11, 210.
- , 2012. In: Jansen, A.P.J. (Ed.), An Introduction to Kinetic Monte Carlo Simulations of Surface Reactions, Vol. 1. Academic Press, London.
- Jurczak, M., Collaert, N., Veloso, A., Hoffmann, T., Biesemans, S., 2009. Review of FINFET technology. In: 2009 IEEE International SOI Conference, pp. 1-4. Foster City, CA, USA
- Kanarik, K.J., Lill, T., Hudson, E.A., Sriraman, S., Tan, S., Marks, J., Vahedi, V., Gottscho, R.A., 2015. Overview of atomic layer etching in the semiconductor industry. J. Vac. Sci. Technol. A 33, 020802.
- Kanarik, K.J., Tan, S., Gottscho, R.A., 2018. Atomic layer etching: rethinking the art of etch. J. Phys. Chem. Lett. 9, 4814-4821.
- Lee, Y., DuMont, J.W., George, S.M., 2016. Trimethylaluminum as the metal precursor for the atomic layer etching of Al2O3 using sequential, self-limiting thermal reactions. Chem. Mater. 28, 2994-3003.
- Lee, Y., Kim, G.H., Choi, B., Yoon, J., Kim, H.J., Kim, D.H., Kim, D.M., Kang, M.H., Choi, S.J., 2020. Design study of the gate-all-around silicon nanosheet MOSFETs. Semicond. Sci. Technol. 35, 03LT01.
- Levy, D.H., Nelson, S.F., Freeman, D., 2009. Oxide electronics by spatial atomic layer deposition. J. Disp. Technol. 5, 484-494.
- Li, Z., Cao, K., Li, X., Chen, R., 2021. Computational fluid dynamics modeling of spatial atomic layer deposition on microgroove substrates. Int. J. Heat Mass Transf. 181, 121854.
- Lou, Y., Christofides, P.D., 2003. Feedback control of growth rate and surface roughness in thin film growth. AIChE J. 49, 2099-2113.
- Moore, G.E., 1998. Cramming more components onto integrated circuits. Proc. IEEE 86, 82-85.
- Mu` noz-Rojas, D., Nguyen, V.H., de la Huerta, C.M., Jiménez, C., Bellet, D., 2019. Spatial atomic layer deposition. In: Chemical Vapor Deposition for Nanotechnology. IntechOpen, pp. 1-25.
- Pan, D., 2021. Density functional theory (DFT)-enhanced computational fluid dynamics modeling of substrate movement and chemical deposition process in spatial atomic layer deposition. Chem. Eng. Sci. 234, 116447.

- Pan, D., Jen, T.-C., Yuan, C., 2016. Effects of gap size, temperature and pumping pressure on the fluid dynamics and chemical kinetics of in-line spatial atomic layer deposition of Al2O3. Int. J. Heat Mass Transf. 96, 189-198.
- Pan, D., Li, T., Jen, T.C., Yuan, C., 2014. Numerical modeling of carrier gas flow in atomic layer deposition vacuum reactor: a comparative study of lattice Boltzmann models. J. Vac. Sci. Technol. A 32, 01A110.

Poodt, P., Cameron, D.C., Dickey, E., George, S.M., Kuznetsov, V., Parsons, G.N., Roozeboom, F., Sundaram, G., Vermeer, A., 2012. Spatial atomic layer deposition: a route towards further industrialization of atomic layer deposition. J. Vac. Sci. Technol. A 30 (1), 010802.

Razavieh, A., Zeitzoff, P., Nowak, E.J., 2019. Challenges and limitations of CMOS scaling for FinFET and beyond architectures. IEEE Trans. Nanotechnol. 18, 999-1004. Ritala, M., Leskelä, M., Dekker, J.P., Mutsaers, C., Soininen, P.J., Skarp, J., 1999. Perfectly conformal tin and Al2O3 films deposited by atomic layer deposition. Chem. Vap. Depos. 5, 7-9.

Sang, X., Chang, J.P., 2020. Physical and chemical effects in directional atomic layer etching. J. Phys. D 53, 183001.

Shaeri, M.R., Jen, T.C., Yuan, C.Y., 2015. Reactor scale simulation of an atomic layer deposition process. Chem. Eng. Res. Des. 94, 584-593.

- Sharma, K., Hall, R.A., George, S.M., 2015. Spatial atomic layer deposition on flexible substrates using a modular rotating cylinder reactor. J. Vac. Sci. Technol. A 33 (1), 01A132.
- Sheng, J., Lee, J.H., Choi, W.H., Hong, T., Kim, M., Park, J.S., 2018. Review article: atomic layer deposition for oxide semiconductor thin film transistors: advances in research and development. J. Vac. Sci. Technol. A 36, 060801.
- Shirazi, M., Elliott, S.D., 2014. Atomistic kinetic Monte Carlo study of atomic layer deposition derived from density functional theory. J. Comput. Chem. 35 (3), 244-259.
- Sun, W., Kim, Y., Shin, J., Yang, W., 2017. Shower Head of Combinatorial Spatial Atomic Layer Deposition Apparatus. KR Patent 20,170,025,417 A.
- Suntola, T., Antson, J., 1977. Method for Producing Compound Thin Films. US Patent 4,058,430.
- Voas, J., Kshetri, N., DeFranco, J.F., 2021. Scarcity and global insecurity: the semiconductor shortage. IT Prof. 23, 78-82.
- Ye, Z., Yuan, Y., Xu, H., Liu, Y., Luo, J., Wong, M., 2017. Mechanism and origin of hysteresis in oxide thin-film transistor and its application on 3-D nonvolatile memory. IEEE Trans. Electron. Devices 64, 438-446.
- Yun, S., Tom, M., Luo, J., Orkoulas, G., Christofides, P.D., 2022. Microscopic and datadriven modeling and operation of thermal atomic layer etching of aluminum oxide thin films. Chem. Eng. Res. Des. 177, 96-107.
- Yun, S., Tom, M., Ou, F., Orkoulas, G., Christofides, P.D., 2022. Multiscale computational fluid dynamics modeling of thermal atomic layer etching: application to chamber configuration design. Comput. Chem. Eng. 161, 107757.
- Zhang, Y., Ding, Y., Christofides, P.D., 2020. Multiscale computational fluid dynamics modeling and reactor design of plasma-enhanced atomic layer deposition. Comput. Chem. Eng. 142, 107066.
- Zywotko, D.R., Faguet, J., George, S.M., 2018. Rapid atomic layer etching of Al2O3 using sequential exposures of hydrogen fluoride and trimethylaluminum with no purging. J. Vac. Sci. Technol. A 36, 061508.