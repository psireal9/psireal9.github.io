---
layout: post
title: Euler Verfahren
---
Wir betrachten zuerst die Differentialgleichung (DFG):
\begin{equation}x^{\prime}(t)=\lambda x(t) \quad t>0 \quad (Gl.1)\end{equation}

mit gegebenem $\lambda \in \mathbb{R}$. Die DFG (GL.1) heißt:
* *gewöhnlich*, denn es treten nur Ableitung nach einer Variablen auf
* *1. Ordnung*, denn es treten nur Ableitungen höchstens 1. Ordnung auf
* *linear*, denn Linearkombinationen von Lösungen sind wieder Lösung.
* *homogen*, denn die Nullfunktion $x(t)=0 \forall t>0$ ist auch eine Lösung

Physikalische bzw ökonomische Phänomene, die von der DFG (Gl.1) beschrieben werden können, sind zB. radioaktiver Zerfall, Reaktionskinetik, Zinsenszins, etc. 

Offenbar ist 
\begin{equation}x=\alpha e^{\lambda t}\end{equation}

für jedes beliebige $\alpha \in \mathbb{R}$. Die Lösungen der linearen DFG 1.Ordnung (Gl.1) bilden sich einen eindimensionalen linearen Raum, welcher von der Basisfunktion $\psi_{1}(t)=e^{\lambda t}$ aufgespannt wird.

Als nächstes betrachten wir ein etwas schwierigeres Problem, nämlich die DFG
\begin{equation}x^{\prime}(t)=\lambda x(t)+f(t) \quad t>0  (Gl.2)\end{equation}

mit einer gegebenen Funktion $f \in C[0, \infty)$. Ist $f \neq 0$ (nicht wie (Gl.1)), so ist die Nullfunktion **keine** Lösung von (Gl.2). Die DFG wird nun **inhomogen**. Alle Lösungen von (Gl.2) haben die Gestalt. 
\begin{equation}x(t)=\alpha e^{\lambda t}+\int_{0}^{t} f(\eta) e^{\lambda(t-\eta)} d \eta\end{equation}

mit einer beliebigen Konstanten $\alpha \in \mathbb{R}$. Die Lösungen von (Gl.2) bilden einen eindimensionalen **affinen** Raum (Vektorraum, welcher bei einem festen Wert verschoben wird).

Wir interessieren uns nun für das zugehörige Anfangswertproblem (AWP) von (Gl.2)
\begin{equation}\begin{array}{l}
x^{\prime}(t)=\lambda x(t)+f(t) \quad 0<t \leq T \\
x(0)=x_{0} \quad (Gl.3)
\end{array}\end{equation}

*Falls ich noch Zeit habe, sage ich etwas über die **Existenz** und **Eindeutigkeit** einer Lösung*

In diesem Post werden wir das Euler Verfahren, die einfachste Methode zur Lösung von AWP (Gl.3) diskutieren.
Ich möchte zuerst (Gl.3) wie folgt umschreiben 
\begin{equation}\begin{array}{l}
x^{\prime}(t)=g(x(t),t) \quad 0<t \leq T \\
x(0)=x_{0} \quad (Gl.4)
\end{array}\end{equation}

Wir können uns die DFG $x^{\prime}(t)=g(x(t),t)$ durch das zugehörige Richtungsfeld veranschaulichen. 


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


x = np.arange(-2,2.2,0.2)
y = np.arange(-2,2.2,0.2)


X, Y = np.meshgrid(x, y)
u=1
v= np.exp(X)-(1/2)*X**2-X #die Ableitung 

# exakte Lösung
x_sol=np.linspace(-2,0.9)
sol=np.exp(x_sol)-(1/2)*x_sol**2

fig, ax = plt.subplots(figsize=(9,9))
ax.quiver(X,Y,u,v)
ax.plot(x_sol,sol)

plt.show()

```


![image alt ><](../images/output_2_0.png#center)
