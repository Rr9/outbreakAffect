function [country, C,date0] = getDataFrance()
%GETDATA Coronavirus data
%  from Agence Santé Publique France
%  https://www.santepubliquefrance.fr/maladies-et-traumatismes/maladies-et-infections-respiratoires/infection-a-coronavirus/articles/infection-au-nouveau-coronavirus-sars-cov-2-covid-19-france-et-monde
%  as reported on https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_France
%
%  2020/03/24

country = 'France';
date0=datenum('2020/02/28'); % start date

C = [
%    13 % 2020/02/25
%    18 % 2020/02/26
%    38 % 2020/02/27
    57 % 2020/02/28
    100 % 2020/02/29
    130 % 2020/03/01
    191 % 2020/03/02
    212 % 2020/03/03
    285 % 2020/03/04
    423 % 2020/03/05
    613 % 2020/03/06
    949 % 2020/03/07
    1126 % 2020/03/08
    1412 % 2020/03/09
    1784 % 2020/03/10
    2281 % 2020/03/11
    2876 % 2020/03/12
    3661 % 2020/03/13
    4499 % 2020/03/14
    5423 % 2020/03/15
    6633 % 2020/03/16
    7730 % 2020/03/17
    9134 % 2020/03/18
    10995 % 2020/03/19
    12612 % 2020/03/20
    14459 % 2020/03/21
    16689 % 2020/03/22
    19856 % 2020/03/23
    22302 % 2020/03/24
    25233 % 2020/03/25    
%<-------------- add new data here
]';
end

