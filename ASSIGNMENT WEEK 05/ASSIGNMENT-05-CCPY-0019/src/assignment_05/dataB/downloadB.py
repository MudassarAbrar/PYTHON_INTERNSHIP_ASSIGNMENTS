
def main():
    
    import os
    from dotenv import load_dotenv

    # Automatically load environment variables from .env file
    load_dotenv()

    # Access environment variables securely
    kaggle_username = os.getenv('KAGGLE_USERNAME')
    kaggle_key = os.getenv('KAGGLE_KEY')


    
    if kaggle_username and kaggle_key:
        os.environ['KAGGLE_USERNAME'] = kaggle_username
        os.environ['KAGGLE_KEY'] = kaggle_key

        # Now use the Kaggle API
        os.system("kaggle datasets download -d camnugent/california-housing-prices")
    else:
        print("KAGGLE_USERNAME or KAGGLE_KEY not set!")
if __name__ == "__main__":
        main()
    