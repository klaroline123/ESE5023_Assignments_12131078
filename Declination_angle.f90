module Declination_angle
implicit none

contains      

subroutine Declination_angle(Declination,angle)
    implicit none   
    real, intent(in)  :: Declination
    real, intent(out)    :: angle
    real                 :: pi

    pi = 3.1415926

    angle = asin(sin(-23.44*pi/180)*cos((360/365.24*(D+10)+360*0.0167*sin(360*(D-2)/365.24)/pi) * pi / 180.))* 180. / pi
         

end subroutine Declination_angle 

end module Declination_angle