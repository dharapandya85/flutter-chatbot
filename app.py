from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv
import json


app=Flask(__name__)
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
print("GROQ_API_KEY")
GROQ_URL="https://api.groq.com/openai/v1/chat/completions"

@app.route("/bot",methods=['POST'])
#response
def chatbot_response():
    if request.content_type != "application/json":
        return jsonify({"response":"Content-Type must be application/json"}), 415
    try:
        data= request.get_json()
        if not data or "message" not in data:
            return jsonify({"response":"Error:Missing 'message' in JSON body"}), 400
        user_message=data["message"].strip()
        
        
        # Sending request to Groq API
        headers={"Authorization": f"Bearer {GROQ_API_KEY}","Content-Type":"application/json"}
        payload={
            "model":"llama-3.3-70b-versatile",
            "messages":[
                {"role":"system","content":"You are a financial advisor. Answer user queries about saving,investing,and budgeting."},
                {"role":"user","content":user_message},
            ],
            "temperature":0.7
        }

        response=requests.post(GROQ_URL,headers=headers,json=payload)

        print("Groq API Response:", response.status_code,response.text)
        if response.status_code== 200:
            bot_reply= response.json()["choices"][0]["message"]["content"]
            return jsonify({"response":bot_reply})
        else :
            return jsonify({"repsonse":f"Error processing request.Groq API returned {response.text}"}),response.status_code
    except Exception as e:
        return jsonify({"response":f"Error: {str(e)}"}),500
 
    
if __name__=="__main__":
    app.run(host="0.0.0.0",)
