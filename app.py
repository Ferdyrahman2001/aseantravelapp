from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi konversi
def usdToRupiah(nilai):
    kurs = 15.880
    return nilai * kurs

def ringgitToRupiah(nilai):
    kurs = 3.553
    return nilai * kurs

def euroToRupiah(nilai):
    kurs = 16.540
    return nilai * kurs

def yenToRupiah(nilai):
    kurs = 102.6
    return  nilai * kurs

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert/<currency>", methods=["GET", "POST"])
def convert(currency):
    result = None
    if request.method == "POST":
        try:
            nilai = float(request.form["nilai"])
            if currency == "usd":
                result = usdToRupiah(nilai)
            elif currency == "myr":
                result = ringgitToRupiah(nilai)
            elif currency == "eur":
                result = euroToRupiah(nilai)
            elif currency == "yen":
                result = yenToRupiah(nilai)
        except ValueError:
            result = "Invalid input. Please enter a number."
            
        result = "{:.3f}".format(result)
    
    return render_template("convert.html", currency=currency.upper(), result=result)

if __name__ == "__main__":
    app.run(debug=True)
