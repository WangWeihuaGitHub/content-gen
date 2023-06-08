from gpt import GPT

leads = [
    {
        "customer_name" : "Alice",
        "listing_address" : "2257 W 30th Street, Los Angeles, 90018",
        "zip_code" : "90018",
        "bed" : 3,
        "bath" : 1,
        "walkscore" : 85,
    },
    {
        "customer_name" : "Bob",
        "listing_address" : "1528 NE 97th St, Seattle, WA 98115",
        "zip_code" : "98115",
        "bed" : 4,
        "bath" : 3.5,
        "walkscore" : 85,
    }
]

def main():
    gpt = GPT()
    gpt.run(message = leads)

if __name__ == "__main__":
    main()
