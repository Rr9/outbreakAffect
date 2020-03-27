function [country, C,date0] = getDataBrazil()
%GETDATA Coronavirus data
%  https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Argentina
%  The plot in Timeline section seems to be up-to-date
country = 'Brazil';
date0=datenum('2020/03/04'); % start date

C = [
    4
    7
    13
    19
    25
    30
    34
    52
    77
    98
    121
    200
    234
    290
    428
    621
    901
    1128
    1546
    1891
    2201
    2517 % 20/03/25
%<-------------- add new data here
]';
end

