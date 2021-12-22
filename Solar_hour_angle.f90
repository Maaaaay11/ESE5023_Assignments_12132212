module Solar_hour_angle

    implicit none

    real, parameter     :: pi = 3.1415926536

contains

    subroutine CalSolarHourAngle(day,time,gma,longitude,timezone,h)
    
    integer, intent(in)    :: day
    real(8), intent(in)    :: time, longitude, timezone
    real(8)                :: gma, EOT, OFFSET, LST
    real(8), intent(out)   :: h

        gma = 2*pi/365*(day-1+(time-12)/24)
        EOT = 229.18*(0.000075+0.001868*COS(gma)-0.032077*SIN(gma)-0.014615*COS(2*gma)-0.040849*SIN(2*gma))
        OFFSET = EOT+4*(longitude-15*timezone)
        LST = time+OFFSET/60
        h = 15*(LST-12)

    end subroutine CalSolarHourAngle

end module Solar_hour_angle
