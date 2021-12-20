Program Main

Implicit none

integer :: k,j,i,s

real(4),dimension(:),allocatable :: a,b,c,d,e
real(4),dimension(5,3) :: m
real(4),dimension(3,5) :: n
real(4) :: mn(3,3)

open(unit = 50, file = 'M.dat', status = 'old')
open(unit = 60, file = 'N.dat', status = 'old')

k = 5

allocate(a(k),b(k),c(k))

do i = 1,5
  read(50,*) a(i),b(i),c(i)
enddo

m(:,1)=a(:)
m(:,2)=b(:)
m(:,3)=c(:)

deallocate(a,b,c)

j = 3

allocate(a(j),b(j),c(j),d(j),e(j))


do s=1,3
  read(60,*) a(s),b(s),c(s),d(s),e(s)
enddo

n(:,1)=a(:)
n(:,2)=b(:)
n(:,3)=c(:)
n(:,4)=d(:)
n(:,5)=e(:)


deallocate(a,b,c,d,e)

close(50)
close(60)

mn = matrix_multiply(m,n)
print*,mn

open(100,file = 'MN.dat',status = 'replace')

do i=1,3
  write(100,'MN.dat') (mn(i,j), j=1,3)
enddo

close(100)

End Program Main




real(4) function matrix_multiply(m,n)


real(4), dimension(:) :: m,n
real(4), dimension(3,3) :: mn

integer :: i
do i=1,3
  mn(1,i)=dot_product(n(i,:),m(:,1))
enddo

do i=1,3
  mn(2,i)=dot_product(n(i,:),m(:,2))
enddo

do i=1,3
  mn(3,i)=dot_product(n(i,:),m(:,3)))
enddo


end function matrix_multiply