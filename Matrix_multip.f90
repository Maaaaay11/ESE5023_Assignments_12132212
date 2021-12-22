subroutine Matrix_multip (C ,D , P )
    implicit none
    integer  i , j , k    
    integer , parameter :: nc = 3 , mc = 5 , md = 3
    real , intent ( in ) :: C ( nc , mc ) , D ( mc , md )
    real , intent ( out ) :: P ( nc , md )
    real :: sum

    do i =1 , nc
    do j =1 , md
    sum = 0.
    do k =1 , mc
    sum = sum + C (i , k )* D (k , j )
    enddo
    P (i , j ) = sum
    enddo
    enddo
    
end subroutine Matrix_multip