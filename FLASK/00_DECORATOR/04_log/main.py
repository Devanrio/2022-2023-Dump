import logging
from datetime import datetime

def record_log(original_function):
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrappers(*args, **kwargs):
        logging.info('{} Ran with args : {} and kwargs {}'.format(datetime.now(), args, kwargs))
        return original_function(*args, **kwargs)

    return wrappers

@record_log
def display_info(name, age, school="IGS Palembang"):
    print('display_info ran with argument ({} {} {})'.format(name, age, school))

@record_log
def display_something(*args, **kwargs):
    print(f"DONE! {args}, {kwargs}")

display_info("Kevin", 10)
display_something("1px", "solid", "Black", margin="10px")