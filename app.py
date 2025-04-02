from flask import Flask, jsonify, request
import time

app=Flask(__name__)
@app.route("/bot",methods=["POST"])

#response
def response():
    try:
        data= request.get_json()
        if not data or 'message' not  in data:
            return jsonify({"error":"Invalid request"}), 400
        query= data['message']
        bot_reply=f"Received:{query}"
        return jsonify({"response":bot_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    app.run(host="0.0.0..0",)
