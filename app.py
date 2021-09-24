from flask import Flask, render_template, jsonify
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import json


app = Flask(__name__)
engine = create_engine(
    'postgresql://postgres:Humble123@@localhost:5432/hospitaldb')





@app.route("/dropdownzip")
def hospital():
    zip = pd.read_sql("""SELECT o
    FROM all_crime
    GROUP BY offense
    ORDER BY offense;""", engine)
    offense_list=offense_type.offense.to_list()
    return jsonify(offense_list)


    
if __name__ == "__main__":
    app.run(debug=True)
