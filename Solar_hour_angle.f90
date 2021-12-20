module Solar_hour_angle
implicit none

contains

subroutine Solar_hour_angle( localsolartime ,h)
    real, intent(in) :: localsolartime 
    real, intent(out)  :: h

    h = 15*( localsolartime -12)


end subroutine Solar_hour_angle

end module Solar_hour_angle