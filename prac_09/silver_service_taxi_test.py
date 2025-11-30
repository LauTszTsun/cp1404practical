from silver_service_taxi import SilverServiceTaxi

def main():
    """Test the silver service taxi"""
    taxi = SilverServiceTaxi("Test Taxi",100,2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())
if __name__ == '__main__':
    main()
