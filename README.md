## make requirements.txt file and procfile

## deploy your backend on railway.com

## assign an GROQ_API_KEY 

## test your chatbot

curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
     -H "Authorization: Bearer your_actual_api_key" \
     -H "Content-Type: application/json" \
     -d '{"model":"llama3-8b-8192","messages":[{"role":"user","content":"Hello"}]}'

{"id":"chatcmpl-634afeac-833c-45d5-9a76-cad775afe1ed","object":"chat.completion","created":1743673633,"model":"llama3-8b-8192","choices":[{"index":0,"message":{"role":"assistant","content":"Hello! It's nice to meet you. Is there something I can help you with, or would you like to chat?"},"logprobs":null,"finish_reason":"stop"}],"usage":{"queue_time":0.234034811,"prompt_tokens":11,"prompt_time":0.001803018,"completion_tokens":26,"completion_time":0.021666667,"total_tokens":37,"total_time":0.023469685},"usage_breakdown":{"models":null},"system_fingerprint":"fp_a97cfe35ae","x_groq":{"id":"req_01jqxgra1me0abh9e749bqwcwn"}}
