def check_payment(func):
    def wrapper(status):
        if status=="completed":
           print("payment completed")
        elif status=="pending":
           print("payment pending")
        elif status=="failed":
           print("payment failed")
        else:
            print("Invalid payment status")
        
        return func(status)
    return wrapper
@check_payment
def payment(status):
    print("checking payment status")
    
payment("completed")
payment("pending")
payment("failed")
               
           