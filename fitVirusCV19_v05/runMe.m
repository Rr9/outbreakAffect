close all
%w1 - weigth for values, w2 - weight for derivatives, prn - print results
%res = fitVirusCV19(@getDataGermany,'w1',1,'w2',1,'prn','on');
res = fitVirusCV19(@getDataUSA,'prn','on','nmax',1e4);
