function [country,C,date0] = getDataSpain()
%GETDATA Coronavirus data
%   https://www.worldometers.info/coronavirus/country/spain/
%   https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Spain
country = 'Spain';
date0=datenum('2020/02/25'); % start date
C = [
    10
    14
    26
    34
59      %
84
125
169
228
282
365
430
674
1213
1695
2277
3146
5232
6391
7844
9942
11826
14769
18077
21571
25496
29909
35480
42058  % 20/03/024
49515  % 20/03/025
%<-------------- add new data here
]';
end

