from flask import render_template
from sqlalchemy import select

from app import app
from models import Player
from settings import Session


@app.route("/player", methods=["GET", "POST"])
def player():
    with Session() as session:
        stmt = select(Player).where(Player.id == 1)
        team = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 2)
        team1 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 3)
        team2 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 4)
        team3 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 5)
        team4 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 6)
        team5 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 7)
        team6 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 8)
        team7 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 9)
        team8 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Player).where(Player.id == 10)
        team9 = session.scalars(stmt).first()
    return render_template(
        "player.html",
        team=team,
        team1=team1,
        team2=team2,
        team3=team3,
        team4=team4,
        team5=team5,
        team6=team6,
        team7=team7,
        team8=team8,
        team9=team9,
    )


@app.route("/simple")
def simple():
    with Session() as session:
        stmt = select(Player).where(Player.id == 1)
        player = session.scalars(stmt).first()
    return render_template("/players/simple.html", player=player)


@app.route("/dupreeh")
def dupreeh():
    with Session() as session:
        stmt = select(Player).where(Player.id == 2)
        player = session.scalars(stmt).first()
    return render_template("/players/dupreeh.html", player=player)


@app.route("/device")
def device():
    with Session() as session:
        stmt = select(Player).where(Player.id == 3)
        player = session.scalars(stmt).first()
    return render_template("/players/dev1ce.html", player=player)


@app.route("/fallen")
def fallen():
    with Session() as session:
        stmt = select(Player).where(Player.id == 4)
        player = session.scalars(stmt).first()
    return render_template("/players/fallen.html", player=player)


@app.route("/cold")
def cold():
    with Session() as session:
        stmt = select(Player).where(Player.id == 5)
        player = session.scalars(stmt).first()
    return render_template("/players/coldzera.html", player=player)


@app.route("/kennys")
def kennys():
    with Session() as session:
        stmt = select(Player).where(Player.id == 6)
        player = session.scalars(stmt).first()
    return render_template("/players/kennys.html", player=player)


@app.route("/niko")
def niko():
    with Session() as session:
        stmt = select(Player).where(Player.id == 7)
        player = session.scalars(stmt).first()
    return render_template("/players/niko.html", player=player)


@app.route("/xyp9x")
def xyp9x():
    with Session() as session:
        stmt = select(Player).where(Player.id == 8)
        player = session.scalars(stmt).first()
    return render_template("/players/xyp9x.html", player=player)


@app.route("/krimz")
def krimz():
    with Session() as session:
        stmt = select(Player).where(Player.id == 9)
        player = session.scalars(stmt).first()
    return render_template("/players/krimz.html", player=player)


@app.route("/olof")
def olof():
    with Session() as session:
        stmt = select(Player).where(Player.id == 10)
        player = session.scalars(stmt).first()
    return render_template("/players/olof.html", player=player)


if __name__ == "__main__":
    app.run(debug=True)
