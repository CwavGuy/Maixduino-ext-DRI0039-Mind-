//% color="#4169E1" iconWidth=50 iconHeight=40
namespace EXT_DRI0039{
  
    //% block="DRI0039 Motor Init Board: PWM1pin [E1]DIR1pin [M1]PWM2pin [E2]DIR2pin [M2]PWM3pin [E3]DIR3pin [M3]PWM4pin [E4]DIR4pin [M4] " blockType="command"
    //% E1.shadow="dropdown" E1.options="E1" 
    //% M1.shadow="dropdown" M1.options="M1"
    //% E2.shadow="dropdown" E2.options="E2"   
    //% M2.shadow="dropdown" M2.options="M2"
    //% E3.shadow="dropdown" E3.options="E3" 
    //% M3.shadow="dropdown" M3.options="M3"
    //% E4.shadow="dropdown" E4.options="E4"   
    //% M4.shadow="dropdown" M4.options="M4"
    export function DRI0039Init(parameter: any, block: any) {      
      let e1=parameter.E1.code;  
      let m1=parameter.M1.code;
      let e2=parameter.E2.code;  
      let m2=parameter.M2.code;
      let e3=parameter.E3.code;  
      let m3=parameter.M3.code;
      let e4=parameter.E4.code;  
      let m4=parameter.M4.code;
     
      Generator.addImport('from board import board_info',true);
      Generator.addImport('from fpioa_manager import fm',true);
      Generator.addImport('from Maix import GPIO',true);
      Generator.addImport('from machine import Timer,PWM',true);
      Generator.addImport('from dri0039 import Dri0039',true);
      Generator.addCode(`dri = Dri0039(${e1}, ${m1}, ${e2}, ${m2}, ${e3}, ${m3}, ${e4}, ${m4})`);   
    }
    
    
    //% block="DRI0039 Motor Board: Motor [MOTOR]Dir [FR]Speed[SPEED] " blockType="command"
    //% MOTOR.shadow="dropdownRound" MOTOR.options="MOTOR" 
    //% FR.shadow="dropdownRound" FR.options="FR"
    //% SPEED.shadow="range" SPEED.params.min="0" SPEED.params.max="100" SPEED.defl="50"
    export function DRI0039Init1(parameter: any, block: any) {      
      let fr=parameter.FR.code;  
      let speed=parameter.SPEED.code;
      let m=parameter.MOTOR.code;
     
      Generator.addImport('from board import board_info',true);
      Generator.addImport('from fpioa_manager import fm',true);
      Generator.addImport('from Maix import GPIO',true);
      Generator.addImport('from machine import Timer,PWM',true);
      Generator.addImport('from dri0039 import Dri0039',true);
      Generator.addCode(`dri.setSpeed(${m}, ${fr}, ${speed})`);
    }


    //% block="DRI0039 Board: Motor [MOTOR] " blockType="command"
    //% MOTOR.shadow="dropdownRound" MOTOR.options="MOTOR" 
    export function DRI0039Init2(parameter: any, block: any) {      
      let m=parameter.MOTOR.code;

      Generator.addImport('from board import board_info',true);
      Generator.addImport('from fpioa_manager import fm',true);
      Generator.addImport('from Maix import GPIO',true);
      Generator.addImport('from machine import Timer,PWM',true);
      Generator.addImport('from dri0039 import Dri0039',true);
      Generator.addCode(`dri.stop(${m})`);
    }
    
    //% block="Delete DRI0039 Motor Board Object" blockType="command"
    export function DRI0039Init3(parameter: any, block: any) {      
      Generator.addImport('from board import board_info',true);
      Generator.addImport('from fpioa_manager import fm',true);
      Generator.addImport('from Maix import GPIO',true);
      Generator.addImport('from machine import Timer,PWM',true);
      Generator.addImport('from dri0039 import Dri0039',true);
      Generator.addCode(`dri.__del__()`);   
    }

}