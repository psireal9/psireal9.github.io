---
layout: post
title: Crystal Vibrations
---

<u> Motivation: </u>
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

<font size="3px"> <em>Normal mode of vibration: a vibration in which all the nuclei undergo <b>harmonic motion</b>, have the same $\nu_{vib}$ and move in phase but generally with <b>differrent amplitudes</b>. </em> </font> 



<u>Why is it important?</u>
* The Einstein model employed Planck's quantization assumption -> Important piece of evidence for the need of quantization
* Exkurs: Dulong-Petit law (End of the post)



<u>Goal:</u>
* Determine formulas of all thermodynamic functions of the Einstein Crystal Model

<u>Idea:</u>
* Decompose complex vibration of a polyatomic molecule into a superposition of normal modes

* The vibration of each of these normal modes can be described in which you employ the QM model for vibrational DOF which is the **harmonic oscillator**. In this case, all of these independent harmonic oscillators will have the same specific ground state frequency $\nu$

From the post *Molecular Partition Functions*, we know that the single-particle total vibrational partion function is given by 
<a name="abcde">
  \begin{equation}
  q_{vib}=\prod_{i=1}^{3N_{\text {atom }}-6(5)} q_{\text {vib }}\left(\frac{h\cdot \nu_{i}}{k_{B} \cdot T} \right) \quad [Eq.1]
  \end{equation}
</a>

The relation between the canonical partition function $Q$ and the unit partition function $q$ is
<p align="center">
  <a name="cde">
  $$ Q=q^{N} \quad \text{for}\quad N \quad \text{distinguishable units} \quad [Eq.2]$$
  </a>  
</p>
For a monoatomic crystal with $N$ atoms, its vibrational energy is given by
<p align="center">
  <a name="eq3">
  $$ E_{\mathrm{vib}}=U_{0}+\sum_{i=1}^{3 N-6} h v \nu_{i} \approx U_{0}+\sum_{i=1}^{3 N} h v \nu_{i} \quad [Eq.3]$$
    </a>
</p>

where $U_{0}$ is the crystal's ground vibrational energy. For a crystal with large number of atoms $N$, the number of normal modes $3N-6$ can be replaced with $3N$.

Combining [[Eq.1]](#abcde), [[Eq.2]](#cde), and [[Eq.3]](#eq3), we can see that the canonical partition function for the whole crystal is
<p align="center">
  <a name="eq4">
  $$Q=e^{-U_{0} / k_{\mathrm{B}} T} q^{3 N} [Eq.4]$$
   </a>
</p>

[[Eq.4]](#eq4) makes sense since $U_{0}$ is only a constant so when you take the exponential of [[Eq.3]](#eq3), you can bring $e^{-U_{0} / k_{\mathrm{B}} T}$ out of the summation and product. What's left is $\prod_{i=1}^{3 N}\left(\sum_{v_{i}=0}^{\infty} e^{-h \nu v_{i} / k_{\mathrm{B}} T}\right) $ and since all normal modes share the same frequency $\nu$, hence the product can be written in terms of power $\left(\sum_{i=0}^{\infty} e^{-h \nu v_{i} / k_{\mathrm{B}} T}\right)^{3 N}$. [[Eq.4]](#eq4) is therefore linked with [[Eq.2]](#cde) because the normal modes are distinguishable from each other. In other words, the vibrational DOF are separable!

The second step involves determining $\ln Q$ as you can derive other thermodynamic functions when you have it! You now can insert the formula for $q_{vib}$ into 
[[Eq.4]](#eq4)
<p align="center">
  <a name="eq5">
  $$\begin{aligned} \ln (\mathcal{Z}) &=-\frac{U_{0}}{k_{\mathrm{B}} T}+3 N \ln (z)=-\frac{U_{0}}{k_{\mathrm{B}} T}+3 N \ln \left(\frac{1}{1-e^{-h \nu / k_{\mathrm{B}} T}}\right) \\

&=-\frac{U_{0}}{k_{\mathrm{B}} T}-3 N \ln \left(1-e^{-h \nu / k_{\mathrm{B}} T}\right) \end{aligned} [Eq.5]$$
  </a>
</p>

I find the derivation of heat capacity from [Wikipedia](https://en.wikipedia.org/wiki/Einstein_solid) quite thorough and understandable. The article also reminds you about counting problem of Bosons and Fermions because the first follows **Bose-Einstein statistics** and the latter follows **Fermi-Dirac statistics**. Anyhoo, if you have time, take a quick look!

You can find other formulas for other thermodynamic functions of the Einstein Model in Mortimer. It's quite lengthy so I will skip that here. Instead, we will discuss the results delivered by the model

<u>Problem:</u>
* Pressure in Einstein Model

It is not obvious from [[Eq.5]](#eq5) how $\ln (\mathcal{Z})$ is related to $V$. A possible way to tackle this is to use $G=A+P V$
<p align="center">
  $$A=-k_{\mathrm{B}} T \ln (\mathcal{Z})=U_{0}+3 N k_{\mathrm{B}} T \ln \left(1-e^{-h v / k_{\mathrm{B}} T}\right)$$
</p>
<p align="center">
  $$\begin{aligned}
G &=N \mu=U_{0}-3 N k_{\mathrm{B}} T \ln (z) \\
&=U_{0}+3 N k_{\mathrm{B}} T \ln \left(1-e^{-h v / k_{\mathrm{B}} T}\right)
\end{aligned}$$
</p>

This means $G=A$. What does this imply?
<p align="center">
  $$\text{Enthalpy}: \quad H \stackrel{\text { def }}{=} U+p V$$
</p>
<p align="center">
  $$\text{Helmholtz Energy:} \quad A \stackrel{\text { def }}{=} U -TS $$
</p>
<p align="center">
  $$\text{Gibbs Energy:} \quad G \stackrel{\text { def }}{=} U -TS + pV = H -TS $$
</p>
This means $U=H$ and $pV=0$. The term $pV$ represents the work that would required to "make room" for the system by pushing the atmospheric pressure. Thus, in a way, the Einstein Model suggests the solid exists in a vacuum (where $p=0$) because the solid, of course, does have a volume!

<u>Exercise 1:</u>
The value of the Einstein temperature $\Theta_E$ that fits the Einstein crystal model heat-capacity formula to aluminum data is 240 K.

1. What is the vibrational frequency corresponding to this value of the parameter?
2. Draw a graph of the heat capacity of aluminum from 0 to 300 K, according to the Einstein model.
3. At what temperature does the prediction of the Einstein model for the heat capacity of aluminum come within 5.00% of the law of Dulong and Petit? At what temperature does it come within 1.00% of the law of Dulong and Petit?

<u>Solution 1:</u>
* Vibrational/Einstein temperature  $\Theta_E$ is used as high temperature approximation to $q_{V}$
\begin{equation}\Theta_{E}=\frac{h c \tilde{\nu}}{k}\end{equation}
We can plug $\Theta_E$ into the vibrational partition function as follows:

\begin{equation}q_{V}=\frac{1}{1-e^{-\beta h c \widetilde{\nu}}}=\frac{1}{1-e^{-h c \widetilde{\mathcal{N}} / k T}}=\frac{1}{1-e^{-\Theta_{E} / T}}\end{equation}

The Taylor's series expansion for $e^{-x}$ is $e^{-x}=1-\frac{x}{1 !}+\frac{x^{2}}{2 !}-\frac{x^{3}}{3 !}(-1)+\ldots$

So when $T>>\Theta_{E}$, terms of higher oders ($\leq 2$) in $e^{-\Theta_{E} / T}$ are terribly small enough to be truncated. Hence, we end up with a high-temperature limit for $q_{V}$
\begin{equation}q_{V}=\frac{1}{1-e^{-\Theta_{V} / T}}=\frac{1}{1-\left(1-\frac{\Theta_{V}}{T}\right)}=\frac{T}{\Theta_{V}} \end{equation}

* Thus, the virbational frequency at any $\Theta_E$ is $\nu = \frac{k_B\Theta_E}{h}$

```python
theta_E = 240 # einstein temperature in K
nu = k*theta_E/h
print(f"nu = {nu:.8e} s^-1")

```

    nu = 5.00079232e+12 s^-1
    
* Plot $C_{V}(T)$

```python
T = np.linspace(1,300,1000)
cv = 3*Nav*k*(theta/T)**2*np.exp(theta/T)/(np.exp(theta/T)-1)**2

plt.figure(figsize=(10,6))
plt.plot(T,cv,label='Einstein model')
plt.hlines(3*Nav*k,xmin=1,xmax=300,label='Dulong-Petit')
plt.legend()
plt.xlabel(r'$T(K)$')
plt.ylabel(r'$c_V $(J/mol.K)')

```




![img](lanyon/images/output_5_1.png )

The post's content was written based on 
1. *Mortimer, R. G. (n.d.). Chapter 28 The structure of Solids,Liquids, and Polymers. In Physical Chemistry (3rd ed., pp. 1162-1171).*
2. *Lecture Note of Prof.Dr.Bettina Keller*
3. *Wikipedia [page](https://en.wikipedia.org/wiki/Einstein_solid)*
