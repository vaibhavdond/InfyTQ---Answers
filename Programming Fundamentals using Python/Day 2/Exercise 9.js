//Exercise-9

noOfFlightsTakeOff=100
noOfFlightsLanded=110
seatingCapacityTakeOff=150
seatingCapacityLanded=185
totalCookies=0


toatlPassengers = (noOfFlightsTakeOff*seatingCapacityTakeOff) + (noOfFlightsLanded*seatingCapacityLanded/2)
totalCookies = toatlPassengers*2

console.log(totalCookies)