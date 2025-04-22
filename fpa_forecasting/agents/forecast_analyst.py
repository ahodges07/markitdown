import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_forecast_narrative(forecast, model="gpt-4o"):
    numbers = ", ".join([str(x) for x in forecast])
    prompt = f"Based on the forecasted monthly revenue numbers: {numbers}, write a 2-paragraph SaaS-style FP&A analysis. Mention any trends, assumptions, and what the business should watch out for."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an experienced SaaS FP&A analyst who writes executive summaries for board decks."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
