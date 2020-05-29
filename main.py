   
import kivy   
        
from kivy.app import App  
from kivy.core.window import Window
kivy.require('1.9.0')  
  
from kivy.uix.gridlayout import GridLayout 

from kivy.config import Config 

Window.size = (300, 400)
Window.clearcolor = (0.5,0.5,0.5,1)
  
  
class CalculatorFrm(GridLayout): 
    def calculate(self, calculation): 
        if calculation: 
            try: 
                self.display.text = str(eval(calculation)) 
            except Exception: 
                self.display.text = "Erro para calcular"

    def verify(self, count):
        if ['-','/','+','*',].__contains__(self.display.text[-1:]):
            return ''
        else:
            return count

   
class Calculator(App): 
   
    def build(self): 
        return CalculatorFrm() 
   
def main():
    calcApp = Calculator()
    calcApp.run() 

if __name__ == '__main__':
    main()