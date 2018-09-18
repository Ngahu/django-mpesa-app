import random
import string



allowed_numbers = '123456789'
allowed_chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ'


def random_string_generator(size=10,chars=allowed_chars + allowed_numbers):
    return ''.join(random.choice(chars) for _ in range(size))





def unique_reference_id_generator(instance,size=10):
    """
    Description:Create a new unique_reference_id everytime a purchase is initialized.\n
    """
    new_id = random_string_generator(size=size)

    # get the class from the instance
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(unique_reference_id=new_id).exists()

    if qs_exists:
        return unique_reference_id_generator(size=size)
    
    return new_id
    