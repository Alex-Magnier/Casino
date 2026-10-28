from flask import Flask, render_template # rajouter request au besoin
def profile_func(username, coins):
    return render_template("profile.html", pseudo=username, coin=coins)