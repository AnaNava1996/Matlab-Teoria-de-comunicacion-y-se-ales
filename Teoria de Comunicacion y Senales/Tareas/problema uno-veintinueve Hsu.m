t=0:0.1:4*pi;
yn=0;
n = input('value of n: ');
for k=1:n
    yn=yn+(  sin((2*k-1)*t+pi) * (4/((2*k-1)*pi))   );
end
plot(t,yn)
title('Fourier Series representation')
xlabel('F(t)')
legend(strcat('n=',num2str(n)),'f(t)')