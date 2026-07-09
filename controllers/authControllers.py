from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from models.Users import Users


def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # FIND USER
        user = Users.query.filter_by(Email=email).first()

        # CHECK USER EXISTS
        if not user:
            flash("Korisnik ne postoji.", "error")
            return render_template("pages/login.html", user=current_user)

        # CHECK ACTIVE STATUS
        if user.IsActive != 1:
            flash("Vaš nalog nije aktivan.", "error")
            return render_template("pages/login.html", user=current_user)

        # CHECK PASSWORD
        if user.Password != password:
            flash("Pogrešna lozinka.", "error")
            return render_template("pages/login.html", user=current_user)

    

        # 🔥 DEBUG USER (samo za testiranje)
        if user.IsActive == 1 and user.RoleId == 1:
            print("=== USER LOGIN DEBUG ===")
            print(user.serialize)
            print("========================")

        # LOGIN USER
        login_user(user)


        # ROLE REDIRECT
        if user.RoleId == 1:
            return redirect(url_for("user.home"))
        else:
            return redirect(url_for("admin.admin_dashboard"))

    return render_template("pages/login.html", user=current_user)


def logout():
    logout_user()
    flash("Uspješno ste se odjavili.", "success")
    return redirect(url_for("auth.login"))