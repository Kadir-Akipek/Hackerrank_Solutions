def bonAppetit(bill, k, b):
    fairybill = sum(bill) - bill[k]
    if fairybill / 2 == b:
        print("Bon Appetit")
    else:
        print(int(sum(bill)/2 - fairybill/2))