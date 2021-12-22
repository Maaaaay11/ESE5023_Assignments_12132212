program Main
    implicit none
    integer , parameter :: na = 3 , ma = 5 , nb = 5 , mb = 3
    Real(8)  :: M(3,5), N(5,3) , P (3 ,3)
    
open(unit=20, file='~/fortran_demo1/M.dat', status='old')

    read(20,*) M

close(20)

open(unit=20, file='~/fortran_demo1/N.dat', status='old')

    read(20,*) N

close(20)
    
call Matrix_multiply (M , na , ma ,N , mb , P )
    
open(unit=20, file='~/fortran_demo1/MN.dat', status='replace')

    write(20,'(3/(3f9.2))') P
    ! 3/ : 3 rows;  3f9.2 : f9.2 for 3 times.
close(20)

end program Main