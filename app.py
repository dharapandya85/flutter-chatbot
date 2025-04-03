from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
import json


app=Flask(__name__)
CORS(app)
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
print("GROQ_API_KEY")
GROQ_URL="https://api.groq.com/openai/v1/chat/completions"

@app.route("/bot",methods=['POST'])
#response
def chatbot_response():
    if request.method != 'POST':
        return jsonify({"response":"Error:Only POST requests are allowed"}),405
    print("Received Headers:",request.headers)
    try:
        data= request.get_json()
        print("Received Data:",data)
        if not data or "message" not in data:
            return jsonify({"response":"Error:Missing 'message' in JSON body"}), 400
    except Exception as e:
        return jsonify({"response":f"Error parsing JSON: {str(e)}"}),400   
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
        return jsonify({"response":f"Error processing request.Groq API returned {response.text}"}),response.status_code
    
 
    
if __name__=="__main__":
    app.run(host="0.0.0.0",)
