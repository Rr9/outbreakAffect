function [country,C,date0] = getDataGermany()
%GETDATA Coronavirus data
% data from Robert Koch Institute, Germany
% https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html
% as reported on https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Germany
%
% other sources:  https://www.worldometers.info/coronavirus/country/germany/
%
% 2020/03/24

country = 'Germany';
date0=datenum('2020/02/24'); % start date

C = [
16 % 2020/02/24
18 % 2020/02/25
26 % 2020/02/26
53 % 2020/02/27
66 % 2020/02/28
74 % 2020/02/29
117 % 2020/03/01
150 % 2020/03/02
188 % 2020/03/03
240 % 2020/03/04
349 % 2020/03/05
534 % 2020/03/06
684 % 2020/03/07
847 % 2020/03/08
1112 % 2020/03/09
1460 % 2020/03/10
1884 % 2020/03/11
2369 % 2020/03/12
3062 % 2020/03/13
3795 % 2020/03/14
4838 % 2020/03/15
6012 % 2020/03/16
7156 % 2020/03/17
8198 % 2020/03/18
10999 % 2020/03/19
13957 % 2020/03/20
16662 % 2020/03/21
18610 % 2020/03/22
22672 % 2020/03/23
27436 % 2020/03/24
31554 % 2020/03/25
%<-------------- add new data here
]';
end

