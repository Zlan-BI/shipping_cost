# write a function that determins the lowest shipping cost. 
# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$1.50	$20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
# Over 10 lb	$4.75	$20.00
# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# Flat_charge = 125
# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$4.50	$0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
# Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
# Over 10 lb	$14.25	$0.00


def groud_shipping(w):
  flat_fee = 20
  if w <= 2:
    price = 1.5
  elif w <= 6:
    price = 3
  elif w <= 10:
    price = 4
  elif w > 10:
    price = 4.75
  return price*w + flat_fee

def groud_shipping_premium(w):
  flat_fee = 125
  return flat_fee
  
def drone_shipping(w):
  flat_fee = 0
  if w <= 2:
    price = 4.5
  elif w <= 6:
    price = 9
  elif w <= 10:
    price = 12
  elif w > 10:
    price = 14.25
  return price*w + flat_fee
def best_shipping(w):
  x = groud_shipping(w)
  y = groud_shipping_premium(w)
  z = drone_shipping(w)
  lowest = [x, y, z]
  return min(lowest)

print(best_shipping(1))