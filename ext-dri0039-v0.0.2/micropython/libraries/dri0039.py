# MindPlus
# maixduino
from board import board_info
from fpioa_manager import fm
from Maix import GPIO
from machine import Timer,PWM

# Class for DRI0039
class Dri0039:
  global board_info,fm,GPIO,Timer,PWM
  # Class Variable
  _PIN_PWM1 = None
  _PIN_DIR1 = None
  _PIN_PWM2 = None
  _PIN_DIR2 = None
  _PIN_PWM3 = None
  _PIN_DIR3 = None
  _PIN_PWM4 = None
  _PIN_DIR4 = None
  _Object_TIM1 = None
  _Object_TIM2 = None
  _Object_TIM3 = None
  _Object_TIM4 = None
  _Object_PWM1 = None
  _Object_PWM2 = None
  _Object_PWM3 = None
  _Object_PWM4 = None
  _Object_DIR1 = None
  _Object_DIR2 = None
  _Object_DIR3 = None
  _Object_DIR4 = None
  
      
  # The init method or constructor
  def __init__(self,pwm1,dir1,pwm2,dir2,pwm3,dir3,pwm4,dir4):
    global board_info,fm,GPIO,Timer,PWM
    self._PIN_PWM1 = pwm1
    self._PIN_DIR1 = dir1
    self._PIN_PWM2 = pwm2
    self._PIN_DIR2 = dir2
    self._PIN_PWM3 = pwm3
    self._PIN_DIR3 = dir3
    self._PIN_PWM4 = pwm4
    if(dir4 == board_info.PIN7):
      self._PIN_DIR4 = 15
    else:
      self._PIN_DIR4 = dir4
      
    # Register GPIO
    fm.register(self._PIN_DIR1, fm.fpioa.GPIO1)
    fm.register(self._PIN_DIR2, fm.fpioa.GPIO2)
    fm.register(self._PIN_DIR3, fm.fpioa.GPIO3)
    fm.register(self._PIN_DIR4, fm.fpioa.GPIO4)
    # Set GPIO function
    self._Object_DIR1 = GPIO(GPIO.GPIO1, GPIO.OUT)
    self._Object_DIR2 = GPIO(GPIO.GPIO2, GPIO.OUT)
    self._Object_DIR3 = GPIO(GPIO.GPIO3, GPIO.OUT)
    self._Object_DIR4 = GPIO(GPIO.GPIO4, GPIO.OUT)
    # Init Timer
    self._Object_TIM1 = Timer(Timer.TIMER1, Timer.CHANNEL0, mode=Timer.MODE_PWM)
    self._Object_TIM2 = Timer(Timer.TIMER1, Timer.CHANNEL1, mode=Timer.MODE_PWM)
    self._Object_TIM3 = Timer(Timer.TIMER1, Timer.CHANNEL2, mode=Timer.MODE_PWM)
    self._Object_TIM4 = Timer(Timer.TIMER1, Timer.CHANNEL3, mode=Timer.MODE_PWM)
    #Set PWM
    self._Object_PWM1 = PWM(self._Object_TIM1, 100000, 0, pin=self._PIN_PWM1, enable=True)
    self._Object_PWM2 = PWM(self._Object_TIM2, 100000, 0, pin=self._PIN_PWM2, enable=True)
    self._Object_PWM3 = PWM(self._Object_TIM3, 100000, 0, pin=self._PIN_PWM3, enable=True)
    self._Object_PWM4 = PWM(self._Object_TIM4, 100000, 0, pin=self._PIN_PWM4, enable=True)
  
  
  def __del__(self):
    global board_info,fm,GPIO,Timer,PWM
    fm.unregister(self._PIN_DIR1)
    fm.unregister(self._PIN_DIR2)
    fm.unregister(self._PIN_DIR3)
    fm.unregister(self._PIN_DIR4)
    self._Object_PWM1.disable()
    self._Object_PWM2.disable()
    self._Object_PWM3.disable()
    self._Object_PWM4.disable()
    self._Object_TIM1.deinit()
    self._Object_TIM2.deinit()
    self._Object_TIM3.deinit()
    self._Object_TIM4.deinit()
    self._Object_PWM1.deinit()
    self._Object_PWM2.deinit()
    self._Object_PWM3.deinit()
    self._Object_PWM4.deinit()
  
  
  def setSpeed(self,Motor,FR,Speed):
    global board_info,fm,GPIO,Timer,PWM
    if   (Motor == 1 and FR == 1):
      self._Object_DIR1.value(0)
      self._Object_PWM1.duty(Speed)
    elif (Motor == 1 and FR == 2):
      self._Object_DIR1.value(1)
      self._Object_PWM1.duty(Speed)
    elif (Motor == 2 and FR == 1):
      self._Object_DIR2.value(1)
      self._Object_PWM2.duty(Speed)
    elif (Motor == 2 and FR == 2):
      self._Object_DIR2.value(0)
      self._Object_PWM2.duty(Speed)
    elif (Motor == 3 and FR == 1):
      self._Object_DIR3.value(0)
      self._Object_PWM3.duty(Speed)
    elif (Motor == 3 and FR == 2):
      self._Object_DIR3.value(1)
      self._Object_PWM3.duty(Speed)
    elif (Motor == 4 and FR == 1):
      self._Object_DIR4.value(1)
      self._Object_PWM4.duty(Speed)
    elif (Motor == 4 and FR == 2):
      self._Object_DIR4.value(0)
      self._Object_PWM4.duty(Speed)
  
  def stop(self,Motor):   
    global board_info,fm,GPIO,Timer,PWM
    if Motor == 1:
      self._Object_PWM1.duty(0)
    elif Motor == 2:
      self._Object_PWM2.duty(0)
    elif Motor == 3:
      self._Object_PWM3.duty(0)
    elif Motor == 4:
      self._Object_PWM4.duty(0)

