package main

import "fmt"

func main() {
  var finalFee int
  var courseFee int = 25000
  var marks float32 = 70
  var extraFees int = 1500
  var scholarship_received float32 = (marks/2.0) /100.0 * float32(courseFee)
  finalFee = courseFee - int(scholarship_received) + extraFees
  fmt.Println(finalFee)
}