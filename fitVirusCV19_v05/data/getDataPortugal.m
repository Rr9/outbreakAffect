function [country,C,date0] = getDataPortugal()
%GETDATA Coronavirus data
%  https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Portugal
country = 'Portugal';
date0=datenum('2020/03/10'); % start date
C = [
    41
59
78
112
169
245
331
448
642
785
1020
1280
1600
2060
2362 % 20/03/24
2995 % 20/03/25
%<-------------- add new data here
]';
end

