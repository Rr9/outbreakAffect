
function [country, C,date0] = getDataBelgium()
%GETDATA Coronavirus data
%  from FPS Health, Food Chain Safety and Environment, Belgium
%  https://www.info-coronavirus.be/en/news/
%  as presented on https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Belgium
%
%  other sources: https://www.vrt.be/vrtnws/nl/
%
%  2020/3/24

country = 'Belgium';
date0=datenum('2020/03/10'); % start date

C = [
%2 % 2020/03/01
%8 % 2020/03/02
%13 % 2020/03/03
%23 % 2020/03/04
%50 % 2020/03/05
%109 % 2020/03/06
%169 % 2020/03/07
%200 % 2020/03/08
%239 % 2020/03/09
267 % 2020/03/10
314 % 2020/03/11
399 % 2020/03/12
559 % 2020/03/13
689 % 2020/03/14
886 % 2020/03/15
1058 % 2020/03/16
1243 % 2020/03/17
1486 % 2020/03/18
1795 % 2020/03/19
2257 % 2020/03/20
2815 % 2020/03/21
3401 % 2020/03/22
3743 % 2020/03/23
4269 % 2020/03/24
%<-------------- add new data here
]';
end


