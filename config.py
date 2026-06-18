import urllib

class Config:
    SECRET_KEY = "super-secret-key"

    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-RJOE23L\\STUDENTSQLSERVER;"
        "DATABASE=GYM_APP;"
        "Trusted_Connection=yes;"
    )

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc:///?odbc_connect=" + params
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False