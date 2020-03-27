function [country, C,date0] = getDataSlovenia()
%GETDATA Coronavirus data for Slovenia
%  https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Slovenia
country = 'Slovenia';
date0=datenum('2020/03/04'); % start date

C = [
     1    % 4 marec
     6    % 5
     8    % 6
    12   % 7
    16   % 8
    25   % 9
    34   % 10
    57   % 11
    96   % 12
    141
    181
    219
    253
    275
    286
    319
    341
    383
    414
    442
    480
    526
%<-------------- add new data here
]';
end

