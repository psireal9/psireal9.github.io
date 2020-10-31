---
layout: post
title: Euler Verfahren
---
### Einführung in Lineare Differentialgleichungen 1. Ordnung
Wir betrachten zuerst die Differentialgleichung (DFG):
\begin{equation}x^{\prime}(t)=\lambda x(t) \quad t>0 \quad (Gl.1)\end{equation}

mit gegebenem $\lambda \in \mathbb{R}$. Die DFG (GL.1) heißt:
* *gewöhnlich*, denn es treten nur Ableitung nach einer Variablen auf
* *1. Ordnung*, denn es treten nur Ableitungen höchstens 1. Ordnung auf
* *linear*, denn Linearkombinationen von Lösungen sind wieder Lösung.
* *homogen*, denn die Nullfunktion $x(t)=0 \forall t>0$ ist auch eine Lösung

Physikalische bzw ökonomische Phänomene, die von der DFG (Gl.1) beschrieben werden können, sind zB. radioaktiver Zerfall, Reaktionskinetik, Zinsenszins, etc. 

Offenbar ist 
\begin{equation}x=\alpha e^{\lambda t} \quad (Gl.2)\end{equation}

für jedes beliebige $\alpha \in \mathbb{R}$. Die Lösungen der linearen DFG 1.Ordnung (Gl.1) bilden sich einen eindimensionalen linearen Raum, welcher von der Basisfunktion $\psi_{1}(t)=e^{\lambda t}$ aufgespannt wird.

Als nächstes betrachten wir ein etwas schwierigeres Problem, nämlich die DFG
\begin{equation}x^{\prime}(t)=\lambda x(t)+f(t) \quad t>0  \quad (Gl.3)\end{equation}

mit einer gegebenen Funktion $f \in C[0, \infty)$. Ist $f \neq 0$ (nicht wie (Gl.1)), so ist die Nullfunktion **keine** Lösung von (Gl.3). Die DFG wird nun **inhomogen**. Alle Lösungen von (Gl.2) haben die Gestalt. 
\begin{equation}x(t)=\alpha e^{\lambda t}+\int_{0}^{t} f(\eta) e^{\lambda(t-\eta)} d \eta \quad (Gl.4)\end{equation}

mit einer beliebigen Konstanten $\alpha \in \mathbb{R}$. Die Lösungen (Gl.4) bilden einen eindimensionalen **affinen** Raum (Vektorraum, welcher bei einem festen Wert verschoben wird).

Wir interessieren uns nun für das zugehörige Anfangswertproblem (AWP) von (Gl.3)
<p align="center">
  $$\begin{align}
x^{\prime}(t) &=\lambda x(t)+f(t) \quad 0<t \leq T  \\
x(0) &=x_{0} \quad (Gl.5)
\end{align}$$
</p>

In diesem Post werden wir das Euler Verfahren, die einfachste Methode zur Lösung von AWP (Gl.3) diskutieren.
Ich möchte zuerst (Gl.3) wie folgt umschreiben
<p align="center">
  $$\begin{align}
x^{\prime}(t) &=g(x(t),t) \quad 0<t \leq T  \\
x(0) &=x_{0} \quad (Gl.4)
\end{align}$$
</p>

Wir können uns die DFG $x^{\prime}(t)=g(x(t),t)$ durch das zugehörige Richtungsfeld veranschaulichen. Zu jedem Punkt $(x, t) \in \mathbb{R}^{2}$ zeichnen wir dabei einen Richtungspfeil mit Steigung $g(x(t),t)$, z.B. den Vektor $(1, g(x, t))^{T}$. Eine Funktion löst die DGL genau dann, wenn an jedem Punkt durch den die Funktion geht, die Steigung der Funktion und die Steigung des Richtungspfeils übereinstimmen. Gegeben den Anfangswert $x(t=0)=x_{0}$ können wir die DGL zeichnerisch lösen, indem wir ausgehend vom Startwert $(0,x_{0})$ die Funktion passend zu den Richtungspfeilen zeichnen. Als Beispiel betrachten wir die Funktion $x(t)=e^{t}-\frac{1}{2}t^{2}$, die entsprechende DFG $x^{\prime}=e^{t}-t$ und der Startwert $x(0)=1$


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


x = np.arange(-2,2.2,0.2)
t = np.arange(-2,2.2,0.2)


X, T = np.meshgrid(x, t)
u=1
v= np.exp(T)-T #die Ableitung 

# exakte Lösung
t_sol=np.linspace(-2,0.9)
sol=np.exp(t_sol)-(1/2)*t_sol**2

fig, ax = plt.subplots(figsize=(9,9))
ax.quiver(X,T,u,v)
ax.plot(t_sol,sol, label='exakte Lösung')

plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.title(r'Abb 1: Richtungsfeld einer DGL und Lösung zu Anfangswert $x_{0}$')
plt.show()

```
![image alt ><](../images/output_2_0.png#center)

### Euler Verfahren
Wir wollen nun numerische Verfahren zur näherungsweisen Lösung des AWPs (Gl.3) mit der exakten Lösung (Gl.4) konstruieren und analysieren. Dazu wählen wir zunächst ein äquidistanter Gitter, wobei die Schrittweite $\tau$ konstant ist.

<p align="center">
  $$\begin{align}
\Delta &=\left\{0=t_{0}<t_{1}<\cdots<t_{n}=T\right\}  \\
\tau &=t_{k+1}-t_{k}
\end{align}$$
</p>
Der nächster Punkt $x_{1}$ lässt sich anhand der Taylor-Entwicklung erster Ordnung mit $x_{0}=x{0}$ als Entwicklungspunkt approximieren.
$$
\begin{aligned}
x(t_{1}) &\approx x(t_{0}) + \tau \cdot x'(t_{0}) \\
&= x_{0} + \tau \cdot (\lamda x_{0}+f(t_{0})) = x_{1}
\end{aligned}
$$

### Anwendung in physikalischen Modellen
Jetzt können wir sehen, wie der explizite Euler-Algorithmus beim Zeichnen der Flugbahn verwendet werden kann. Wir betrachten zuerst den klassischen harmonischen Oszillator.


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def V(k,x):
    return (1/2)*k*x**2

def classical_HO(t,A=25,w0=0.2,phi=0):
    x = A*np.sin(w0*t+phi)
    v = A*w0*np.cos(w0*t+phi)
    return x,v

T = 10*np.pi

def Euler(r0,v0,k,timestep,T,m):
    '''
    Input
    timestep: floating ('0.2'T -> consider only 0.2) 
    '''
    n = round(10/timestep) # length of each simulation is 10T
    #index = np.arange(1,n+1,1)
    #t = [0+ u*timestep*T for u in index]
    r = np.zeros(n+1)
    v = np.zeros(n+1)
    r[0]=r0
    v[0]=v0
    for i in range(1,n+1):
        r[i] = r[i-1]+v[i-1]*timestep*T+(1/(2*m))*(-k*r[i-1])*(timestep*T)**2
        v[i] = v[i-1]+(1/m)*(-k*r[i-1])*timestep*T
    
    return r,v


time=np.linspace(0,10*T,101)
x,v = classical_HO(time)

fig, ax = plt.subplots(2,2)
ax[0, 0].plot(time,Euler(0,5,0.2,0.1,T,5)[0],label='Euler,x')
ax[0, 0].plot(time,x,'--',label='Analytical,x', color='tab:blue')
ax[0, 0].set_xlabel('t(s)')
ax[0, 0].set_ylabel('x(m)')
ax[0, 0].legend(loc="upper left")

ax[0, 1].plot(time,Euler(0,5,0.2,0.1,T,5)[1],label='Euler,v',color='tab:orange')
ax[0, 1].plot(time,v,'--',label='Analytical,v', color='tab:orange')
ax[0, 1].set_xlabel('t(s)')
ax[0, 1].set_ylabel('v(m/s)')
ax[0, 1].legend(loc="lower left")

ax[1, 0].plot(x,v,color='tab:green')
ax[1, 0].set_xlabel('x(s)')
ax[1, 0].set_ylabel('v(m/s)')
ax[1, 0].set_title('Analytical phase space')

ax[1, 1].plot(Euler(0,5,0.2,0.1,T,5)[0],Euler(0,5,0.2,0.1,T,5)[1],color='tab:red')
ax[1, 1].set_xlabel('x(s)')
ax[1, 1].set_ylabel('v(m/s)')
ax[1, 1].set_title('Euler phase space')

fig.tight_layout()
plt.show()
```



![image alt ><](../images/test2png.png#center)


```python

```



