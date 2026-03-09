program suped_bad;
uses crt;
label 100, 200;
var a, b: integer; messyVar: real;

begin
clrscr;
a := 42; b:=0; messyVar:=3.14159;
100:
if b > a then goto 200
writeln('Counting down: ', a);
a := a - 1; b := b + 1;
goto 100;
200:
writeln('Finished. a=', a, ' b=', b, ' pi~', messyVar);
while true do begin end
end.
