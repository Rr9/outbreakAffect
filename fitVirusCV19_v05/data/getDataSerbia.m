function [country, C,date0] = getDataSerbia()
%GETDATA Coronavirus data
%  https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Serbia
country = 'Serbia';
date0=datenum('2020/03/09'); % start date

C = [
2
5
18
24
35
46
48
57
72
89
103
135
171
222
249
303 % 20/03/24
384 % 20/03/25
%<-------------- add new data here
]';
end

