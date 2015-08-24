# Martingdale Gambling Strategy

This is a simulation of the [Martingale](https://en.wikipedia.org/wiki/Martingale_(betting_system)) gambling strategy applied to the game of roulette.  The bettor starts every session by placing a bet on red.  If the bettor loses, they simply double the bet for the next spin.  This is repeated until the bettor wins.  At this point the better will be up 1 bet and starts the process over.

A quick observation will tell you that casinos are still in business so this strategy must be flawed!  There are two practical limitations to this strategy - 1) The bettor doesn't have infinite funds, 2) A table will have a maximum bet size.

This python simulation is inspired after this [blog post](http://blog.godatadriven.com/lazy%20plot.html) which uses R.

#Contents:

The file gambler.py runs two gambling simulations based on the game of roulette.  The first simulates 200 series of 500 equal bets using the probability of winning in roulette.  The odds of winning an individual bet is 18/37.  The second simulation implements the Martingdale system with the following default values: Starting bet = 1, Starting money = 500 and a maximum allowed bet of 1024.