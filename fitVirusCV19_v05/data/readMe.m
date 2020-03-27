%Sources of the data
%The data in the 'getdata..DOTm' files are Total Confirmed Cases of Corona
%in 2020. The data have been collected by volunteers from multiple sources
%(WHO, ECDC, national health institutes, Worldometers, Our World in Data, 
%Wikipedia, journals, etc), have not been checked by these sources and may
%contain errors. Most of the 'getdata...DOTm' files contain in the header
%the source of the data and links to websites were numbers have been 
%collected and preferably a history of changes. 

%Data for other countries
%Data from the European Center for Disease Prevention and Control (ECDC)
%for many countries in the world can be found at Our World in Data, 
%https://ourworldindata.org/coronavirus-source-data.

%DISCLAIMER
%We do not take responsability or libability whatsoever with regard to the
%software and data provided.  The data have been collected by volunteers 
%from multiple public sources (WHO, ECDC, various national health 
%institutes, worldometers.info, Wikipedia, journals, etc), have not been
%checked by these sources and may contain errors. Parts of the software 
%and data can also be subject to rights by third parties, that the user 
%should respect.
%The data are only for demonstrating the operation of fitVirusCV19. FitVirus
%and presented demo data are only for educational and academic purposes and
%should not be used for medical purposes and in commerce. They are provided
%as is and any express or implied warranties, including but not limited to 
%implied warranties of merchantability and fitness for a particular purpose
%are disclaimed.

%Format example for 'getdata...DOTm' files
%In this example the first numbers were commented out

%function [country,C,date0] = getDataCountry()
%%GETDATA Coronavirus data
%%   data from <SOURCE>, as reported on
%%   <LINK>
%%
%%  <LAST EDITED>

%country = '<country>';
%date0=datenum(2020/03/01); % start date

%C = [
%%63 % 2020/02/28 % <-------------- add % <DATE> after each number
%%68 % 2020/02/29
%75 % 2020/03/01 % <-------------- current start date, copy to date0
%100 % 2020/03/02
%…
%43734 % 2020/03/23
%%<-------------- add new data here
%]';
%end
