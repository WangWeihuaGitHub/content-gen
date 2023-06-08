import openai
import time

# Set up OpenAI API credentials
openai.api_key = 'API-KEY' 

class GPT:

    def run(self, message):

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
                f"- amenities, shops and restaurants around {listing_address} with Urls.\n"
                "Email:")

            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=0.5,
                max_tokens=2048,
                n=1,
                stop=None,
                timeout=15,
            )

            # Extract the email text from the response
            email_text = response.choices[0].text.strip()

            # Print the email text
            print(f"Real estate lead response email:\n{email_text}\n")
            time.sleep(3)
