function [country,C,date0] = getDataSpain()
%GETDATA Coronavirus data
%  from Ministerio de Sanidad, Spain
%     https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov-China/situacionActual.htm
%  via ECDC (European Center for Disease Prevention and Control)
%     https://www.ecdc.europa.eu/en/corona
%
%  as reported by One World in Data
%     https://ourworldindata.org/coronavirus-source-data
%
%  other sources: 
%     RTVE Spain, https://www.rtve.es/noticias/20200325/mapa-del-coronavirus-espana/2004681.shtml
%     https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Spain
%     https://www.worldometers.info/coronavirus/country/spain/
%
%  2020/03/24

country = 'Spain';
date0=datenum('2020/02/29'); % start date

C = [
%1
%1
%1
%1
%1
%1
%1
%1
%1
%2
%2
%2
%2
%2
%2
%2
%2
%2
%2
%2
%2
%2
%2
%2
3 % 2020/02/25
7 % 2020/02/26
12 % 2020/02/27
25 % 2020/02/28
34 % 2020/02/29
66 % 2020/03/01
83 % 2020/03/02
114 % 2020/03/03
151 % 2020/03/04
200 % 2020/03/05
261 % 2020/03/06
374 % 2020/03/07
430 % 2020/03/08
589 % 2020/03/09
1204 % 2020/03/10
1639 % 2020/03/11
2140 % 2020/03/12
3004 % 2020/03/13
4231 % 2020/03/14
5753 % 2020/03/15
7753 % 2020/03/16
9191 % 2020/03/17
11178 % 2020/03/18
13716 % 2020/03/19
17147 % 2020/03/20
19980 % 2020/03/21
24926 % 2020/03/22
28572 % 2020/03/23
33089 % 2020/03/24
%<-------------- add new data here
]';
end

