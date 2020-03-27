function [country, C,date0] = getDataNYState()
%GETDATA Coronavirus data
%  https://www.nijz.si/sl/dnevno-spremljanje-okuzb-s-sars-cov-2-covid-19
country = 'New York State';
date0=datenum('2020/03/04'); % start date

C = [
     11
     22
     44
     89
     105
     142
     173
     216
     325
     421
     613
     729
     950
     1347
     2480
     5711
     8402
     10356
     15168
     20875  % 20/03/23
     25665  % 20/03/24
     33030  % 20/03/25     
%<-------------- add new data here
]';
end

