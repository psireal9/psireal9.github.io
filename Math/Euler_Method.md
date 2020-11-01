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
x(0) &=x_{0} \quad (Gl.6)
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
Für die absolute Kondition  $k_{abs}$ des AWPs (Gl.5) gilt

<p align="center">
$$\begin{array}{l}
  \underline{\lambda < 0}: \qquad 1 \leq k_{abs}(AWP) \leq 1+T \\
  \underline{\lambda \geq 0}: \qquad e^{\lambda T} \leq k_{abs}(AWP) \leq (1+T)e^{\lambda T}
\end{array}$$
</p>

### Euler Verfahren
Wir wollen nun numerische Verfahren zur näherungsweisen Lösung des AWPs (Gl.3) mit der exakten Lösung (Gl.4) konstruieren und analysieren. Dazu wählen wir zunächst ein äquidistanter Gitter, wobei die Schrittweite $\tau$ konstant ist.

<p align="center">
  $$\begin{align}
\Delta &=\left\{0=t_{0}<t_{1}<\cdots<t_{n}=T\right\}  \\
\tau &=t_{k+1}-t_{k}
\end{align}$$
</p>
Der nächster Punkt $x_{1}$ lässt sich anhand der Taylor-Entwicklung erster Ordnung mit $x_{0}=x(t_{0})$ als Entwicklungspunkt approximieren.
  
<p align="center">
  $$
\begin{aligned}
x(t_{1}) &\approx x(t_{0}) + \tau \cdot x'(t_{0}) \\
&= x_{0} + \tau \cdot (\lambda x_{0}+f(t_{0})) = x_{1}
\end{aligned}
$$
</p>

Indem wir auf die gleiche Weise fortfahren, erhalten wir das Euler’sche Polygonzugverfahren, eine iterative Formel zur Berechnung der Zeitentwicklung von $x$.
\begin{equation}
x_{k+1}=x_{k}+\tau\left(\lambda x_{k}+f\left(t_{k}\right)\right), \quad k=0, \ldots, n-1 \quad (Gl.7)
\end{equation}

Wir werden auch die Gitterfunktion einführen, die später verwendet wird, um die diskrete Kondition zu bestimmen
\begin{equation}
x_{\Delta}\left(t_{k}\right)=x_{k}, \quad k=0, \ldots, n
\end{equation}

Da (Gl.7) eine explizite Vorschrift zur Berechnung von $x_{k+1}$ liefert, nennt man dieses Verfahren auch **explizites Euler-Verfahren**, welches sich durch den vorwärtsgenommenen Differenzenquotienten lässt.
\begin{equation}
\frac{x_{k+1}-x_{k}}{\tau}=\lambda x_{k}+f\left(t_{k}\right), \quad k=0, \ldots, n-1
\end{equation}

Verwendet man stattdessen den rückwartsgenommenen Differenzenquotienten, so ergibt sich das **implizite Euler-Verfahren**
<p align="center">
  $$\frac{x_{k+1}-x_{k}}{\tau}=\lambda x_{k+1}+f\left(t_{k+1}\right), \quad k=0, \ldots, n-1 $$
</p>
<p align="center">
  $$\Rightarrow x_{k+1}=\frac{1}{1-\tau \lambda}\left(x_{k}+f\left(t_{k+1}\right)\right), \quad k=0, \ldots, n-1 \quad (Gl.8) $$
</p>

Die Frage ist nun, wann welches Verfahren anzuwenden ist? Betrachten wir eine homogene DFG der Form (Gl.1), wobei $\lambda = -21$, $x_{0}=1$, $T=1$ und $\tau = \frac{1}{10}$ (also 10 Teilintervalle).

```python
import numpy as np
import matplotlib.pyplot as plt

def explicitEuler(A, f, x0, T, n):
    '''
    Solve x'(t) = lambda*x(t) + f(t), x(0) = x0
    Input
        lambda = A
        x0: Anfangswert
        n: Zeitintervall
        T: Endzeitpunkt
    Output
        x ∈ R^(n+1) (inklusive Startwert)
    '''

    x = np.zeros(n+1)
    x[0] = x0
    t = [0 + (i/n) * (T - 0) for i in range(n)]
    tau = T/n
    for k in range(0,n):
        x[k+1] = x[k] + tau*(A*x[k]+f(t[k]))
        #x[k + 1] = x[k] + tau * (A * x[k])
    return x

def implicitEuler(A, f, x0, T, n):
    '''
    Solve x'(t) = lambda*x(t) + f(t), x(0) = x0
    Input
        lambda = A
        x0: Anfangswert
        n: Zeitintervall
        T: Endzeitpunkt
    Output
        x ∈ R^(n+1) (inklusive Startwert)
    '''

    x = np.zeros(n+1)
    x[0] = x0
    t = [0 + (i/n) * (T - 0) for i in range(n+1)]
    tau = T/n
    for k in range(0,n):
        x[k+1] = (1/(1-tau*A))*(x[k]+tau*f(t[k+1]))

    return x

def exact_solution(A,x0,t):
    return x0*np.exp(A*t)

time = np.linspace(0,1,11)
plt.plot(time, explicitEuler(-21, lambda x:0, 1, 1, 10), label='explicit Euler')
plt.plot(time, exact_solution(-21,1,time), label='exact solution')
plt.plot(time, implicitEuler(-21, lambda x:0, 1, 1, 10), label='implicit Euler')
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.show()

```
  
![image alt ><](../images/output_3_0.png#center)

Um das unterschiedliche Verhalten der beiden Verfahren zu verstehen, wenden wir uns an die Auswirkung von Störungen des Anfangswerts und der rechten Seite auf die berechnete Gitterfunktion, welche zusammen als **diskrete Kondition**, $\Vert x_{\Delta}-\tilde{x}_{\Delta} \Vert _{\infty}$, bezeichnet wird. Für explizites Euler-Verfahren gilt nämlich:

<p align="center">
$$\begin{align}
  \underline{\lambda < 0} \quad \text{und} \quad \underline{\tau < \frac{2}{|\lambda|}}: \qquad & 1 \leq k_{abs}(exEuler) \leq 1+T \\
  \underline{\lambda \geq 0}: \qquad & e^{\lambda T} \leq k_{abs}(exEuler) \leq (1+T)e^{\lambda T}
\end{align}$$
</p>

Vergleichen wir mit $k_{abs}(AWP)$, dann sehen wir, dass es $k_{abs}(exEuler) \leq k_{abs}(AWP)$ gilt. Im Vergleich zum kontinuierlichen Problem findet also *keine zusätzliche Fehlerverstärkung statt*. Das explizite Euler-Verfahren ist damit <u>stabil</u>. Im Falle $\lambda < 0$ ist die Stabilität allerdings an die Bedingung $0 < \tau < \frac{2}{\vert \lambda \vert}$. Ist diese verletzt, so folgt

<p align="center">
$$
\Vert x_{\Delta}-\tilde{x}_{\Delta} \Vert _{\infty}=\sigma \vert x_{0}-\tilde{x}_{0} \vert , \quad \sigma \gg 1
$$
</p>

Man kann (Gl.7) für $f(t)=0$ wie folgt umschreiben
\begin{equation}
x_{k+1}=x_{k}+\tau \lambda x_{k} = (1+ \tau \lambda)^{k+1} \cdot x_{0}
\end{equation}

Für $\tau > \frac{2}{|\lambda|}$ (wie in unserem Beispiel) ist $1+ \tau \lambda < -1$. Wenn $k+1$ gerade ist, ist $(1+ \tau \lambda)^{k+1} > 1$ und wenn $k+1$ ungerade ist, ist $(1+ \tau \lambda)^{k+1} < -1$. Daher sehen wir nach jedem Zeitschritt $t_{k}$ einen Wechsel zwischen positivem und negativem Wert. Mit wachsendem $k$ haben exakte Lösung und Näherung also nichts mehr miteinander zu tun. Problematisch sind dabei sicher nicht irgendwelche *Rundungsfehler*, z.B. bei der Eingabe des An-
fangswertes. Stabilität scheint notwendig für die *Konvergenz des Verfahrens*!

Das implizite Euler-Verfahren ist im Falle $\lambda <0$ für beliebiege Schrittweiten $\tau > 0$ stabil, d.h. es gilt $1 \leq k_{abs}(exEuler) \leq 1+T, \quad \lambda <0$. Im Falle $\lambda >0 $ gibt es beim impliziten Euler-Verfahren Probleme: Um Oszillationen zu
vermeiden und auch um die Durchführbarkeit des Verfahrens zu sichern, muß die Stabilitätsbedingung $\tau < \frac{1}{\lambda}$ erfüllt sein. Wenn $\tau > \frac{1}{\lambda}$ ist, ist $\frac{1}{1-\tau \lambda}<1$ und dann wechselt wieder $x_{k+1}$ zwischen positivem und negativem Wert, bis $\frac{1}{1-\tau \lambda} \cdot f(t_{k+1})$ so negativ, dass die alle folgenden $x_{k+1}$ negativ sind. (Zum Ausprobieren: $\lambda = 16, f(t)=t, T=8, x_{0}=1, n=60 oder n=120$) 

### Anwendung in physikalischen Modellen
Jetzt können wir sehen, wie das explizite Euler-Verfahren beim Zeichnen der Flugbahn verwendet werden kann. Wir betrachten nun den klassischen harmonischen Oszillator. Um die Newton-Gleichung mit der Euler-Methode zu integrieren, fügen wir den zweiten Term hinzu.
\begin{equation}
\mathbf{r}_{i}(t+\Delta)=\mathbf{r}_{i}(t)+\mathbf{v}_{i}(t) \Delta+\frac{1}{2 m_{i}} \mathbf{F}_{i}(t) \Delta^{2}+\mathcal{O}\left(\Delta^{3}\right)
\end{equation}

\begin{equation}
\mathbf{v}_{i}(t+\Delta)=\mathbf{v}_{i}(t)+\frac{1}{m_{i}} \mathbf{F}_{i}(t) \Delta+\mathcal{O}\left(\Delta^{2}\right)
\end{equation}


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


Der Euler-Integrator ist nicht zeitumkehrbar und konserviert keine Energie. 
Wir können die Kontraktion des Volumens des Phasenraums sehen, wie es auftreten würde, wenn die Energiedissipation stattfindet. Es wird daher nicht für dynamische Simulationen empfohlen.

Der Inhalt dieses Posts wurde geschrieben basierend auf: 
1. *Vorlesungskript zum Computerorientierte Mathematik II (FU Berlin)*
2. *Vorlesungskript zum Moleküldynamik (FU Berlin)*

