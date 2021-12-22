module Declination_angle

    implicit none

    real(8), parameter      :: pi=3.1415926536

contains

    subroutine CalDeclinationAngle(day,sigma)

    integer, intent(in)     :: day
    real(8), intent(out)    :: sigma

!SIND=SIN(angle*pi/180)  COSD=COS(angle*pi/180)

        sigma = ASIND(SIND(-23.44)*COSD(360*(day+10)/365.24+360/pi*0.0167*SIN(360*(day-2)/365.24)))

    end subroutine CalDeclinationAngle

end module Declination_angle
