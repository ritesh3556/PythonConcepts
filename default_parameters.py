# default parameters----->
def user_info(first_name,last_name,age):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info("ritesh","gupta",20)    


def user_info(first_name,last_name,age=20):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info("ritesh","gupta")    


def user_info(first_name,last_name="gupta",age=20):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info("ritesh")

def user_info(first_name,last_name="gupta",age=None):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info("ritesh")    




def user_info(first_name="rietsh",last_name="gupta",age=None):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info()    

def user_info(first_name="ritesh",last_name=None,age=None):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info()    


def user_info(first_name=None,last_name=None,age=None):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info()    


