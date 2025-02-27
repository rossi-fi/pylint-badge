# pybadge

A simple and functional pylint badge generator. Better to use [anybadge](https://github.com/jongracecox/anybadge) for most purposes.

## Howto

1. Install via `pip` or other method.
2. Run as follows: `pylint-badge script.py pylint.svg` which will produce a file `pylint.svg` in the current directory. 

## Color intervals

0.00 < ![pylint Score](https://mperlet.github.io/pybadge/badges/1.50.svg) < 3.00 < ![pylint Score](https://mperlet.github.io/pybadge/badges/5.51.svg) < 7.00 ![pylint Score](https://mperlet.github.io/pybadge/badges/9.73.svg) < 10.00

## Limitations

* Negative scores are not supported

## Idea
Inspired by mperlet's [pybadge](https://github.com/mperlet/pybadge), which was in turn inspired by [this blogpost](http://www.desmondrivet.com/blog/technical/pylint-badges.html.)
