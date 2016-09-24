# Author Rishab Shah rishah@bu.edu
M=5.97237*(10**24)
#lower bound
mu=3.9525627*(10**-25)
eu=92
lb=((M/mu)*eu)/(8*1.09951162778e+12)/2	
#upper bound
mh=1.6737236*(10**-27)
eh=1	
ub=((M/mh)*eh)/(8*1.09951162778e+12)*1.5
#average
mfe=9.273796*10**-26
pfe=.321
efe=26
mo=2.6567626*10**-26
po=.301
eo=8
msi=4.6637066*10**-26
psi=.151
esi=14
mmg=4.0359398*10**-26
pmg=.139
emg=12
ms=5.3245181*10**-26
ps=.029
es=16
mni=9.7462675*10**-26
pni=.018
eni=28
mca=6.6551079*10**-26
pca=.015
eca=20
mal=4.4803895*10**-26
pal=.014
eal=13
mna=3.8175407*10**-26
pna=.012
ena=11
mass=[mfe,mo,msi,mmg,ms,mni,mca,mal,mna]
percent=[pfe,po,psi,pmg,ps,pni,pca,pal,pna]
elec=[efe,eo,esi,emg,es,eni,eca,eal,ena]
avg=0.0
for i in range (0,9):
	avg+=((M/mass[i])*(percent[i]*elec[i]))/(8*1.09951162778e+12)*1.2
print(avg)
print(lb)
print(ub)
