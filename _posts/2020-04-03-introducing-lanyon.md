---
layout: post
title: There will be a good title for this
---

Obviously, it's getting harder and harder to solve scientific problems with only pen and paper. Not that people have nothing to do on a Friday evening but write down the state-space of $k$ harmonic oscillators with $n$ energy level per oscillator. Hence, I can't stress enough the significance of computer in the advancement of science. I can barely perform Gaussian elimination correctly on a 4x4 matrix so imagine a 15x15 matrix of atom coordinates of the simple methane molecule. You gotta leave that to the copmuter. However, as easy as the path to a quick answer may seem to be, the mine field is full of booby traps. You can run into serious problems with numerical calculation if you are not careful. Take for example if you evalue $f(x)=x^{3}+12 a^{2} x-6 a x^{2}-8 a^{3}=(x-2 a)^{3}$ with the parameter $a = 49999.5$ at $x_{0}=1000000.05$ with 2 different but equivalent transformations, you wil get immensely different results!
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

Thus, if you are not careful with numerical mathematics, problems including but not limited to cancelllation, Runge phenomenon may make your algorithm shockingly unstable. with this blog, I hope to lay out some of the pitfalls that I am aware of while simultaneously show you the overwhelming joy of simulating physical and theoretical problems. It's addictive!

However, I still categorize this blog as a personal instead of an educational one. I'm neither a mathematician, a computer scientist nor an expert in my field. Hence, even though I try to make sure the content of my blog accurate to my best knowledge, please don't be lazy and just take my word for it. Look through the formulas carefully and read the code line by line. It's also better for your understanding! If you have a hunch that something in my post is incorrect, there may be a good chance it is so. I'm more than delighted to read anything coming from my readers whether it is critic, feedback, correction or suggestion.

Since it's a personal blog, I will include some aspects of my life and thoughts that I would love to have them written. You can find these personal posts here in the [Home] section. For other types of posts, you can find them in the toggleable sliding sidebar.

### Built on Poole

Poole is the Jekyll Butler, serving as an upstanding and effective foundation for Jekyll themes by [@mdo](https://twitter.com/mdo). Poole, and every theme built on it (like Lanyon here) includes the following:

* Complete Jekyll setup included (layouts, config, [404](/404), [RSS feed](/atom.xml), posts, and [example page](/about))
* Mobile friendly design and development
* Easily scalable text and component sizing with `rem` units in the CSS
* Support for a wide gamut of HTML elements
* Related posts (time-based, because Jekyll) below each post
* Syntax highlighting, courtesy Pygments (the Python-based code snippet highlighter)

### Lanyon features

In addition to the features of Poole, Lanyon adds the following:

* Toggleable sliding sidebar (built with only CSS) via **☰** link in top corner
* Sidebar includes support for textual modules and a dynamically generated navigation with active link support
* Two orientations for content and sidebar, default (left sidebar) and [reverse](https://github.com/poole/lanyon#reverse-layout) (right sidebar), available via `<body>` classes
* [Eight optional color schemes](https://github.com/poole/lanyon#themes), available via `<body>` classes

[Head to the readme](https://github.com/poole/lanyon#readme) to learn more.

### Browser support

Lanyon is by preference a forward-thinking project. In addition to the latest versions of Chrome, Safari (mobile and desktop), and Firefox, it is only compatible with Internet Explorer 9 and above.

### Download

Lanyon is developed on and hosted with GitHub. Head to the <a href="https://github.com/poole/lanyon">GitHub repository</a> for downloads, bug reports, and features requests.

Thanks!
