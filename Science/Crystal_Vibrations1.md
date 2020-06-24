---
layout: post
title: Crystal Vibrations
---
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script>
  
<u> Motivation </u>
* Study 2 model systems that represent the vibrations of a crystal
    1. Einstein Crystal Model
    2. Debye Crystal Model

### Einstein Crystal Model
Einstein solid is a model of solid based on 2 assumptions:
* Each atom in the lattice is an **indenpedendent** 3D quantum HO
* All of the vibrational normal modes oscillate with the same frequency

<u>Reality:</u>

A solid is, indeed, comprised of **independent oscillations**, these oscillations are collective(normal) modes involving many atoms. 

In Einstein model, **each atom** oscillates independently.

<font size="1"> <em>Normal mode of vibration: a vibration in which all the nuclei undergo **harmonic motion**, have the same $\nu_{vib}$ and move in phase but generally with **differrent amplitudes** </em> </font> 


<u>Why is it important?</u>
* The Einstein model employed Planck's quantization assumption -> Important piece of evidence for the need of quantization
* Exkurs: Dulong-Petit law (End of the post)



<u>Goal:</u>
* Determine formulas of all thermodynamic functions of the Einstein Crystal Model

<u>Idea:</u>
* Decompose complex vibration of a polyatomic molecule into a superposition of normal modes

* The vibration of each of these normal modes can be described in which you employ the QM model for vibrational DOF which is the **harmonic oscillator**. In this case, all of these independent harmonic oscillators will have the same specific ground state frequency $\nu$

From the post *Molecular Partition Functions*, we know that the single-particle total vibrational partion function is given by
$$ q_{vib}=\prod_{i=1}^{3N_{\text {atom }}-6(5)} q_{\text {vib }}\left(\frac{h\cdot \nu_{i}}{k_{B} \cdot T} \right) \quad [Eq.1]$$

The relation between the canonical partition function $Q$ and the unit partition function $q$ is
$$Q=q^{N} \quad \text{for}\quad N \quad \text{distinguishable units} \quad [Eq.2]$$

For a monoatomic crystal with $N$ atoms, its vibrational energy is given by
$$E_{\mathrm{vib}}=U_{0}+\sum_{i=1}^{3 N-6} h v \nu_{i} \approx U_{0}+\sum_{i=1}^{3 N} h v \nu_{i} \quad [Eq.3]$$
where $U_{0}$ is the crystal's ground vibrational energy. For a crystal with large number of atoms $N$, the number of normal modes $3N-6$ can be replaced with $3N$.

Combining [Eq.1], [Eq.2], and [Eq.3], we can see that the canonical partition function for the whole crystal is 
$$Q=e^{-U_{0} / k_{\mathrm{B}} T} q^{3 N} [Eq.4]$$

[Eq.4] makes sense since $U_{0}$ is only a constant so when you take the exponential of [Eq.3], you can bring $e^{-U_{0} / k_{\mathrm{B}} T}$ out of the summation and product. What's left is $\prod_{i=1}^{3 N}\left(\sum_{v_{i}=0}^{\infty} e^{-h \nu v_{i} / k_{\mathrm{B}} T}\right) $ and since all normal modes share the same frequency $\nu$, hence the product can be written in terms of power $\left(\sum_{i=0}^{\infty} e^{-h \nu v_{i} / k_{\mathrm{B}} T}\right)^{3 N}$. [Eq.4] is therefore linked with [Eq.2] because the normal modes are distinguishable from each other. In other words, the vibrational DOF are separable!

The second step involves determining $\ln Q$ as you can derive other thermodynamic functions when you have it! You now can insert the formula for $q_{vib}$ into [Eq.4]

$\begin{aligned} \ln (\mathcal{Z}) &=-\frac{U_{0}}{k_{\mathrm{B}} T}+3 N \ln (z)=-\frac{U_{0}}{k_{\mathrm{B}} T}+3 N \ln \left(\frac{1}{1-e^{-h \nu / k_{\mathrm{B}} T}}\right) \\ &=-\frac{U_{0}}{k_{\mathrm{B}} T}-3 N \ln \left(1-e^{-h \nu / k_{\mathrm{B}} T}\right) \end{aligned} [Eq.5]$

I find the derivation of heat capacity from [Wikipedia](https://en.wikipedia.org/wiki/Einstein_solid) quite thorough and understandable. The article also reminds you about counting problem of Bosons and Fermions because the first follows **Bose-Einstein statistics** and the latter follows **Fermi-Dirac statistics**. Anyhoo, if you have time, take a quick look!

You can find other formulas for other thermodynamic functions of the Einstein Model in Mortimer. It's quite lengthy so I will skip that here. Instead, we will discuss the results delivered by the model

<u>Problem:</u>
* Pressure in Einstein Model

It is not obvious from [Eq.5] how $\ln (\mathcal{Z})$ is related to $V$. A possible way to tackle this is to use $G=A+P V$
$$A=-k_{\mathrm{B}} T \ln (\mathcal{Z})=U_{0}+3 N k_{\mathrm{B}} T \ln \left(1-e^{-h v / k_{\mathrm{B}} T}\right)$$

$$\begin{aligned}
G &=N \mu=U_{0}-3 N k_{\mathrm{B}} T \ln (z) \\
&=U_{0}+3 N k_{\mathrm{B}} T \ln \left(1-e^{-h v / k_{\mathrm{B}} T}\right)
\end{aligned}$$

This means $G=A$. What does this imply?

$$\text{Enthalpy}: \quad H \stackrel{\text { def }}{=} U+p V$$
$$\text{Helmholtz Energy:} \quad A \stackrel{\text { def }}{=} U -TS $$
$$\text{Gibbs Energy:} \quad G \stackrel{\text { def }}{=} U -TS + pV = H -TS $$

This means $U=H$ and $pV=0$. The term $pV$ represents the work that would required to "make room" for the system by pushing the atmospheric pressure. Thus, in a way, the Einstein Model suggests the solid exists in a vacuum (where $p=0$) because the solid, of course, does have a volume!
