function [country, C,date0] = getDatPoland()
%GETDATA Coronavirus data
%  https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Poland
country = 'Poland';
date0=datenum('2020/03/04'); % start date

C = [
   1
1
5
6
11
17
22
31
51
68
103
125
177
238
287
355
425
536
634
693
884
1031 
%<-------------- add new data here
]';
end

