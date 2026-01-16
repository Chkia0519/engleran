from flask import Flask, request, jsonify ,render_template
#import db

app = Flask(__name__)

#輸入單字卡
@app.route('/mylearnwords',methods=["GET"])
def index():
    return render_template('mylearnwords.html')


@app.route('/mywords',methods=['GET','POST'])
def learnWord():
    if request.method == 'GET':
        learnW = request.args.get('lenW')
    else:
        data = request.get_json(silent=True)
        learnW = (data.get('lenW') if data else request.form.get('lenW') or "").strip()

    if not learnW:
        # 後端回傳錯誤，前端可顯示「尚未輸入文字」
        return jsonify({"error": "尚未輸入文字"}), 400

    return jsonify({"lenW": learnW}), 200
# ...existing code...    

if __name__ == "__main__":
    app.run(debug=True)