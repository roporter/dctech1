from flask import Flask

app = Flask(__name__)

@app.route("/") def hello(): 
    return "<!DOCTYPE html><html lang='en'><head><link href='css/bootstrap.min.css' rel='stylesheet'><script src='js/bootstrap.min.js'></script></head><body><div class='container'><div class='row'><div class='col-xs-2 col-md-2'></div><div class='col-xs-6 col-md-4'><img src='http://www.xpressions.co.uk/ciscoevents/techhuddle/welcomeyt_files/TechHuddleLogo.png'></div><div class='col-xs-6 col -md-4'></div></div><div class='row' style='height:60px'><div class='col-md-2'>&nbsp</div></div><div class='row' style='align:center'><div class='col-xs-3 col-md-3'></div><div class='col-xs-4 col-m d-4'><a href='http://drone04.shipped-cisco.com/roporter/dctech1'><img src='http://drone04.shipped-cisco.com/api/badges/roporter/dctech1/status.svg' /></a></div></div><div class='row' style='height:60px'><div class='col-md-2'>&nbsp</div></div><div class='row' style='align:center'><div class='col-xs-3 col-md-3'></div><div class='col-xs-12 col-md-8' style='font-size:32px'>Welcome to the Tech Huddle April 2016!!!!</div></div></div></body></html>"






if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
