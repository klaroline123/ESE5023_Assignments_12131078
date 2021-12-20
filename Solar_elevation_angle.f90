program Solar_elevation_angle

use Declination_angle
use Solar_hour_angle

implicit none
real                 :: pi
real :: d, h, SEA, lat, Declination, localsolartime, angle
integer,dimension(12) :: months_num
integer :: mon,day,year

pi        =  3.14
months_num      = (/31,28,31,30,31,30,31,31,30,31,30,31/)

year = 2021
mon  = 12
day  = 31

d = 365-sum(months_num(mon:))+day

localsolartime = 10.53 

Declination=d+localsolartime/24
call Declination_angle(Declination,angle)
call solar_hour_angle(localsolartime,h)

if (A < 0) then
    A=-A
 endif

lat = 22.54

SEA = 180-asin(sin(lat*pi/360)*sin(A*pi/360)+cos(lat*pi/360)*cos(A*pi/360)*cos(h*pi/360))*360/pi


endprogram Solar_elevation_angle