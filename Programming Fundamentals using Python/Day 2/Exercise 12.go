//Exercise-12

package main
import "fmt"
func main(){
    var num1 int = 3
    var num2 int = 4
    var num3 int = 1
    if (num1>=num2 && num1>=num3) {
        fmt.Println(num1)
    }
    if (num2>=num1 && num2>=num3){
        fmt.Println(num2)
    }
    if (num3>=num1 && num3>=num2) {
        fmt.Println(num3)
    }
}