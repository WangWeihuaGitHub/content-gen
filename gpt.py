import openai
import time

# Set up OpenAI API credentials
openai.api_key = 'API_KEY' 

class GPT:

    def run(self, message):
        init_prompt = "You act as the real estate agent, your task is to write emails to potential customers"

        for lead in message:
            customer_name = lead['customer_name']
            listing_address = lead['listing_address']
            zip_code = lead['zip_code']
            bed = lead['bed']
            bath = lead['bath']
            walkscore = lead['walkscore']

            prompt = (f"Write an email response to a real estate lead who has shown interest in a {bed} bed {bath} bath property at {listing_address}.\n"
                f"The lead's name is {customer_name}.\n"
                f"The property's address is {listing_address}.\n"
                f"The property's zip_code is {zip_code}.\n"
                f"The property's walkscore is {walkscore}.\n"
                "Please make sure to find and provide the following information with more details and urls:\n"
                f"- schools with name, ranking around {listing_address} with Urls.\n"
                f"- amenities, shops and restaurants around {listing_address} with Urls."
            )
            model = [
                {"role": "system", "content": init_prompt},
                {"role": "user", "content": prompt}
            ]

            results = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0.5,
                messages=model,
            )

            # Extract the email text from the response
            email_text = results.choices[0].message.content.strip()
            # Print the email 
            print(f"Real estate lead response email:\n{email_text}\n")
            #time.sleep(3)
