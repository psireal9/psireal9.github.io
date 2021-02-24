---
layout: post
title: Introduction
<--!sticky: true-->
---

Obviously, it's getting harder and harder to solve scientific problems with only pen and paper. Not that people have nothing to do on a Friday evening but write down the state-space of $k$ harmonic oscillators with $n$ energy level per oscillator. Hence, I can't stress enough the significance of computer in the advancement of science. I can barely perform Gaussian elimination correctly on a 4x4 matrix so imagine a 15x15 matrix of atom coordinates of the simple methane molecule. You gotta leave that to the copmuter. However, as easy as the path to a quick answer may seem to be, the mine field is full of booby traps. Take for example, if you evaluate $f(x)=x^{3}+12 a^{2} x-6 a x^{2}-8 a^{3}=(x-2 a)^{3}$ with the parameter $a = 49999.5$ at $x_{0}=1000000.05$ with 2 different but equivalent transformations, you wil get immensely different results! 
```python
x0 = 1000000.05
a = 49999.5
def f1(x):
    return x**3 + 12*a**2*x - 6*a*x**2 - 8*a**3
f1(x0)
```




    7.290025515029768e+17




```python
def f2(x):
    return (x-2*a)**3

f2(x0)
```




    -7.289995018501133e+20

Thus, if you are not careful with numerical calcuation, problems including but not limited to cancelllation, Runge phenomenon may make your algorithm shockingly unstable. With this blog, I hope to lay out some of the pitfalls that I am aware of while simultaneously show you the overwhelming joy of simulating physical and theoretical problems. It's addictive!

However, I still categorize this blog as a personal instead of an educational one. It's just my way to organize my school's stuffs properly. Even though I try to make sure the content of my blog accurate to my best knowledge, please don't be lazy and just take my word for it. Look through the formulas carefully and read the code line by line. It's also better for your understanding! If you have a hunch that something in my post is incorrect, there might be a good chance it is so. I'm more than delighted to read anything coming from my readers whether it is critic, feedback, correction or suggestion.

Since it's a personal blog, I will include some aspects of my life and thoughts that I would love to have them written. Along with some book, music, and play review. You can find these personal posts here in the [Home]() section. For other types of posts, you can find them in the toggleable sliding sidebar via **☰**.
