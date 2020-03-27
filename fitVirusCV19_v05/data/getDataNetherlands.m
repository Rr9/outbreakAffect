function [country,C,date0] = getDataNetherlands()
%GETDATA Coronavirus data
%   data from RIVM Netherlands
%   source https://www.rivm.nl/en/news/current-information-about-novel-coronavirus-covid-19
%   as reported on https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_Netherlands
%
%   last change 2020/03/24 

country = 'Netherlands';
date0=datenum('2020/02/27'); % start date

C = [
1 % 2020/02/27
2 % 2020/02/28
7 % 2020/03/29
10 % 2020/03/01
18 % 2020/03/02
24 % 2020/03/03
38 % 2020/03/04
82 % 2020/03/05
128 % 2020/03/06
188 % 2020/03/07
265 % 2020/03/08
321 % 2020/03/09
382 % 2020/03/10
503 % 2020/03/11
614 % 2020/03/12
804 % 2020/03/13
959 % 2020/03/14
1135 % 2020/03/15
1413 % 2020/03/16
1705 % 2020/03/17
2051 % 2020/03/18
2460 % 2020/03/19
2994 % 2020/03/20
3631 % 2020/03/21
4204 % 2020/03/22
4749 % 2020/03/23
5560 % 2020/03/24
6412 % 2020/03/25
%<-------------- add new data here
]';
end

