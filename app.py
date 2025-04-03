from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

GROQ_URL="https://api.groq.com/v1/chat/completions"

@app.route("/bot",methods=['POST','GET'])
#response
def chatbot_response():
    try:
        if request.content_type != "application/json":
            return jsonify({"response":"Content-Type must be application/json"}), 415
        data= request.get_json()
        user_message=data.get("message","").strip()
        if not user_message:
            return jsonify({"response":"Please ask a financial question."})
        
        # Sending request to Groq API
        headers={"Authorization":f"Bearer {GROQ_API_KEY}",
                 "Content-Type":"application/json"}
        payload={
            "model":"llama3-8b-8192",
            "messages":[
                {"role":"system","content":"You are a financial advisor. Answer user queries about saving,investing,and budgeting."},
                {"role":"user","content":user_message},
            ],
            "temperature":0.7
        }

        response=requests.post(GROQ_URL,headers=headers,json=payload)
        if response.status_code== 200:
            bot_reply= response.json()["choices"][0]["message"]["content"]
            return jsonify({"response":bot_reply})
        else :
            return jsonify({"repsonse":"Error processing request."})
    except Exception as e:
        return jsonify({"response":f"Error: {str(e)}"})
    
if __name__=="__main__":
    app.run(host="0.0.0.0",)
